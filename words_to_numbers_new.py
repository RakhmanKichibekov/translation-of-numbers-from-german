num_dict = {
    "null": 0,
    "ein": 1,
    "eins": 1,
    "zwei": 2,
    "drei": 3,
    "vier": 4,
    "fünf": 5,
    "sechs": 6,
    "sieben": 7,
    "acht": 8,
    "neun": 9,
    "zehn": 10,
    "elf": 11,
    "zwölf": 12,
    "dreizehn": 13,
    "vierzehn": 14,
    "fünfzehn": 15,
    "sechzehn": 16,
    "siebzehn": 17,
    "achtzehn": 18,
    "neunzehn": 19,
    "zwanzig": 20,
    "dreißig": 30,
    "vierzig": 40,
    "fünfzig": 50,
    "sechzig": 60,
    "siebzig": 70,
    "achtzig": 80,
    "neunzig": 90,
    "hundert": 100,
    "einhundert": 100,
    "tausend": 1000,
    "eintausend": 1000
}


# main function
def convert_to_num(string):
    string_list = string.lower().strip().split()
    num_list = []
    if not string_list:
        return 'Ничего не введено или введены одни только пробелы'

    for element in string_list:
        if not ((element in num_dict.keys()) or (element == 'und')):
            return 'Слово - ' + element + ' не найдено'
        if element == 'und':
            num_list.append('und')
        else:
            num_list.append(num_dict[element])

    # expected_length = 2
    def find_from_2(num_list, string_list):
        if num_list[0] in list(range(2,10)):
            if num_list[1] == 100:
                return num_list[0]*100
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + string_list[0] + ' идёт ' + ' '.join(string_list[1:])
        elif num_list[0] == 100:
            if (num_list[1] in (list(range(1,20)) + list(range(20,100,10)))) and (string_list[1] != 'ein'):
                return 100 + num_list[1]
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + string_list[0] + ' идёт ' + ' '.join(string_list[1:])
        else:
            return 'Нет числа длиной ' + str(len(num_list)) + ' которое начианется с ' + string_list[0]

    # expected_length = 3
    def find_from_3(num_list, string_list):
        if (num_list[0] in list(range(1,10))) and (string_list[0] != 'eins'):
            if num_list[1] == 'und':
                if num_list[2] in list(range(20,100,10)):
                    return num_list[0] + num_list[2]
                else:
                    return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(string_list[:2]) + ' идёт ' + ' '.join(string_list[2:])
            elif num_list[1] == 100:
                if string_list[0] == 'ein':
                    return 'Нет числа длиной ' + str(len(num_list)) + ', где после ein идёт hundert'
                if (num_list[2] in (list(range(1,20)) + list(range(20,100,10)))) and (string_list[2] != 'ein'):
                    return num_list[0]*100+num_list[2]
                return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(string_list[:2]) + ' идёт ' + ' '.join(string_list[2:])
            else:
                return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(string_list[:1]) + ' идёт ' + ' '.join(string_list[1:])
        else:
            return 'Нет числа длиной ' + str(len(num_list)) + ', которое начинается с ' + string_list[0]

    # expected_length = 4
    def find_from_4(num_list, string_list):
        if num_list[0] == 100:
            if (num_list[1] in list(range(1,10))) and (string_list[1] != 'eins'):
                if num_list[2] == 'und':
                    if num_list[3] in list(range(20,100,10)):
                        return 100 + num_list[1] + num_list[3]
                    else:
                        return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                            string_list[:3]) + ' идёт ' + ' '.join(string_list[3:])
                else:
                    return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                        string_list[:2]) + ' идёт ' + ' '.join(string_list[2:])
            else:
                return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                    string_list[:1]) + ' идёт ' + ' '.join(string_list[1:])
        else:
            return 'Нет числа длиной ' + str(len(num_list)) + ', которое начинается с ' + string_list[0]

    # expected_length = 5
    def find_from_5(num_list, string_list):
        if num_list[0] in list(range(2,10)):
            if num_list[1] == 100:
                if (num_list[2] in list(range(1, 10))) and (string_list[2] != 'eins'):
                    if num_list[3] == 'und':
                        if num_list[4] in list(range(20, 100, 10)):
                            return num_list[0]*100 + num_list[2] + num_list[4]
                        else:
                            return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                                string_list[:4]) + ' идёт ' + ' '.join(string_list[4:])
                    else:
                        return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                            string_list[:3]) + ' идёт ' + ' '.join(string_list[3:])
                else:
                    return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                        string_list[:2]) + ' идёт ' + ' '.join(string_list[2:])
            else:
                return 'Нет числа длиной ' + str(len(num_list)) + ', где после ' + ' '.join(
                    string_list[:1]) + ' идёт ' + ' '.join(string_list[1:])
        else:
            return 'Нет числа длиной ' + str(len(num_list)) + ', которое начинается с ' + string_list[0]

    if len(num_list) == 1:
        if string_list[0] not in ['ein', 'und']:
            return num_list[0]
        else:
            return 'Число не может начинаться с слова - ' + string_list[0]

    if ((string_list[0] == 'ein') and (string_list[1] in ['hundert', 'tausend'])) and (len(num_list) == 2):
        return num_dict[string_list[0] + string_list[1]]

    # print(len(num_list))
    if len(num_list) == 2:
        return find_from_2(num_list, string_list)
    if len(num_list) == 3:
        if isinstance(find_from_3(num_list, string_list), int):
            return find_from_3(num_list, string_list)
        elif isinstance(find_from_2(num_list[:2], string_list[:2]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:2]) + ' (=' + str(find_from_2(num_list[:2], string_list[:2])) + ') идёт ' + ' '.join(
                string_list[2:])
        return find_from_3(num_list, string_list)
    if len(num_list) == 4:
        if isinstance(find_from_4(num_list, string_list), int):
            return find_from_4(num_list, string_list)
        if isinstance(find_from_3(num_list[:3], string_list[:3]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:3]) + ' (=' + str(find_from_3(num_list[:3], string_list[:3])) + ') идёт ' + ' '.join(
                string_list[3:])
        if isinstance(find_from_2(num_list[:2], string_list[:2]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:2]) + ' (=' + str(find_from_2(num_list[:2], string_list[:2])) + ') идёт ' + ' '.join(
                string_list[2:])
        return find_from_4(num_list, string_list)
    if len(num_list) == 5:
        if isinstance(find_from_5(num_list[:5], string_list[:5]), int):
            return find_from_5(num_list, string_list)
        if isinstance(find_from_4(num_list[:4], string_list[:4]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:4]) + ' (=' + str(find_from_4(num_list[:4], string_list[:4])) + ') идёт ' + ' '.join(
                string_list[4:])
        if isinstance(find_from_3(num_list[:3], string_list[:3]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:3]) + ' (=' + str(find_from_3(num_list[:3], string_list[:3])) + ') идёт ' + ' '.join(
                string_list[3:])
        if isinstance(find_from_2(num_list[:2], string_list[:2]), int):
            return 'Нет числа длиной ' + str(len(num_list)) + ', где после числа ' + ' '.join(
                string_list[:2]) + ' (=' + str(find_from_2(num_list[:2], string_list[:2])) + ') идёт ' + ' '.join(
                string_list[2:])
        return find_from_5(num_list, string_list)


    if isinstance(find_from_5(num_list[:5], string_list[:5]), int):
        return 'Не существует чисел длиной ' + str(len(num_list)) + ', после числа ' + ' '.join(
                        string_list[:5]) + ' (=' + str(find_from_5(num_list[:5], string_list[:5])) + ') идёт ' + ' '.join(string_list[5:])
    if isinstance(find_from_4(num_list[:4], string_list[:4]), int):
        return 'Не существует чисел длиной ' + str(len(num_list)) + ', после числа ' + ' '.join(
            string_list[:4]) + ' (=' + str(find_from_4(num_list[:4], string_list[:4])) + ') идёт ' + ' '.join(string_list[4:])
    if isinstance(find_from_3(num_list[:3], string_list[:3]), int):
        return 'Не существует чисел длиной ' + str(len(num_list)) + ', после числа ' + ' '.join(
            string_list[:3]) + ' (=' + str(find_from_3(num_list[:3], string_list[:3])) + ') идёт ' + ' '.join(string_list[3:])
    if isinstance(find_from_2(num_list[:2], string_list[:2]), int):
        return 'Не существует чисел длиной ' + str(len(num_list)) + ', после числа ' + ' '.join(
            string_list[:2]) + ' (=' + str(find_from_2(num_list[:2], string_list[:2])) + ') идёт ' + ' '.join(string_list[2:])
    return 'Не существует чисел длиной ' + str(len(num_list)) + ', а из первых слов невозможно составить число'

# print(convert_to_num('  	zwei   hundert   acht  '))
