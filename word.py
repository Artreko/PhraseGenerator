class Word:
    def __init__(
            self, forms: tuple,
            word_type: str,
            gender: int = 0,
            subjective: bool = False,
            case: int = 0,
            next_case: int = 0):
        """
        :param forms: падеж, род/падеж
        :param word_type: noun, adjective, verb, preposition
        :param gender: 0 - male, 1 - female
        :param subjective: True - если может совершать действия|действие можно совершить над чем-то
        """
        self.forms = forms
        self.gender = gender
        self.word_type = word_type
        self.subjective = subjective
        self.case = case
        self.next_case = next_case

    def __str__(self):
        match self.word_type:
            case 'adjective':
                if self.gender == 0 and self.case == 3:
                    return self.forms[self.gender][0]
                return self.forms[self.gender][self.case]
            case 'preposition':
                return self.forms[0]
            case _:
                return self.forms[self.case]

    @classmethod
    def get_word(cls, params_tuple: tuple):
        match len(params_tuple):
            case 6:
                return cls(params_tuple[0], params_tuple[1],
                           params_tuple[2], params_tuple[3],
                           params_tuple[4], params_tuple[5]
                           )
            case 5:
                return cls(params_tuple[0], params_tuple[1],
                           params_tuple[2], params_tuple[3],
                           params_tuple[4], 0
                           )
            case 4:
                return cls(params_tuple[0], params_tuple[1],
                           params_tuple[2], params_tuple[3],
                           0, 0
                           )
            case 3:
                return cls(params_tuple[0], params_tuple[1], params_tuple[2], False, 0, 0)
            case 2:
                return cls(params_tuple[0], params_tuple[1], 0, False, 0, 0)


NOUNS = [
    (('человек', 'человека', 'человеку', 'человека', 'человеком', 'человеке'), 'noun', 0, True),
    (('стол', 'стола', 'столу', 'стол', 'столом', 'столу'), 'noun', 0, False),
    (('собака', 'собаки', 'собаке', 'собаку', 'собакой', 'собаке'), 'noun', 1, True),
    (('пакет', 'пакета', 'пакету', 'пакет', 'пакетом', 'пакете'), 'noun', 0, False),
    (('картошка', 'картошки', 'картошке', 'картошку', 'картошкой', 'картошке'), 'noun', 1, False),
]
NOUNS = [Word.get_word(word) for word in NOUNS]
NOUNS_SUBJ = [noun for noun in NOUNS if noun.subjective]
ADJECTIVES = [
    ((
        ('красный', 'красного', 'красному', 'красного', 'красным', 'красном',),
        ('красная', 'красной', 'красной', 'красную', 'красной', 'красной',)
    ), 'adjective'),
    ((
        ('маленький', 'маленького', 'маленькому', 'маленького', 'маленьким', 'маленьком'),
        ('маленькая', 'маленькой', 'маленькой', 'маленькую', 'маленькой', 'маленькой')
    ), 'adjective'),
    ((
        ('большой', 'большого', 'большому', 'большого', 'большим', 'большом',),
        ('большая', 'большой', 'большой', 'большую', 'большой', 'большой',)
    ), 'adjective')
]
ADJECTIVES = [Word.get_word(word) for word in ADJECTIVES]
VERBS = [
    (('положить', 'положит'), 'verb', None, True, 0, 3),
    (('кинуть', 'кинет'), 'verb', None, True, 0, 3),
    (('взять', 'возьмет'), 'verb', None, True, 0, 3),
    (('есть', 'ест'), 'verb', None, True, 0, 3),
    (('бежать', 'бежит'), 'verb', None, False, 0, None),
]
VERBS = [Word.get_word(word) for word in VERBS]
VERBS_ACT = [verb for verb in VERBS if verb.subjective]
PREPOSITIONS = [
    (('в',), 'preposition', None, None, 5, 5),
    (('к',), 'preposition', None, None, 2, 2),
    (('над',), 'preposition', None, None, 4, 4),
]
PREPOSITIONS = [Word.get_word(word) for word in PREPOSITIONS]
WORDS = {
    'NOUNS': tuple(NOUNS),
    'ADJECTIVES': tuple(ADJECTIVES),
    'VERBS': tuple(VERBS),
    'PREPOSITIONS': tuple(PREPOSITIONS),
}
