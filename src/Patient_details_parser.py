from backend.src.parser_generic import Medical_Parser
import re


class PatientDetailsParser(Medical_Parser):
    def __init__(self, text2):
        Medical_Parser.__init__(self, text2)

    def parser(self):
        return {
            "Patient Name": self.get_name(),
            "Phone Number": self.get_number(),
            "Hepatitis B vaccination?": self.get_vaccine(),
            "Medical Problems": self.get_problem()
        }

    def get_field(self, field_name):
        pattern_dict = {
            "Patient Name": {"pattern": "Date(.*?) [a-zA-Z]+ \d", "flag": re.DOTALL},
            "Phone No": {"pattern": "\(\d{3}\) \d{3}-\d{4}", "flag": 0},
            "Vaccine Taken?": {"pattern": "vaccination\?(?:[\s\S]*?)(Yes|No)", "flag": re.DOTALL},
            "Problems": {"pattern": "\(asthma, seizures, headaches\):\s*([^\n]+)", "flag": re.DOTALL},
        }
        field_details = pattern_dict.get(field_name)
        match = re.findall(field_details.get("pattern"), self.text, flags=field_details.get("flag"))
        if len(match) > 0:
            return match[0].strip()

    def get_name(self):
        pattern = "Date(.*?) [a-zA-Z]+ \d"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()

    def get_number(self):
        pattern = "\(\d{3}\) \d{3}-\d{4}"
        match = re.findall(pattern, self.text, flags=0)
        if len(match) > 0:
            return match[0].strip()

    def get_vaccine(self):
        pattern = "vaccination\?(?:[\s\S]*?)(Yes|No)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()

    def get_problem(self):
        pattern = "Medical Problems .*?:\s*([^\n]+)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()


if __name__ == "__main__":
    text = '''
   17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 :

United States Height:
190

In Case of Emergency :
ee __.
Simeone Crawford 9266 Ash Dr
H New York City, New York, 10005
ome phone United States
(990) 375-4621
Work phone
Genera! Medical History
a

eh ee A AS ne

ene

nr enna

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine

e Name of Insurance Company:
Random Insuarance Company

F . policy Number:
7115207313
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:
Peanuts

List any medication taken regularly:

Triptans

4789 Bollinger Rd
Jersey City, New Jersey, 07030

Expiry Date:
30 December 2020
    '''
    results = PatientDetailsParser(text)
    print(results.parser())
