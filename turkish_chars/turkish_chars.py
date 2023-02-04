
class TurkishChars:
    def __init__(self, target_text):
        self.text = target_text
        self.tc_dict = {'İ': 'I', 'ı': 'i', 'Ö': 'O', 'ö': 'o', 'Ü': 'U', 'ü': 'u',
                        'ğ': 'g', 'Ğ': 'G', 'Ş': 'S', 'ş': 's', 'Ç': 'C', 'ç': 'c'}
        self.eng = self.convert_to_eng(self.text)

    def convert_to_eng(self, txt_to_process):
        return "".join([c if c not in self.tc_dict.keys() else self.tc_dict[c] for c in txt_to_process])



if __name__ == '__main__':
    text = 'Sesi büzüşesiceler.'
    tc = TurkishChars(text)
    # print([text])
    print(tc.eng)
    