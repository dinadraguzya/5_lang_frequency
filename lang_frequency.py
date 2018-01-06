import re
import collections
import os
import sys


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        return opened_file.read().lower()


def get_most_frequent_words(text):
    words_list = re.sub('[\W]', ' ', text).split()
    counter = collections.Counter(words_list)
    return counter.most_common(10)


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path) and os.path.isfile(file_path):
        text = load_data(file_path)
        words = get_most_frequent_words(text)
        print('The top 10 most frequent words:\n')
        for word in words:
            print('{} : {}'.format(word[0], word[1]))
    else:
        print("The file doesn't exist!")