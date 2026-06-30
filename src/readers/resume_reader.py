from pathlib import Path

import pdfplumber


class ResumeReader:
    """
    Reads resume PDF and returns plain text.
    """

    def read(self, file_path: str | Path) -> str:

        pages = []

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    pages.append(text)

        return "\n".join(pages)