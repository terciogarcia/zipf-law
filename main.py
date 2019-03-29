import matplotlib.pyplot as plt
import re

def get_words_from_file(filename):
    with open(filename) as file:
        content = file.readlines()

    content = ''.join(content)
    regex = re.compile('[^a-zA-Z ]')
    all_words = regex.sub('', content.lower()).split()
    return all_words


def count_words(all_words):
    dict_words = dict()
    for word in all_words:
        dict_words[word] = dict_words.setdefault(word, 0) + 1
    return dict_words


def plot_frequency_chart(sorted_words):
    words = [x[0] for x in sorted_words]
    frequence = [y[1] for y in sorted_words]
    plt.bar(words, frequence)
    plt.title('Frequência de ocorrência das palavras')
    plt.ylabel('Ocorrências')
    plt.xlabel('Palavras')
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    words = count_words(get_words_from_file('bible.txt'))
    sorted_words = sorted(words.items(), reverse=True, key=lambda kv: kv[1])
    plot_frequency_chart(sorted_words[:50])
