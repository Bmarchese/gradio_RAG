import pymupdf4llm
import pymupdf
import pypandoc


class TextExtraction:
    @staticmethod
    def extract_pdf(file):
        doc = pymupdf.open(file)
        markdown = pymupdf4llm.to_markdown(doc)
        return markdown

    @staticmethod
    def extract_docx(file):
        extra_args = [
            '--wrap=none',  # evita quebra automática de linhas
        ]

        markdown = pypandoc.convert_file(
            file,
            to='gfm',
            # to='markdown-simple_tables-multiline_tables+pipe_tables',
            format='docx',
            extra_args=extra_args
        )
        return markdown

    @staticmethod
    def extract_txt(file):
        with open(file) as text:
            return text.read()
