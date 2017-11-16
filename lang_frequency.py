from collections import Counter
from heapq import nlargest
import re
import sys


def load_data(filepath):
    text = ''
    try:
        with open(filepath, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Couldn\'t find file: {}'.format(filepath))
    except IOError:
        raise IOError('Couldn\'t read file: {}'.format(format(filepath)))
    return text


def extract_word_list_from_text(text):
    text = text.lower()
    pattern = re.compile(r'\w+')
    word_list = re.findall(pattern, text)

    return word_list


def get_most_frequent_words(text, n_frequent_words):
    word_list = extract_word_list_from_text(text)
    text_counter = Counter(word_list)
    n_frequent_words = nlargest(n_frequent_words, text_counter,
                                key=text_counter.__getitem__)

    return n_frequent_words


if __name__ == '__main__':
    default_number_of_frequent_words = 10
    default_file_path = './Герой_нашего_времени.txt'

    file_path = sys.argv[1] if len(sys.argv) > 1 \
        else default_file_path
    number_of_frequent_words = int(sys.argv[2]) if len(sys.argv) > 2 \
        else default_number_of_frequent_words

    try:
        text = load_data(file_path)
    except FileNotFoundError as err:
        print(err)
    except IOError as err:
        print(err)
    else:
        most_frequent_words_list = \
            get_most_frequent_words(text, number_of_frequent_words)

        print("Top {} most frequent words:".format(number_of_frequent_words))
        for index, word in enumerate(most_frequent_words_list):
            print('{:2}.: {}'.format(index+1, word))
