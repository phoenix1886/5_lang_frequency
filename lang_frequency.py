from collections import Counter
import re
import argparse


def create_arguments_parser():
    arguments_parser = argparse.ArgumentParser(
        description='List the most frequent words in text.')
    arguments_parser.add_argument('path', help='Path of a file')
    arguments_parser.add_argument('--num_words', '-n', type=int, default=10,
                                 help='Number of words to show')

    return arguments_parser


def load_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    return text


def extract_words_list_from_text(text):
    text = text.lower()
    words_list = re.findall(r'\w+', text)

    return words_list


def get_most_frequent_words(words_list, number_of_words_to_show=10):
    words_counter = Counter(words_list)
    most_frequent_words = [word for word, frequency in
                           words_counter.most_common(number_of_words_to_show)]

    return most_frequent_words


if __name__ == '__main__':
    arguments_parser = create_arguments_parser()
    args = arguments_parser.parse_args()

    file_path = args.path
    text = load_text_from_file(file_path)
    words_list = extract_words_list_from_text(text)

    number_of_words_to_show = args.num_words
    most_frequent_words_list = get_most_frequent_words(
        words_list, number_of_words_to_show)

    print("Top {} most frequent words:".format(number_of_words_to_show))
    for index, word in enumerate(most_frequent_words_list, 1):
        print('{:2}.: {}'.format(index, word))
