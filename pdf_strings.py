from collections import Counter


def get_exit_string():
    return "Type of school, college or training centre:"


def raw_table_headers():
    acheived_headers = [
        "Date",
        "Body",
        "Exam",
        "Subject",
        "Grade",
        "Result",
        "Centre Number",
    ]
    predicted_headers = [
        "Date",
        "Body",
        "Exam",
        "Subject",
        "Grade",
        "Result",
        "Centre\rNumber",
        "Predicted\rGrade",
    ]
    examresults_headers = ["Date", "Body", "Exam Level", "Sitting", "Subject", "Grade"]

    return (acheived_headers, predicted_headers, examresults_headers)


def desired_tables():

    acheived_headers, predicted_headers, examresults_headers = raw_table_headers()
    achieved_counter = Counter(acheived_headers)
    predicted_counter = Counter(predicted_headers)
    examresults_counter = Counter(examresults_headers)

    return (achieved_counter, predicted_counter, examresults_counter)


def valid_exams(mapping):
    return set(mapping.keys())


def qualifications_with_overall_score():
    return {
        "France: French Baccalaureate Scientific stream",
        "World: IB - International Baccalaureate (IB) Diploma",
        "Spain: Bachillerato",
        "Romania: Diploma de Bacalaureat",
        "India: CISCE - ISC - Council for the Indian School Certificate Examination",
        "Singapore: National University of Singapore Diploma",
        "India: CBSE - AISSE - Central Board of Secondary Education Board",
        "France: OIB - Option Internationale du Baccalauréat",
        "Poland: Świadectwo dojrzalosci (Matura)",
        "Italy: Diploma di Esame di Stato",
        "Portugal: Diploma Nível Secundário de Educação",
        "Germany: Abiturprufung",
    }


def ib_permutations():
    return {
        "International Baccalaureate Diploma",
        "IB",
        "IB Standard Level",
        "Int. Baccalaureate",
        "IB Total points",
        "World: IB - International Baccalaureate (IB) Diploma"
    }


def detail_string():
    return "Module Details/Unit Grades"


def math_mapping():
    return {
        "France: French Baccalaureate Scientific stream": {
            "Mathematics Specialism",
            "Expert Mathematics","mathematics",
            "Mathematics",
        },
        "France: OIB - Option Internationale du Baccalauréat": {
            "Mathematics Major (Specialism)",
            "Mathematics Experts (Advanced)",
            "Mathematics",
        },
        "Germany: Abiturprufung": {
            "Mathematics advanced",
            "Mathematics advanced course",
            "Mathematics",
        },
        "Hong Kong: HKDSE - Hong Kong Diploma of Secondary Education": {
            "Mathematics (compulsory component)",
            "Mathematics",
        },
        "India: CBSE - AISSE - Central Board of Secondary Education Board": {
            "Mathematics",
            "MATHEMATICS",
        },
        "India: CISCE - ISC - Council for the Indian School Certificate Examination": {
            "Mathematics",
        },
        "Ireland: (Post-2017) Irish Leaving Certificate ": {
            "Mathematics",
        },
        "Italy: Diploma di Esame di Stato": {
            "Mathematics",
        },
        "Poland: Świadectwo dojrzalosci (Matura)": {
            "Mathematics - basic level",
            "Mathematics - bilingual",
            "Mathematics - extended level",
            "Mathematics Level: Basic",
            "Mathematics Level: Advanced",
        },
        "Portugal: Diploma Nível Secundário de Educação": {
            "Mathematics",
        },
        "Romania: Diploma de Bacalaureat": {
            "Mathematics"
        },
        "Singapore: A Level and SIPCAL": {
            "Mathematics"
        },
        "Singapore: National University of Singapore Diploma": {
            "Mathematics",
        },
        "Spain: Bachillerato": {
            "Mathematics",
        },
        "United Kingdom (UK): A Levels": {
            "Mathematics",
            "Mathematics (MEI)",
            "Mathematics A",
        },
        "United Kingdom (UK): Scotland Advanced Highers": {
            "Mathematics C847",
            "Mathematics",
        },
        "United Kingdom (UK): Cambridge Pre-U": {
            "Mathematics (principal subject)",
            "Mathematics",
        },
        "United States of America (USA): Advanced Placements (AP)": {
            "AP Calculus BC",
            "AP Calculus\rBC",
            "CALCULUS BC",
        },
        "World: IB - International Baccalaureate (IB) Diploma": {
            "Math Analysis & Appr",
            "Mathematics",
            "Mathematics Analysis",
            "Mathematics: Analysis and Approaches",
        },
    }


def fm_mapping():
    return {
        "Hong Kong: HKDSE - Hong Kong Diploma of Secondary Education": {
            "Calculus & Statistics",
            "Calculus & Algebra",
        },
        "Singapore: A Level and SIPCAL": {
            "Further Mathematics"
        },
        "United Kingdom (UK): A Levels": {
            "Further Mathematics (MEI)",
            "Further Mathematics"
        },
        "United Kingdom (UK): Scotland Advanced Highers": {
            "Mathematics of Mechanics C802",
            "Mathematics of Mechanics",
        },
        "United Kingdom (UK): Cambridge Pre-U": {
            "Further Mathematics (principal subject)",
            "FUrther Mathematics",
        },
    }


def physics_mapping():
    return {
        "France: French Baccalaureate Scientific stream": {
            "physics",
            "Physics",
            "Physics-Chemistry Specialism",
            "Expert Mathematics",
        },
        "France: OIB - Option Internationale du Baccalauréat": {
            "Physics Chemistry Major (Specialism)",
            "Physics and chemistry",
            "Physics & chemistry",
            "Physics & Chemistry",
        },
        "Germany: Abiturprufung": {
            "Physics advanced course",
            "Physics",
            "Physics advanced",
        },
        "Hong Kong: HKDSE - Hong Kong Diploma of Secondary Education": {
            "Physics",
        },
        "India: CBSE - AISSE - Central Board of Secondary Education Board": {
            "Physics",
            "PHYSICS",
        },
        "India: CISCE - ISC - Council for the Indian School Certificate Examination": {
            "Physics",
        },
        "Ireland: (Post-2017) Irish Leaving Certificate ": {
            "Physics",
        },
        "Italy: Diploma di Esame di Stato": {
            "Physics",
        },
        "Poland: Świadectwo dojrzalosci (Matura)": {
            "Physics",
            "Physics - bilingual",
            "Physics Level: Advanced",
        },
        "Portugal: Diploma Nível Secundário de Educação": {
            "Physics",
        },
        "Romania: Diploma de Bacalaureat": {
            "Physics",
        },
        "Singapore: A Level and SIPCAL": {
            "Physics",
        },
        "Singapore: National University of Singapore Diploma": {
            "Physics",
        },
        "Spain: Bachillerato": {
            "Physics and Chemistry",
            "Physics",
        },
        "United Kingdom (UK): A Levels": {
            "Physics A",
            "Physics"
        },
        "United Kingdom (UK): Scotland Advanced Highers": {
            "Physics C857",
            "Physics"
        },
        "United Kingdom (UK): Cambridge Pre-U": {
            "Physics (principal subject)",
            "Physics",
        },
        "United States of America (USA): Advanced Placements (AP)": {
            "AP Physics C: Electricity and Magnetism",
            "AP Physics C: Mechanics",
            "AP Physics 1",
            "AP Physics C ELECTRICITY AND MAGNETISM",
            "AP Physics C MECHANICS",
        },
        "World: IB - International Baccalaureate (IB) Diploma": {
            "Physics"
        },
    }
