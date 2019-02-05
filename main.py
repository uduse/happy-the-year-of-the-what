import json
import random


def main():
    with open('idiom.json', encoding='utf-8') as f:
        idioms = json.load(f)

    collected = []
    for idiom in idioms:
        word = idiom['word']
        if len(word) == 4:
            pinyin = idiom['pinyin'].split()
            indices = []
            for i, e in enumerate(pinyin):
                if e in ['zhū', 'zhú', 'zhǔ', 'zhù']:
                    indices.append(i)
            if indices:
                chars = list(word)
                for index in indices:
                    chars[index] = '🐷'
                word = ''.join(chars)
                collected.append(word)

    random.shuffle(collected)

    with open("README.md", 'w', encoding='utf-8') as f:
        header = "# 🐷年快乐！！！ \n## "
        content = '祝大家🐷年：' + '，'.join(collected) + '！' * 20
        f.write(header + content)


if __name__ == '__main__':
    main()
