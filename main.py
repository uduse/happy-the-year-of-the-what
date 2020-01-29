import json
import random


animal_pronouciations = {
    '🐷': ['zhū', 'zhú', 'zhǔ', 'zhù'],
    '🐀': ['shū', 'shú', 'shǔ', 'shù'],
}


def generate(animal):
    with open('idiom.json', encoding='utf-8') as f:
        idioms = json.load(f)

    collected = []
    for idiom in idioms:
        word = idiom['word']
        if len(word) == 4:
            pinyin = idiom['pinyin'].split()
            indices = []
            for i, e in enumerate(pinyin):
                if e in animal_pronouciations[animal]:
                    indices.append(i)
            if indices:
                chars = list(word)
                for index in indices:
                    chars[index] = animal
                word = ''.join(chars)
                collected.append(word)

    random.shuffle(collected)

    with open("README.md", 'w', encoding='utf-8') as f:
        header = f"# {animal}年快乐！！！ \n## "
        content = f'祝大家{animal}年：' + '，'.join(collected) + '！' * 20
        f.write(header + content)


if __name__ == '__main__':
    generate('🐀')