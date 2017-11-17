from collections import Counter
import re
import os
import argparse


def get_first_txt_file_path_from_root_directry():
    txt_file_path = ''
    file_names_in_current_dir = os.listdir(os.curdir)

    for file_name in file_names_in_current_dir:
        if re.fullmatch(r'.+\.txt', file_name):
            txt_file_path = os.path.join(os.curdir, file_name)
            break

    return txt_file_path


def load_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            'Couldn\'t find txt file. {}'.format(file_path))
    except IOError:
        raise IOError('Couldn\'t read file: {}'.format(format(file_path)))
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
    terminal_parser = argparse.ArgumentParser(
        description='List the most frequent words in text.')
    terminal_parser.add_argument('--path', '-p',help='Path of .txt file')
    terminal_parser.add_argument('--num_words', '-n', type=int, default=10,
                                 help='Number of words to show')
    args = terminal_parser.parse_args()

    file_path = args.path or get_first_txt_file_path_from_root_directry()
    number_of_words_to_show = args.num_words

    try:
        text = load_text_from_file(file_path)
    except FileNotFoundError as err:
        print(err)
    except IOError as err:
        print(err)
    else:
        words_list = extract_words_list_from_text(text)
        most_frequent_words_list = get_most_frequent_words(
            words_list, number_of_words_to_show)

        print("Top {} most frequent words:".format(number_of_words_to_show))
        for index, word in enumerate(most_frequent_words_list, 1):
            print('{:2}.: {}'.format(index, word))
