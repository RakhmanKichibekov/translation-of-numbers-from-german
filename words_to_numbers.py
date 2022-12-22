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
    "sechzehn": 16,
    "siebzehn": 17,
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
    string = string.lower().strip()
    if (simple_elem_to_num(string) is not None) and (string != 'ein'):
        return simple_elem_to_num(string)
    if 'hundert' not in string:
        return two_digits_to_num(string)
    else:
        return three_digits_to_num(string)


def simple_elem_to_num(string, start_point=0, finish_point=1000, exc=()):
    if string in num_dict:
        if (num_dict[string] in range(start_point, finish_point+1)) and (num_dict[string] not in exc):
            return num_dict[string]


def two_digits_to_num(string):
    if string.endswith('zehn'):
        # return 10 + num_dict[string[:-4]]
        try:
            return 10 + simple_elem_to_num(string[0:string.index('zehn')], start_point=3, finish_point=9, exc=(6,7))
        except:
            return None
    string_list = string.split('und')
    if string_list[0] == 'eins':
        return None
    try:
        return simple_elem_to_num(string_list[0], finish_point=9) + simple_elem_to_num(string_list[1], start_point=20, finish_point=90)
    except:
        return None


def three_digits_to_num(string):
    multiplier = 1
    start_word = string[0:string.index('hundert')]

    if start_word and (start_word != 'ein'):
        try:
            multiplier *= simple_elem_to_num(start_word, start_point=2, finish_point=9)
        except:
            return None

    if len(string) == (string.index('hundert') + 7):
        try:
            return multiplier * 100
        except:
            return None
    if simple_elem_to_num(string[string.index('hundert') + 7:]):
        return multiplier * 100 + simple_elem_to_num(string[string.index('hundert') + 7:])
    try:
        return multiplier * 100 + two_digits_to_num(string[string.index('hundert') + 7:])
    except:
        return None


# print(convert_to_num('zwanzig'))

# answers = []
# checks = []
#
# with open('test.txt', 'r') as f:
#     data = f.readlines()
#     for line in data:
#         if not line.isspace():
#             answers.append(line.strip().split()[0])
#             checks.append(line.strip().split()[1])
#     f.close()
#
# answers = list(map(int, answers))
# dict = dict(zip(checks, answers))
#
#
# for check in checks:
#     if convert_to_num(check) != dict[check]:
#         print(check)


