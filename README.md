# Frequency Analysis of Words

This script shows the most frequent words used in a given text.
It can take up to 2 arguments: 
* path (positional argument): path to file.
* --num_words, -n  (optional argument): number of words to show, default value = 10.

# How to use
```
$ python lang_frequency.py path_to_file -n number_of_words_to_show
```

# Examples:

Example with one argument (path). 
By default the list of 10 most frequent words:
```
$ python lang_frequency.py '~/Documents/some_file.txt'
Top 10 most frequent words:
 1.: и
 2.: я
 3.: не
 4.: в
 5.: что
 6.: на
 7.: с
 8.: он
 9.: Я
10.: мне
```

Example with two arguments (path, num_words).
```
$python lang_frequency.py '~/Documents/some_file.txt' -n 5
Top 5 most frequent words:
 1.: и
 2.: я
 3.: не
 4.: в
 5.: что
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
