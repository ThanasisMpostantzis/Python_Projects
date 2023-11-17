import requests

baseurl = "https://hr.apografi.gov.gr/api/public/"

un1 = 'ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'
un2 = 'ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'
un3 = 'ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'


def main_request(baseurl, endpoint):
    try:
        r = requests.get(baseurl + endpoint)
        r.raise_for_status()  # Ελέγχει αν υπάρχει σφάλμα στο αίτημα
        return r.json()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Error:",err)
    return None


def find_org_code(uniName):
    endpoint = 'organizations'
    data = main_request(baseurl, endpoint)
    code = ""
    for i in range(len(data['data'])):
        if data['data'][i]['preferredLabel'] == uniName:
            code = data['data'][i]['code']
    return code


def get_org_position_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    return len(data['data'])


def get_type_info(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    oragnic, temporary= 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023' and data['data'][i]['type'] == 'Organic':
                oragnic +=1
            elif str(date)[:4] == '2023' and data['data'][i]['type'] == 'Temporary':
                temporary += 1

    return "Organic: " + str(oragnic) + "\n" + "Temporary: " + str(temporary)

def get_employmentType_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    empType1, empType3,empType10 = 0, 0, 0
    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i] and 'employmentType' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023':
                match data['data'][i]['employmentType']:
                    case 1:
                        empType1 += 1
                    case 3:
                        empType3 += 1
                    case 10:
                        empType10 += 1
    return "ΜOΝΙΜΟΙ ΥΠAΛΛΗΛΟΙ ΤΟΥ ΔΗΜΟΣIΟΥ /ΔΙΚΑΣΤΙΚΟI ΛΕΙΤΟΥΡΓΟI /ΔΗΜOΣΙΟΙ ΛΕΙΤΟΥΡΓΟI (employmentType 1): " + str(empType1) + "\n" + "ΙΔΙΩΤΙΚΟΥ ΔΙΚΑΙΟΥ ΑΟΡΙΣΤΟΥ ΧΡΟΝΟΥ(employmentType 3): " + str(empType3) + "\n" + "ΕΜΜΙΣΘΗ ΕΝΤΟΛΗ(employmentType 10): " + str(empType10)

def get_educationType_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    eduType1, eduType2, eduType3, eduType4, eduType5, eduType6, eduType7 = 0, 0, 0, 0, 0, 0, 0
    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i] and 'employmentType' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023':
                match data['data'][i]['educationType']:
                    case 1:
                        eduType1 += 1
                    case 2:
                        eduType2 += 1
                    case 3:
                        eduType3 += 1
                    case 4:
                        eduType4 += 1
                    case 5:
                        eduType5 += 1
                    case 6:
                        eduType6 += 1
                    case 7:
                        eduType7 += 1
    return "ΑΝΕΥ ΚΑΤΗΓΟΡΙΑΣ ΕΚΠ/ΣΗΣ: " + str(eduType1) + "\n" + "ΠΕ: " + str(eduType2) + "\n" + "ΤΕ: " + str(eduType3) + "\n" + "ΔΕ: " + str(eduType4) + "\n" + "ΥΕ: " + str(eduType5) + "\n" + "ΕΙΔΙΚΩΝ ΘΕΣΕΩΝ: " + str(eduType6) + "\n" + "ΕΕΠ: " + str(eduType7)

def get_departments(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    departments_count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,
                         '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                         '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}

    for i in range(len(data['data'])):
        if 'jobDescriptionVersion' in data['data'][i]:
            version = str(data['data'][i]['jobDescriptionVersion'])
            if version[:10] in departments_count:
                departments_count[version[:10]] += 1

    return departments_count


def get_organizational_units(orgcode):
    units = []
    endpoint = "organizational-units?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    for i in range(len(data['data'])):
        units.append(data['data'][i]['preferredLabel'])
    return units


def diakimansi_taktikou_prosopikou(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    posnum2019, posnum2020, posnum2021, posnum2022, posnum2023 = 0, 0, 0, 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2019' and data['data'][i]['type'] == 'Organic':
                posnum2019 += 1
            elif str(date)[:4] == '2020' and data['data'][i]['type'] == 'Organic':
                posnum2020 += 1
            elif str(date)[:4] == '2021' and data['data'][i]['type'] == 'Organic':
                posnum2021 += 1
            elif str(date)[:4] == '2022' and data['data'][i]['type'] == 'Organic':
                posnum2022 += 1
            elif str(date)[:4] == '2023' and data['data'][i]['type'] == 'Organic':
                posnum2023 += 1

    return '2019: {}\n2020: {}\n2021: {}\n2022: {}\n2023: {}'.format(
        posnum2019, posnum2019 + posnum2020, posnum2019 + posnum2020 + posnum2021,
        posnum2019 + posnum2020 + posnum2021 + posnum2022,
        posnum2019 + posnum2020 + posnum2021 + posnum2022 + posnum2023)


def diakimansi_proslipsewn_prosopikou(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    posnum2019, posnum2020, posnum2021, posnum2022, posnum2023 = 0, 0, 0, 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2019':
                posnum2019 += 1
            elif str(date)[:4] == '2020':
                posnum2020 += 1
            elif str(date)[:4] == '2021':
                posnum2021 += 1
            elif str(date)[:4] == '2022':
                posnum2022 += 1
            elif str(date)[:4] == '2023':
                posnum2023 += 1

    return '2019: {}\n2020: {}\n2021: {}\n2022: {}\n2023: {}'.format(
        posnum2019, posnum2020, posnum2021, posnum2022, posnum2023)


def change_theme_event():
    print('--------------------------------------------------------------------------------------')


def find_code():
    print(f"1. Κωδικός {un1}: {find_org_code(un1)}")
    print(f"1. Κωδικός {un2}: {find_org_code(un2)}")
    print(f"1. Κωδικός {un3}: {find_org_code(un3)}")


def staff_variation():
    print('2. Διακύμανση τακτικού προσωπικού (ανά χρόνο) ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: \n' + diakimansi_taktikou_prosopikou(
        find_org_code(un1)))
    print(
        '2. Διακύμανση τακτικού προσωπικού (ανά χρόνο) ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: \n' + diakimansi_taktikou_prosopikou(
            find_org_code(un2)))
    print('2. Διακύμανση τακτικού προσωπικού (ανά χρόνο) ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: \n' + diakimansi_taktikou_prosopikou(
        find_org_code(un3)))


def annual_retreatments():
    print('3. Διακύμανση ετήσιων προσλήψεων ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: \n' +
          diakimansi_proslipsewn_prosopikou(find_org_code(un1)))
    print(
        '3. Διακύμανση ετήσιων προσλήψεων ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: \n' +
        diakimansi_proslipsewn_prosopikou(find_org_code(un2)))
    print('3. Διακύμανση ετήσιων προσλήψεων ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: \n' +
          diakimansi_proslipsewn_prosopikou(find_org_code(un3)))


def uni_num_job_pos():
    print("4. Θέσεις του Πανεπιστημίου Πατρών για το έτος 2023 σύμφωνα με συγκεκριμένα κριτήρια (τύπος θέσης, εργασιακή σχέση, κατηγορία εκπαίδευσης, κλάδος) \n")
    print("4. Τύποι θέσης: \n" + get_type_info(find_org_code(un3)) + "\n")
    print("4. Eργασιακή σχέση: \n" + get_employmentType_num(find_org_code(un3)) + "\n")
    print("4. Κατηγορία εκπαίδευσης: \n" + get_educationType_num(find_org_code(un3)) + "\n")
    print("4. Κλάδοι ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_departments(find_org_code(un3)))+ "\n")



def org_units():
    print("5. UNITS ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + str(get_organizational_units(find_org_code(un1))))
    print("5. UNITS ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + str(get_organizational_units(find_org_code(un2))))
    print("5. UNITS ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_organizational_units(find_org_code(un3))))


# 1
find_code()
change_theme_event()

# 2
staff_variation()
change_theme_event()

# 3
annual_retreatments()
change_theme_event()

# 4
uni_num_job_pos()
change_theme_event()

# 5
org_units()
change_theme_event()
