import random
from copy import copy
from word import *


expressions = [
    ['predicate', 'addition'],
    ['predicate', 'definition', 'addition'],
    ['definition', 'subject'],
    ['subject', 'preposition', 'condition'],
    ['definition', 'subject', 'preposition', 'condition'],
    ['definition', 'subject', 'preposition', 'definition', 'condition'],
    ['subject', 'predicate'],
    ['subject', 'predicate', 'addition'],
    ['subject', 'predicate', 'definition', 'addition'],
    ['definition', 'subject', 'predicate', 'addition'],
    ['definition', 'subject', 'predicate', 'definition', 'addition'],
    ['subject', 'predicate', 'preposition', 'condition'],
    ['subject', 'predicate', 'definition', 'addition', 'preposition', 'condition'],
    ['definition', 'subject', 'predicate', 'preposition', 'condition'],
    ['definition', 'subject', 'predicate', 'definition', 'addition', 'preposition', 'condition'],
    ['subject', 'predicate', 'preposition', 'definition', 'condition'],
    ['subject', 'predicate', 'definition', 'addition', 'preposition', 'definition', 'condition'],
    ['definition', 'subject', 'predicate', 'preposition', 'definition', 'condition'],
    ['definition', 'subject', 'predicate', 'definition', 'addition', 'preposition', 'definition', 'condition'],
]

COMP_DICT = {
    'definition': 'ADJECTIVES',
    'predicate': 'VERBS',
    'subject': 'NOUNS',
    'addition': 'NOUNS',
    'condition': 'NOUNS',
    'preposition': 'PREPOSITIONS',
}


def desc(expression, phrase):
    for idx, role in enumerate(expression):
        print(role, phrase[idx], phrase[idx].case)


def fill_expression(expression):
    is_addition_in = 'addition' in expression
    is_subject_in = 'subject' in expression
    is_predicate_in = 'predicate' in expression
    is_condition_in = 'condition' in expression
    is_definition_in = 'definition' in expression
    phrase = []
    for role in expression:
        match role:
            case 'subject':
                if is_predicate_in:
                    phrase.append(copy(random.choice(NOUNS_SUBJ)))
                else:
                    phrase.append(copy(random.choice(NOUNS)))
            case 'predicate':
                if is_addition_in:
                    phrase.append(copy(random.choice(VERBS_ACT)))
                else:
                    phrase.append(copy(random.choice(VERBS)))
                phrase[-1].case = int(is_subject_in)
            case _:
                phrase.append(copy(random.choice(WORDS[COMP_DICT[role]])))
    if is_addition_in:
        addition_idx = expression.index('addition')
        predicate_idx = expression.index('predicate')
        phrase[addition_idx].case = phrase[predicate_idx].next_case
    if is_condition_in:
        condition_idx = expression.index('condition')
        preposition_idx = expression.index('preposition')
        phrase[condition_idx].case = phrase[preposition_idx].next_case
    if is_subject_in:
        subject_idx = expression.index('subject')
        phrase[subject_idx].case = 0
    if is_definition_in:
        for idx, role in enumerate(expression):
            if role == 'definition':
                phrase[idx].case = phrase[idx + 1].case
                phrase[idx].gender = phrase[idx + 1].gender
    desc(expression, phrase)
    return phrase


if __name__ == '__main__':
    with open("file.txt", 'a') as f:
        for expr in expressions:
            ph = fill_expression(expr)
            print(*ph)
            print()
            ph = [str(word) for word in ph]
            outline = ' '.join(ph) + '\n'
            f.write(outline)
