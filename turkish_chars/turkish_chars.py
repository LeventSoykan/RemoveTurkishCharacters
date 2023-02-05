

tc_dict = {'İ': 'I', 'ı': 'i', 'Ö': 'O', 'ö': 'o', 'Ü': 'U', 'ü': 'u',
                        'ğ': 'g', 'Ğ': 'G', 'Ş': 'S', 'ş': 's', 'Ç': 'C', 'ç': 'c'}


def convert_to_eng(txt_to_process):
    return "".join([c if c not in tc_dict.keys() else tc_dict[c] for c in txt_to_process])


def highlight_tc(txt_to_process):
    string_exp = "".join([c if c not in tc_dict.keys() else '\033[1m'+c+'\033[0m' for c in txt_to_process])
    print(string_exp)


if __name__ == '__main__':
    text = 'Sesi büzüşesiceler. Çılgın dağcan'
    print(convert_to_eng(text))
    highlight_tc(text)

