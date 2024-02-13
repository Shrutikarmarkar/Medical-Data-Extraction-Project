from backend.src.parser_generic import Medical_Parser
import re


class PrescriptionParser(Medical_Parser):
    def __init__(self, text):
        Medical_Parser.__init__(self, text)

    def parser(self):
        return {
            "Patient's Name: ": self.get_fields("Patient Name"),
            "Address: ": self.get_fields("Address"),
            "Medicines: ": self.get_fields("Medicines"),
            "Directions: ": self.get_fields("Directions"),
            "Refill: ": self.get_fields("Refill")
        }

    def get_fields(self, field_name):
        pattern_dict = {
            "Patient Name": {"pattern": "Name:(.*)Date", "flag": 0},
            "Address": {"pattern": "Address:(.*)\n", "flag": 0},
            "Medicines": {"pattern": "Address:[^\n]*(.*)Directions", "flag": re.DOTALL},
            "Directions": {"pattern": "Directions:(.*)Refill", "flag": re.DOTALL},
            "Refill": {"pattern": "Refill: (.*)times", "flag": 0}
        }
        field = pattern_dict.get(field_name)
        pattern = field.get("pattern")
        matches = re.findall(pattern, self.text, flags=field.get("flag"))
        if len(matches) > 0:
            return matches[0].strip()


if __name__ == "__main__":
    doc_text = '''
    Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    results = PrescriptionParser(doc_text)
    print(results.parser())
