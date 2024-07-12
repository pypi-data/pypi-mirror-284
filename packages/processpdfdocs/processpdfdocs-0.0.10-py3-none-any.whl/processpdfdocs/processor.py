import os
from .utils import is_text_selectable, ocr_pdf_to_text_and_html, extract_table_from_pdf
from .download_models import download_models

class Processor:
    def __init__(self, model_dir='~/.processpdfdocs/models'):
        self.model_dir = os.path.expanduser(model_dir)

        self._check_and_download_models()

    def _check_and_download_models(self):
        required_models = ['rotation_model.onnx', 'table_detect_model.pt', 'cell_detect_model.pt']
        for model in required_models:
            if not os.path.exists(os.path.join(self.model_dir, model)):
                print(f"Model {model} not found. Downloading...")
                download_models(self.model_dir)
                break

    def process_pdf(self, pdf_path):
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")
        
        if not pdf_path.lower().endswith('.pdf'):
            raise ValueError("The provided file is not a PDF.")
        
        if not is_text_selectable(pdf_path):
            extracted_text = ocr_pdf_to_text_and_html(pdf_path)
            texts = "\n".join(extracted_text)
        else:
            extracted_text = extract_table_from_pdf(pdf_path)
            texts = "\n".join(extracted_text)

        return texts
