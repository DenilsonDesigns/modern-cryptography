cipher = """fasdfasdf ggbjmqqdef fdfwewef xvpoqwer sd sadff 
wewerr fasdf poyert fgjwe asdf dfsdfjk qwervv jkqwert pqwer asdfn qwer
fasdf qwerfop lsdflk asdfjk
"""


class Attack:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}

    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0

        letter_count = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1

        for c in self.freq:
            self.freq[c] = round(self.freq[c]/letter_count, 4)

    def print_freq(self):
        for c in self.freq:
            print(c, ':', self.freq[c], end="\n")


attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
