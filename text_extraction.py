import docx2txt
import pymupdf

class TextExtraction:
    @staticmethod
    def extract_pdf(file):
        doc = pymupdf.open(file)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    @staticmethod
    def extract_docx(file):
        text = docx2txt.process(file)
        return text

    @staticmethod
    def extract_txt(file):
        with open(file) as text:
            return text.read()
