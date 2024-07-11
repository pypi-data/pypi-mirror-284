import os
import fitz

from .botrun_ask_folder_logger import BotrunAskFolderLogger
from .fast_api.util.pdf_util import pdf_page_to_image, DEFAULT_DPI, process_pdf_page


def run_pdf_to_img(google_drive_folder_id: str, force: bool = False):
    """
    Convert all PDF pages in the specified Google Drive folder to images.

    :param google_drive_folder_id: Google Drive folder ID containing the PDFs.
    :param force: If True, re-download and re-process all PDFs.
    """
    BotrunAskFolderLogger().get_logger().debug(f"Running PDF to image conversion for Google Drive folder ID {google_drive_folder_id}")
    data_folder = f"./data/{google_drive_folder_id}"
    metadata_file = os.path.join(data_folder, f"{google_drive_folder_id}-metadata.json")
    BotrunAskFolderLogger().get_logger().debug(f"Data folder: {data_folder}")
    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"Data folder for Google Drive folder ID {google_drive_folder_id} does not exist.")
    if not os.path.exists(metadata_file):
        raise FileNotFoundError(f"Metadata file for Google Drive folder ID {google_drive_folder_id} does not exist.")

    import json
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)
        metadata = {item['name']: item['id'] for item in metadata.get('items', [])}

    output_folder = "./users/botrun_ask_folder/img"
    os.makedirs(output_folder, exist_ok=True)
    dpi = DEFAULT_DPI
    scale = 1.0
    color = True
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                # pdf_name = os.path.splitext(file)[0]
                google_file_id = metadata.get(file, None)
                if not google_file_id:
                    continue

                with open(pdf_path, 'rb') as pdf_file:
                    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
                    print(f"processing {file}... with {len(pdf_document)} pages")
                    start_page = 1
                    for end_page in range(100, len(pdf_document) + 100, 100):
                        if end_page > len(pdf_document):
                            end_page = len(pdf_document)
                        print(f"processing scope: {google_file_id}, pages {start_page}-{end_page}")
                        for page_number in range(start_page, end_page + 1):
                            img_path = os.path.join(output_folder, f"{google_file_id}_{page_number}.png")
                            if not force and os.path.exists(img_path):
                                continue
                            img_byte_arr = process_pdf_page(pdf_document, page_number, dpi=dpi, scale=scale, color=color)
                            absolute_path = os.path.abspath(img_path)

                            with open(img_path, "wb") as img_file:
                                img_file.write(img_byte_arr)
                        start_page = end_page + 1
