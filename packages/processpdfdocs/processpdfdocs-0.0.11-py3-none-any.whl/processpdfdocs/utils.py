import json
import os
import cv2
# import pdfplumber
import fitz
import pdf2image
import pdftotext
import numpy as np
from PIL import Image
from ultralytics import YOLO

import onnxruntime as ort

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from paddleocr import PaddleOCR

classes = ['0', '180', '270', '90']

model_dir = os.getenv('MODEL_DIR', os.path.join(os.path.expanduser('~'), '.processpdfdocs', 'models'))

rotation_model = ort.InferenceSession(os.path.join(model_dir, 'rotation_model.onnx'))
rotation_model_input_name = rotation_model.get_inputs()[0].name
rotation_model_output_name = rotation_model.get_outputs()[0].name

config = Cfg.load_config_from_name('vgg_seq2seq')
config['cnn']['pretrained'] = False
config['device'] = "cpu"

detector = Predictor(config)

table_detector = YOLO(os.path.join(model_dir, 'table_detect_model.pt'))
cell_detector = YOLO(os.path.join(model_dir, 'cell_detect_model.pt'))

def is_text_selectable(pdf_path):
    if not pdf_path.lower().endswith('.pdf'):
        print("The file is not a PDF.")
        return False
    
    try:
        pdf_document = fitz.open(pdf_path)
        text_content_threshold = 150
        total_text_length = 0

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")
            total_text_length += len(text.strip())

        if total_text_length <= text_content_threshold:
            return False

        if total_text_length > text_content_threshold:
            common_signature_phrases = ["Digitally signed", "Signature", "Certified by", "Ngày ký:"]
            if any(phrase in text for phrase in common_signature_phrases):
                return False
            return True

    except Exception as e:
        print(f"An error occurred: {e}")
    return False

def generate_html_table(cells_dict):
    cells = list(cells_dict.items())

    # if not cells:
    #     return "<table></table>"

    cells.sort(key=lambda item: item[0][1])
    try:
        rows = []
        current_row = []
        current_y = cells[0][0][1]
    except:
        print('No cell detected')
        return ''
    threshold = 10

    for cell in cells:
        bbox = cell[0]
        if bbox[1] > current_y + threshold:
            rows.append(current_row)
            current_row = []
            current_y = bbox[1]
        current_row.append(cell)
    
    if current_row:
        rows.append(current_row)
    
    for row in rows:
        row.sort(key=lambda item: item[0][0])

    html = "<table>\n"
    for row in rows:
        html += "  <tr>\n"
        for cell in row:
            cell_text = cell[1].replace("\n", "<br>")
            html += f"    <td>{cell_text}</td>\n"
        html += "  </tr>\n"
    html += "</table>"

    return html

def extract_table_from_pdf(pdf_path, page_num=None):
    with open(pdf_path, "rb") as f:
        pdf = pdftotext.PDF(f, physical=True)

    pdf_return = []

    for i, page in enumerate(pdf):
        pdf_return.append(page)
        pdf_return.append("\n\n")
        print(f"Page {i + 1}...\n")
        # pdf_return.append('#' * 100)

    return pdf_return

def ocr_pdf_to_text_and_html(pdf_path):

    results = []

    if not is_text_selectable(pdf_path):
        if pdf_path.lower().endswith('.pdf'):
            images = pdf2image.convert_from_path(pdf_path)
            # table_detector = YOLO('models/table_detect_model.pt')
            # cell_detector = YOLO('models/cell_detect_model.pt')
            for i, image in enumerate(images):
                print(type(image))
                print("Page: ", i + 1)
                a_page_output = []

                # cv2_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                try:    
                    resized_img = image.resize((480, 480))
                    rotation_result = rotation_model.run([rotation_model_output_name], {rotation_model_input_name: np.array([resized_img], dtype=np.float32)/255.0})
                    rotation_angle = int(classes[np.argmax(rotation_result[0])])
                    if rotation_angle==0:
                        rotated_image = image
                    elif rotation_angle==180:
                        rotated_image = image.rotate(180)
                    elif rotation_angle==270:
                        rotated_image = image.rotate(270, expand=True)
                    else:
                        rotated_image = image.rotate(90, expand=True)
                    cv2_img = cv2.cvtColor(np.array(rotated_image), cv2.COLOR_RGB2BGR)
                    pdf_file_name = os.path.basename(pdf_path)
                    pdf_file_name = os.path.splitext(pdf_file_name)[0]
                    # image_path = os.path.join(temp_image_converted_path, f'{pdf_file_name}_{i}.jpg')
                    # cv2.imwrite(image_path, cv2_img)
                    # try:
                    table_detect_results = table_detector.predict(cv2_img, conf=0.6)

                    table_regions = []
                    rotate_times = 0
                    for result in table_detect_results[0].boxes.cpu().xyxy.numpy():
                        paddle = PaddleOCR(
                                            # enable_mkldnn=True, 
                                            # use_tensorrt=False, 
                                            use_angle_cls=False, 
                                            lang="vi", 
                                            use_gpu=False,
                                            # gpu_mem=4096,
                                        )
                        x1, y1, x2, y2 = result
                        table_regions.append((x1, y1, x2, y2))
                        only_table_image = cv2_img[int(y1):int(y2), int(x1):int(x2)]

                        cell_detect_results = cell_detector.predict(only_table_image)
                        cell_and_its_text = {}

                        for cell_result in cell_detect_results[0].boxes.cpu().xyxy.numpy():
                            cx1, cy1, cx2, cy2 = cell_result
                            cell_image = only_table_image[int(cy1):int(cy2), int(cx1):int(cx2)]
                            if cell_image is None:
                                continue
                            try:
                                paddle_result = paddle.ocr(cell_image, cls=False, det=True)
                                paddle_result = paddle_result[:][:][0]
                                boxes = []
                                for line in paddle_result:
                                    line = line[0]
                                    boxes.append([[int(line[0][0]), int(line[0][1])], [int(line[2][0]), int(line[2][1])]])
                            except SystemExit as e:
                                print("Caught SystemExit:", e)
                                continue
                            except Exception as e:
                                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                print(e)
                                continue

                            EXPEND = 5
                            for box in boxes:
                                box[0][0] -= EXPEND
                                box[0][1] -= EXPEND
                                box[1][0] += EXPEND
                                box[1][1] += EXPEND

                            texts = []
                            for box in boxes:
                                cropped_image = cell_image[box[0][1]:box[1][1], box[0][0]:box[1][0]]
                                try:
                                    cropped_image = Image.fromarray(cropped_image)
                                    rec_result = detector.predict(cropped_image)
                                    text = rec_result
                                    texts.append(text)
                                except Exception as e:
                                    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                                    continue

                            cell_and_its_text[(cx1, cy1, cx2, cy2)] = '\n'.join(texts)

                        html_table = generate_html_table(cell_and_its_text)
                        a_page_output.append(((x1, y1, x2, y2), html_table, 'table'))
                    # except:
                    #     print("Exception")
                    #     continue
                    paddle = PaddleOCR(
                                        # enable_mkldnn=True, 
                                        # use_tensorrt=False, 
                                        use_angle_cls=False, 
                                        lang="vi", 
                                        use_gpu=False,
                                        # gpu_mem=4096,
                                    )
                    try:
                        ocr_result = paddle.ocr(cv2_img, cls=False, det=True)
                        ocr_result = ocr_result[:][:][0]
                        text_boxes = []
                        for line in ocr_result:
                            line = line[0]
                            text_boxes.append([[int(line[0][0]), int(line[0][1])], [int(line[2][0]), int(line[2][1])]])
                    except SystemExit as e:
                        print("Caught SystemExit:", e)
                        continue
                    except:
                        continue
                    EXPEND = 5
                    for box in text_boxes:
                        box[0][0] -= EXPEND
                        box[0][1] -= EXPEND
                        box[1][0] += EXPEND
                        box[1][1] += EXPEND

                    for box in text_boxes:
                        x1, y1, x2, y2 = box[0][0], box[0][1], box[1][0], box[1][1]
                        overlaps = any((x1 < tx2 and x2 > tx1 and y1 < ty2 and y2 > ty1) for tx1, ty1, tx2, ty2 in table_regions)
                        if overlaps:
                            continue

                        cropped_image = cv2_img[box[0][1]:box[1][1], box[0][0]:box[1][0]]
                        try:
                            cropped_image = Image.fromarray(cropped_image)
                            rec_result = detector.predict(cropped_image)
                            text = rec_result
                            a_page_output.append(((box[0][0], box[0][1], box[1][0], box[1][1]), text, 'text'))
                        except Exception as e:
                            continue

                    a_page_output.sort(key=lambda item: (item[0][1], item[0][0]))
                    final_page_output = "\n".join([item[1] for item in a_page_output])
                    results.append(final_page_output)
                except SystemExit as e:
                    print("Caught SystemExit:", e)
                    continue
                except Exception as e:
                    print(e)
                    continue
    return results