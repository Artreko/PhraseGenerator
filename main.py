import random as r
from word import *


class PhraseGenerator:
    def __init__(self):
        self.phrase = []
        self.verbNotIn = True
        self.prepNotIn = True
        self.adjCount = 0

    def start(self):
        self.generator(r.choice(['SN', 'SA', 'SV']))

    def generator(self, method):
        match method:
            case 'SN':
                self.phrase.append(r.choice(NOUNS))
                self.generator('V')
            case 'SA':
                self.phrase.append(r.choice(ADJECTIVES))
                self.adjCount += 1
                choices = ['N', 'A']
                self.generator(r.choice(choices))
            case 'SV':
                self.phrase.append(r.choice(VERBS))
                self.verbNotIn = False
                self.generator(r.choice(['P', 'N']))
            case 'V':
                self.phrase.append(r.choice(VERBS))
                self.verbNotIn = False
                choices = ['', 'N']
                if self.prepNotIn:
                    choices.append('P')
                self.generator(r.choice(choices))
            case 'N':
                self.phrase.append(r.choice(NOUNS))
                self.adjCount = 0
                choices = ['']
                if self.prepNotIn:
                    choices.append('P')
                    if self.verbNotIn :
                        choices.append('V')
                self.generator(r.choice(choices))
            case 'P':
                self.phrase.append(r.choice(PREPOSITIONS))
                self.prepNotIn = False
                choices = ['N']
                if self.adjCount < 2:
                    choices.append('A')
                self.generator(r.choice(choices))
            case 'A':
                self.phrase.append(r.choice(ADJECTIVES))
                self.adjCount += 1
                choices = ['N']
                if self.adjCount < 2:
                    choices.append('A')
                self.generator(r.choice(choices))
            case _:
                pass


if __name__ == '__main__':
    with open("file.txt", 'a', encoding='utf-8') as f:
        for _ in range(10):
            ph = PhraseGenerator()
            ph.start()
            print(*ph.phrase, file=f)


