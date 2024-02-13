from Patient_details_parser import PatientDetailsParser
import pytest


@pytest.fixture()
def doc_1():
    document = '''
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
    return PatientDetailsParser(document)


@pytest.fixture()
def doc_2():
    document = '''
    17/12/2020

Patient Medical Record

Patient Information Birth Date
Jerry Lucas May 2 1998
(279) 920-8204 " Weight:
4218 Wheeler Ridge Dr 57

are ieee, 14201 Height:

In Case of Emergency |
eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: .

IMMUNE NOT IMMUNE
Have you had the Hepatitis B vaccination?
“Yes | |

List any Medical Problems (asthma, seizures, headaches):
N/A

a CS
NN TOC

Name of Insurance Company:

Random Insuarance Company 4218 Smeeler Ridge Dr
ote Number sage
5638746258

Expiry Date:

31 December 2020
Do you have medical insurance?

Yes

Medical Insurance Details

List any allergies:

N/A

List any medication taken regularly:
N/A

iat. Tae

    '''
    return PatientDetailsParser(document)


@pytest.fixture()
def doc_empty():
    return PatientDetailsParser("")


def test_get_patient_name(doc_1, doc_2, doc_empty):
    assert doc_1.get_name() == "Kathy Crawford"
    assert doc_2.get_name() == "Jerry Lucas"
    assert doc_empty.get_name() is None


def test_get_number(doc_1, doc_2, doc_empty):
    assert doc_1.get_number() == "(737) 988-0851"
    assert doc_2.get_number() == "(279) 920-8204"
    assert doc_empty.get_number() is None


def test_get_vaccine(doc_1, doc_2, doc_empty):
    assert doc_1.get_vaccine() == "No"
    assert doc_2.get_vaccine() == "Yes"
    assert doc_empty.get_vaccine() is None


def test_get_problems(doc_1, doc_2, doc_empty):
    assert doc_1.get_problem() == "Migraine"
    assert doc_2.get_problem() == "N/A"
    assert doc_empty.get_problem() is None


def test_parser(doc_1, doc_2, doc_empty):
    record_1 = doc_1.parser()
    assert record_1 == {'Patient Name': 'Kathy Crawford',
                        'Phone Number': '(737) 988-0851',
                        'Hepatitis B vaccination?': "No",
                        'Medical Problems': 'Migraine'
                        }

    record_2 = doc_2.parser()
    assert record_2 == {'Patient Name': "Jerry Lucas",
                        'Phone Number': "(279) 920-8204",
                        'Hepatitis B vaccination?': "Yes",
                        'Medical Problems': "N/A"
                        }

    record_empty = doc_empty.parser()
    assert record_empty == {'Patient Name': None,
                            'Phone Number': None,
                            'Hepatitis B vaccination?': None,
                            'Medical Problems': None}
