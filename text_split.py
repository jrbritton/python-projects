# Remove punctuation and count words

from collections import Counter

# Input text here
text = '''Hello, there there!
This is is a test test test test. Do you see any punctuation?'''


def word_count(text):
    text = text.replace('\n', ' ') # removes new line \n
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punc = ""
    for char in text:
        if char not in punctuation:
            no_punc += char
    no_punc = no_punc.lower()
    no_punc = no_punc.split(" ")
    word_list = []
    for word in no_punc:
        count = no_punc.count(word)
        word_list.append(word)
        if (count == 1) and (word_list.count(word) == 1):
            print(f"{word} was used {count} time.")
        elif (count > 1) and (word_list.count(word) < 2):
            print(f"{word} was used {count} times.")


word_count(text)

# A better way.
# Create a set of unique items before searching them in the original string

def word_counter(text):
    text = text.replace('\n', ' ') # removes new line \n
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punc = ""
    for char in text:
        if char not in punctuation:
            no_punc += char
    no_punc = no_punc.lower()
    no_punc = no_punc.split(" ")
    word_set = set(no_punc)
    for word in word_set:
        count = no_punc.count(word)
        if count == 1:
            print(f"{word} was used {count} time.")
        elif count > 1:
            print(f"{word} was used {count} times.")


word_counter(text)


def top_3_words(text):
    text = text.replace('\n', ' ')
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punc = ""
    for char in text:
        if char not in punctuation:
            no_punc += char
    text = no_punc.lower()
    text = text.split(" ")
    text = Counter(text)
    top3 = text.most_common(3)
    print(top3)


top_3_words(text)


# Unused

##count_list = []
##for word in word_set:
##    count = no_punc.count(word)
##    count_list.append(f'{word}, {count}')
##count_list = sorted(count_list)
##print(count_list)
