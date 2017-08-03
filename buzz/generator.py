import random

buzz = ('непрерывное тестирование', 'непрерывная интергация',
    'непрерывное развертывание', 'непрерывное улучшение', 'devops')
adjectives = ('полный', 'современный', 'самодостаточный', 'интегрированный', 'оконченный')
adverbs = ('замечетально', 'чрезвычайно', 'по существу', 'существенно','серьезно')
verbs = ('ускоряет', 'улучшает', 'усиливает', 'реконструирует', 'форсирует')
#типа синхронизировались
def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result
newcomment
def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print (generate_buzz())