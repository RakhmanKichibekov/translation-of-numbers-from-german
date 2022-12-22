num_dict = {
    "null": 0,
    "eins": 1,
    "ein": 1,
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
    if not string_list:
        return 'Ничего не введено или введены одни только пробелы'

    for element in string_list:
        if not ((element in num_dict.keys()) or (element == 'und')):
            return 'Ошибка в слове - ' + element

    if len(string_list) == 1:
        if string_list[0] == 'ein':
            return 'Нет числа - ein, возможно вы имели в виду - eins ?'
        if string_list[0] == 'und':
            return 'Введена только связь "und"'
        return num_dict[string_list[0]]

    if string_list[0] == 'eins':
        if string_list[1] in list(num_dict.keys())[:11]:
            return 'После числа eins ожидался конец строки\nВстречено число ' + string_list[1] + ', являющееся числом единиц'
        if string_list[1] in list(num_dict.keys())[11:21]:
            return 'После числа eins ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом формата 11 - 19'
        if string_list[1] in list(num_dict.keys())[21:-4]:
            return 'После числа eins ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом десятков'
        if string_list[1] in list(num_dict.keys())[-4:-2]:
            return 'После числа eins ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся сотней'
        if string_list[1] in list(num_dict.keys())[-2:]:
            return 'После числа eins ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся тысячей'
        return 'После числа eins ожидался конец строки\nВстречено und'

    if string_list[0] == 'null':
        if string_list[1] in list(num_dict.keys())[:11]:
            return 'После числа null ожидался конец строки\nВстречено число ' + string_list[1] + ', являющееся числом единиц'
        if string_list[1] in list(num_dict.keys())[11:21]:
            return 'После числа null ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом формата 11 - 19'
        if string_list[1] in list(num_dict.keys())[21:-4]:
            return 'После числа null ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом десятков'
        if string_list[1] in list(num_dict.keys())[-4:-2]:
            return 'После числа null ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся сотней'
        if string_list[1] in list(num_dict.keys())[-2:]:
            return 'После числа null ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся тысячей'
        return 'После числа null ожидался конец строки\nВстречено und'

    if num_dict[string_list[0]] == 1000:
        return 'После числа ' + string_list[0] + ' не может идти ' + ' '.join(string_list[1:]) + '\nЧисла больше 1000 не обрабатываются'

    if string_list[0] in list(num_dict.keys())[11:-4]:
        if string_list[1] in list(num_dict.keys())[:11]:
            return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено число ' + string_list[1] + ', являющееся числом единиц'
        if string_list[1] in list(num_dict.keys())[11:21]:
            return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом формата 11 - 19'
        if string_list[1] in list(num_dict.keys())[21:-4]:
            return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся числом десятков'
        if string_list[1] in list(num_dict.keys())[-4:-2]:
            return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся сотней'
        if string_list[1] in list(num_dict.keys())[-2:]:
            return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено число ' + string_list[1] + ' , являющееся тысячей'
        return 'После числа ' + string_list[0] + ' ожидался конец строки\nВстречено und'

    if string_list[0] in list(num_dict.keys())[2:11]:
        if (string_list[0] == 'ein') and (string_list[1] == 'tausend'):
            if len(string_list) == 2:
                return 1000
            return 'После числа ' + ' '.join(string_list[:2]) + ' не может идти ' + ' '.join(string_list[2:]) + '\nЧисла больше 1000 не обрабатываются'
        if string_list[1] == 'und':
            if len(string_list) > 2:
                if string_list[2] in list(num_dict.keys())[21:-4]:
                    if len(string_list) == 3:
                        return num_dict[string_list[2]] + num_dict[string_list[0]]
                    if string_list[3] in list(num_dict.keys())[11:-4]:
                        if string_list[3] in list(num_dict.keys())[:11]:
                            return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                                   string_list[3] + ', являющееся числом единиц'
                        if string_list[3] in list(num_dict.keys())[11:21]:
                            return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                                   string_list[3] + ' , являющееся числом формата 11 - 19'
                        if string_list[3] in list(num_dict.keys())[21:-4]:
                            return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                                   string_list[3] + ' , являющееся числом десятков'
                        if string_list[3] in list(num_dict.keys())[-4:-2]:
                            return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                                   string_list[3] + ' , являющееся сотней'
                        if string_list[3] in list(num_dict.keys())[-2:]:
                            return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                                   string_list[3] + ' , являющееся тысячей'
                        return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено und'

                if string_list[2] in list(num_dict.keys())[:11]:
                    return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                        2] + ' , являющееся числом единиц'
                if string_list[2] in list(num_dict.keys())[11:21]:
                    return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                        2] + ' , являющееся числом формата 11 - 19'
                if string_list[2] in list(num_dict.keys())[-4:-2]:
                    return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                        2] + ' , являющееся сотней'
                if string_list[2] in list(num_dict.keys())[-2:]:
                    return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                        2] + ' , являющееся тысячей'
                return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число десятков' + '\nВстречено und'
            return 'После ' + ' '.join(string_list[:]) + ' ожидалось еще число десятков\nВстречен конец строки'
        if string_list[1] == 'hundert':
            if len(string_list) == 2:
                return num_dict[string_list[0]] * 100
            if string_list[2] in list(num_dict.keys())[11:-4]:
                if len(string_list) == 3:
                    return num_dict[string_list[0]] * 100 + num_dict[string_list[2]]
                if string_list[3] in list(num_dict.keys())[:11]:
                    return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                           string_list[3] + ', являющееся числом единиц'
                if string_list[3] in list(num_dict.keys())[11:21]:
                    return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                           string_list[3] + ' , являющееся числом формата 11 - 19'
                if string_list[3] in list(num_dict.keys())[21:-4]:
                    return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                           string_list[3] + ' , являющееся числом десятков'
                if string_list[3] in list(num_dict.keys())[-4:-2]:
                    return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                           string_list[3] + ' , являющееся сотней'
                if string_list[3] in list(num_dict.keys())[-2:]:
                    return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено число ' + \
                           string_list[3] + ' , являющееся тысячей'
                return 'После числа ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено und'

            if string_list[2] in list(num_dict.keys())[1:11]:
                if len(string_list) == 3:
                    if string_list[2] == 'ein':
                        return 'После ' + ' '.join(string_list[:]) + ' не может идти конец строки\nОжидалось: und и число десятков'
                    return num_dict[string_list[0]] * 100 + num_dict[string_list[2]]
                if string_list[2] == 'eins':
                    if string_list[3] in list(num_dict.keys())[:11]:
                        return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                            3] + ' , являющееся числом единиц'
                    if string_list[3] in list(num_dict.keys())[11:21]:
                        return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                            3] + ' , являющееся числом формата 11 - 19'
                    if string_list[3] in list(num_dict.keys())[21:-4]:
                        return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                            3] + ' , являющееся числом десятков'
                    if string_list[3] in list(num_dict.keys())[-4:-2]:
                        return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                            3] + ' , являющееся сотней'
                    if string_list[3] in list(num_dict.keys())[-2:]:
                        return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                3] + ' , являющееся тысячей'
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидался конец строки\nВстречено und'
                if string_list[3] == 'und':

                    if len(string_list) > 4:
                        if string_list[4] in list(num_dict.keys())[21:-4]:
                            if len(string_list) == 5:
                                return num_dict[string_list[0]] * 100 + num_dict[string_list[2]] + num_dict[string_list[4]]

                            if string_list[5] in list(num_dict.keys())[:11]:
                                return 'После числа ' + ' '.join(
                                    string_list[:5]) + ' ожидался конец строки\nВстречено число ' + \
                                       string_list[5] + ', являющееся числом единиц'
                            if string_list[5] in list(num_dict.keys())[11:21]:
                                return 'После числа ' + ' '.join(
                                    string_list[:5]) + ' ожидался конец строки\nВстречено число ' + \
                                       string_list[5] + ' , являющееся числом формата 11 - 19'
                            if string_list[5] in list(num_dict.keys())[21:-4]:
                                return 'После числа ' + ' '.join(
                                    string_list[:5]) + ' ожидался конец строки\nВстречено число ' + \
                                       string_list[5] + ' , являющееся числом десятков'
                            if string_list[5] in list(num_dict.keys())[-4:-2]:
                                return 'После числа ' + ' '.join(
                                    string_list[:5]) + ' ожидался конец строки\nВстречено число ' + \
                                       string_list[5] + ' , являющееся сотней'
                            if string_list[5] in list(num_dict.keys())[-2:]:
                                return 'После числа ' + ' '.join(
                                    string_list[:5]) + ' ожидался конец строки\nВстречено число ' + \
                                       string_list[5] + ' , являющееся тысячей'
                            return 'После числа ' + ' '.join(string_list[:5]) + ' ожидался конец строки\nВстречено und'

                        if string_list[4] in list(num_dict.keys())[:11]:
                            return 'После ' + ' '.join(string_list[:4]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                                4] + ' , являющееся числом единиц'
                        if string_list[4] in list(num_dict.keys())[11:21]:
                            return 'После ' + ' '.join(string_list[:4]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                                4] + ' , являющееся числом формата 11 - 19'
                        if string_list[4] in list(num_dict.keys())[-4:-2]:
                            return 'После ' + ' '.join(string_list[:4]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                                4] + ' , являющееся сотней'
                        if string_list[4] in list(num_dict.keys())[-2:]:
                            return 'После ' + ' '.join(string_list[:4]) + ' ожидалось число десятков' + '\nВстречено число ' + string_list[
                                4] + ' , являющееся тысячей'
                        return 'После ' + ' '.join(string_list[:4]) + ' ожидалось число десятков\nВстречено und'

                    return 'После und ожидалось еще число десятков, а встречено конец строки'

                if string_list[3] in list(num_dict.keys())[:11]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся числом единиц'
                if string_list[3] in list(num_dict.keys())[11:21]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся числом формата 11 - 19'
                if string_list[3] in list(num_dict.keys())[21:-4]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся числом десятков'
                if string_list[3] in list(num_dict.keys())[-4:-2]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся сотней'
                if string_list[3] in list(num_dict.keys())[-2:]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся тысячей'
                return 'После числа ' + ' '.join(string_list[:3]) + ' не может идти ' + string_list[3] + '\nОжидалось: und и число десятков или конец строки'

            if string_list[2] in list(num_dict.keys())[11:21]:
                return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число единиц или десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся числом формата 11 - 19'
            if string_list[2] in list(num_dict.keys())[-4:-2]:
                return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число единиц или десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся сотней'
            if string_list[2] in list(num_dict.keys())[-2:]:
                return 'После ' + ' '.join(string_list[:2]) + ' ожидалось число единиц или десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся тысячей'
            return 'После числа ' + ' '.join(string_list[:2]) + ' не может идти ' + string_list[2] + '\nОжидалось: число единиц или десятков или конец строки'

        if string_list[1] in list(num_dict.keys())[:11]:
            return 'После числа ' + string_list[0] + ' ожидалось und или hundert или конец строки\nВстречено число ' + string_list[
                1] + ', являющееся числом единиц'
        if string_list[1] in list(num_dict.keys())[11:21]:
            return 'После числа ' + string_list[0] + ' ожидалось und или hundert или конец строки\nВстречено число ' + string_list[
                1] + ' , являющееся числом формата 11 - 19'
        if string_list[1] in list(num_dict.keys())[21:-4]:
            return 'После числа ' + string_list[0] + ' ожидалось und или hundert или конец строки\nВстречено число ' + string_list[
                1] + ' , являющееся числом десятков'
        if string_list[1] in list(num_dict.keys())[-2:]:
            return 'После числа ' + string_list[0] + ' ожидалось und или hundert или конец строки\nВстречено число ' + string_list[
                1] + ' , являющееся тысячей'
        return 'После числа ' + string_list[0] + ' не может идти ' + string_list[1] + '\nОжидалось: und или hundert или конец строки'

    if string_list[0] == 'hundert':
        # hundert zwei
        if string_list[1] in list(num_dict.keys())[:11]:
            if len(string_list) == 2:
                if string_list[1] == 'null':
                    return 'Число единиц не может быть равна нулю'
                if string_list[1] == 'ein':
                    return 'После ' + ' '.join(string_list[:2]) + ' не может идти конец строки\nОжидалось und и число десятков'
                return 100 + num_dict[string_list[1]]
            if string_list[2] == 'und':
                if len(string_list) == 3:
                    return 'После ' + ' '.join(string_list[:]) + ' не может идти конец строки\nОжидалось число десятков'
                if string_list[3] in list(num_dict.keys())[21:-4]:
                    if len(string_list) == 4:
                        return 100 + num_dict[string_list[1]] + num_dict[string_list[3]]
                    if string_list[4] in list(num_dict.keys())[:11]:
                        return 'После ' + ' '.join(
                            string_list[:4]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                   4] + ' , являющееся числом единиц'
                    if string_list[4] in list(num_dict.keys())[11:21]:
                        return 'После ' + ' '.join(
                            string_list[:4]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                   4] + ' , являющееся числом формата 11 - 19'
                    if string_list[4] in list(num_dict.keys())[21:-4]:
                        return 'После ' + ' '.join(
                            string_list[:4]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                   4] + ' , являющееся числом десятков'
                    if string_list[4] in list(num_dict.keys())[-4:-2]:
                        return 'После ' + ' '.join(
                            string_list[:4]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                   4] + ' , являющееся сотней'
                    if string_list[4] in list(num_dict.keys())[-2:]:
                        return 'После ' + ' '.join(
                            string_list[:4]) + ' ожидался конец строки' + '\nВстречено число ' + string_list[
                                   4] + ' , являющееся тысячей'
                    return 'После ' + ' '.join(string_list[:4]) + ' ожидался конец строки\nВстречено und'

                if string_list[3] in list(num_dict.keys())[:11]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось число десятков' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся числом единиц'
                if string_list[3] in list(num_dict.keys())[11:21]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось число десятков' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся числом формата 11 - 19'
                if string_list[3] in list(num_dict.keys())[-4:-2]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось число десятков' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся сотней'
                if string_list[3] in list(num_dict.keys())[-2:]:
                    return 'После ' + ' '.join(string_list[:3]) + ' ожидалось число десятков' + '\nВстречено число ' + \
                           string_list[
                               3] + ' , являющееся тысячей'
                return 'После ' + ' '.join(string_list[:3]) + ' ожидалось число десятков\nВстречено und'

            if string_list[2] in list(num_dict.keys())[:11]:
                return 'После ' + ' '.join(
                    string_list[:2]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся числом единиц'
            if string_list[2] in list(num_dict.keys())[11:21]:
                return 'После ' + ' '.join(
                    string_list[:2]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся числом формата 11 - 19'
            if string_list[2] in list(num_dict.keys())[21:-4]:
                return 'После ' + ' '.join(
                    string_list[:2]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся числом десятков'
            if string_list[2] in list(num_dict.keys())[-4:-2]:
                return 'После ' + ' '.join(
                    string_list[:2]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся сотней'
            if string_list[2] in list(num_dict.keys())[-2:]:
                return 'После ' + ' '.join(
                    string_list[:2]) + ' ожидалось und и число десятков или конец строки' + '\nВстречено число ' + \
                       string_list[
                           2] + ' , являющееся тысячей'
            # next stroka ne nyzhna. Ostavil na vsyakiy sluchai
            return 'После числа ' + ' '.join(string_list[:2]) + ' не может идти ' + string_list[
                3] + '\nОжидалось: und и число десятков или конец строки'

        if string_list[1] in list(num_dict.keys())[11:-4]:
            if len(string_list) == 2:
                return 100 + num_dict[string_list[1]]

            if string_list[2] in list(num_dict.keys())[:11]:
                return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено число ' + \
                       string_list[2] + ', являющееся числом единиц'
            if string_list[2] in list(num_dict.keys())[11:21]:
                return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено число ' + \
                       string_list[2] + ' , являющееся числом формата 11 - 19'
            if string_list[2] in list(num_dict.keys())[21:-4]:
                return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено число ' + \
                       string_list[2] + ' , являющееся числом десятков'
            if string_list[2] in list(num_dict.keys())[-4:-2]:
                return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено число ' + \
                       string_list[2] + ' , являющееся сотней'
            if string_list[2] in list(num_dict.keys())[-2:]:
                return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено число ' + \
                       string_list[2] + ' , являющееся тысячей'
            return 'После числа ' + ' '.join(string_list[:2]) + ' ожидался конец строки\nВстречено und'

        if string_list[1] == 'hundert':
            return 'После числа ' + ' '.join(string_list[:1]) + ' ожидалось число единиц, число дестяков или числа формата 11 - 19\nВстречено число ' + string_list[1] + ' , являющееся сотней'
        if string_list[1] == 'tausend':
            return 'После числа ' + ' '.join(
                string_list[:1]) + ' ожидалось число единиц, число дестяков или числа формата 11 - 19\nВстречено число ' + \
                   string_list[1] + ' , являющееся тысячей'
        return 'После числа ' + ' '.join(string_list[:1]) + ' ожидалось число единиц, число дестяков или числа формата 11 - 19\nВстречено ' + string_list[1]

    return 'Неизвестная ошибка'

print('hundert zehn')
