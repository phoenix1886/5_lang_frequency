# Frequency Analysis of Words

This script calculates the most frequent words used in a given text.
It can take up to 2 arguments: 
* path to file
* number of words to show (optional argument, default=10)

# How to use
```
$ python path_to_file number_of_words_to_show
```

# Examples:

Example with one argument (path). 
By default the list of 10 most frequent word is given:
```
$ python lang_frequency.py '/Users/UserName/Documents/Герой_нашего_времени.txt'
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

Example with two arguments (path, number_of_words):
```
$python lang_frequency.py '/Users/KirillMaslov/Documents/Герой_нашего_времени.txt' 5
Top 5 most frequent words:
 1.: и
 2.: я
 3.: не
 4.: в
 5.: что
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
