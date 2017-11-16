from collections import Counter
from heapq import nlargest
import re
import sys


def load_text_from_file(filepath):
    text = ''
    try:
        with open(filepath, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Couldn\'t find file: {}'.format(filepath))
    except IOError:
        raise IOError('Couldn\'t read file: {}'.format(format(filepath)))
    return text


def extract_words_list_from_text(text):
    text = text.lower()
    words_list = re.findall(r'\w+', text)

    return words_list


def get_most_frequent_words(text, number_of_words_to_show):
    words_list = extract_words_list_from_text(text)
    words_counter = Counter(words_list)
    most_frequent_words = nlargest(number_of_words_to_show, words_counter,
                                   key=words_counter.__getitem__)

    return most_frequent_words


if __name__ == '__main__':
    default_number_of_words_to_show = 10
    default_file_path = './Герой нашего времени.txt'

    file_path = sys.argv[1] if len(sys.argv) > 1 \
        else default_file_path
    number_of_words_to_show = int(sys.argv[2]) if len(sys.argv) > 2 \
        else default_number_of_words_to_show

    try:
        text = load_text_from_file(file_path)
    except FileNotFoundError as err:
        print(err)
    except IOError as err:
        print(err)
    else:
        most_frequent_words_list = \
            get_most_frequent_words(text, number_of_words_to_show)

        print("Top {} most frequent words:".format(number_of_words_to_show))
        for index, word in enumerate(most_frequent_words_list):
            print('{:2}.: {}'.format(index+1, word))
