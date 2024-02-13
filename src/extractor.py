from pdf2image import convert_from_path
import pytesseract
import util
from Prescription_parser import PrescriptionParser
from Patient_details_parser import PatientDetailsParser

POPPLER_PATH = r"C:\medical-project\installations\poppler-23.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\medical-project\installations\Tesseract-OCR\tesseract.exe"


def extract(file_path, file_format):
    extracted_text = ""
    pages = convert_from_path(file_path,
                              poppler_path=POPPLER_PATH)
    for page in pages:
        new_image = util.pre_process_image(page)
        text = pytesseract.image_to_string(new_image, lang='eng')
        extracted_text += "\n" + text

    if file_format == 'prescription':
        extracted_text = PrescriptionParser(extracted_text).parser()
    elif file_format == 'patient_details':
        extracted_text = PatientDetailsParser(extracted_text).parser()
    else:
        raise Exception(f"Invalid document format {file_format}")

    return extracted_text


if __name__ == "__main__":
    data = extract(r"../resources/patient_details/pd_2.pdf", "prescription")
    print(data)
