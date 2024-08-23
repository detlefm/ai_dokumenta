from io import BytesIO
import fitz  # PyMuPDF
from PIL import Image as ImageModul
from pathlib import Path
import json
import os
from datetime import datetime


class PdfConverter():

    def __init__(self,filename:Path|str|BytesIO):
        if isinstance(filename,str) or isinstance(filename,Path):
            # Öffne die PDF-Datei mit PyMuPDF
            self.pdf_document = fitz.Document(filename)
        elif isinstance(filename,BytesIO):
            pdf_stream = BytesIO(filename.read())
            self.pdf_document = fitz.Document(stream=pdf_stream, filetype="pdf")          

    def to_images(self) -> ImageModul.Image:
        # Liste zum Speichern der Seitenbilder
        pages = []

        # Iteriere durch jede Seite der PDF und konvertiere sie in ein Bild
        for page_num in range(len(self.pdf_document)):
            page = self.pdf_document.load_page(page_num)
            pix = page.get_pixmap(dpi=300)
            img = ImageModul.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pages.append(img)

        return pages

    def to_combined_image(self,pages:list[ImageModul.Image]) -> ImageModul.Image:
        # Bestimme die Breite und Höhe des kombinierten Bildes
        total_width = max(page.width for page in pages)
        total_height = sum(page.height for page in pages)

        # Erstelle ein neues Bild mit der berechneten Größe und setze es auf weiß
        combined_image = ImageModul.new('RGB', (total_width, total_height), (255, 255, 255))

        # Füge die Seitenbilder in das kombinierte Bild ein
        y_offset = 0
        for page in pages:
            combined_image.paste(page, (0, y_offset))
            y_offset += page.height

        return combined_image
    
    def metadata(self,rm_empty:bool=True):
        d = self.pdf_document.metadata
        if rm_empty:
            for key,val in list(d.items()):
                if not val:
                    del d[key]
        return d







# def convert(filename:Path|str|BytesIO) :
#     if isinstance(filename,str) or isinstance(filename,Path):
#         # Öffne die PDF-Datei mit PyMuPDF
#         pdf_document = fitz.Document(filename)
#     elif isinstance(filename,BytesIO):
#         pdf_stream = BytesIO(filename.read())
#         pdf_document = fitz.Document(stream=pdf_stream, filetype="pdf")

#     # Liste zum Speichern der Seitenbilder
#     pages = []

#     # Iteriere durch jede Seite der PDF und konvertiere sie in ein Bild
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
#         pix = page.get_pixmap(dpi=300)
#         img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#         pages.append(img)

#     # Bestimme die Breite und Höhe des kombinierten Bildes
#     total_width = max(page.width for page in pages)
#     total_height = sum(page.height for page in pages)

#     # Erstelle ein neues Bild mit der berechneten Größe und setze es auf weiß
#     combined_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

#     # Füge die Seitenbilder in das kombinierte Bild ein
#     y_offset = 0
#     for page in pages:
#         combined_image.paste(page, (0, y_offset))
#         y_offset += page.height

#     # get meta data
#     metadata = pdf_document.metadata

#     return combined_image, metadata


def storage_data(filepath:Path|str):
    if isinstance(filepath,str):
        filepath = Path(filepath)
    if filepath.is_file() == False:
        raise AttributeError('not a file or not found')
    
    c_time_dt = datetime.fromtimestamp(filepath.stat().st_birthtime)

    # Formatieren des datetime-Objekts in einen lesbaren String
    c_time_str = c_time_dt.strftime('%d.%m.%Y %H:%M:%S')    
    return {
        'filename': str(filepath.name),
        'size': filepath.stat().st_size,
        'extension': filepath.suffix,
        'creationdate':c_time_str
    }



if __name__ == '__main__':
    import sys
    from pathlib import Path
    import json
    filename = r'.\testdata\135992631_UserManual_L6FBG51470.pdf'
    filepath = Path(filename)    
    converter = PdfConverter(filename=filepath)
    images = converter.to_images()
    no = 1
    for image in images[:5]:
        nfp = filepath.with_stem(filepath.stem+f"_{no:03d}")
        image.save(nfp.with_suffix('.jpg'))
        no += 1

    allmeta = {
        'metadata':converter.metadata(),
        'storagedata':storage_data(filepath)
        }
    filepath.with_suffix('.meta').write_text(
                json.dumps(allmeta,indent=2),
                encoding='utf-8'
            )



    # image, metadata = convert(filename)
    # image.save(filepath.with_suffix('.png'))

    # filepath.with_suffix('.meta').write_text(
    #             json.dumps(metadata,indent=2),encoding='utf-8'
    #         )


