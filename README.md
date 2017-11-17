# Frequency Analysis of Words

This script shows the most frequent words used in a given text.
It can take up to 2 arguments: 
* --path, -p: path to file (optional argument, by default the first .txt document in root directory will be taken)
* --num_words, -n: number of words to show (optional argument, default=10)

# How to use
```
$ python lang_frequency.py -p path_to_file -n number_of_words_to_show
```

# Examples:

Example with one argument (path). 
By default the list of 10 most frequent words is given:
```
$ python lang_frequency.py
Top 10 most frequent words from the first .txt document in root directory:
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

Example with two arguments (path, number_of_words), shows 5 most frequent word in text.
```
$python lang_frequency.py -p '/Users/KirillMaslov/Documents/some_text.txt' -n 5
Top 5 most frequent words:
 1.: и
 2.: я
 3.: не
 4.: в
 5.: что
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
