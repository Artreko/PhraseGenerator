class Word:
    def __init__(self, word:str, type:str):
        self.word = word
        self.type = type

    def __str__(self):
        return self.word

    def print_word(self):
        print(f'{self.word} - {self.type}')


NOUNS = [
    'человек',
    'стол',
    'собака',
    'самолет',
    'картошка',
]
NOUNS = [Word(word, 'noun') for word in NOUNS]
ADJECTIVES = [
    'красный',
    'маленький',
    'большой',
]
ADJECTIVES = [Word(word, 'adjective') for word in ADJECTIVES]
VERBS = [
    'положить',
    'кинуть',
    'взять',
    'есть',
    'бежать',
]
VERBS = [Word(word, 'verb') for word in VERBS]
PREPOSITIONS = [
    'в',
    'к',
    'на',
]
PREPOSITIONS = [Word(word, 'preposition') for word in PREPOSITIONS]
WORDS = NOUNS + ADJECTIVES + VERBS + PREPOSITIONS