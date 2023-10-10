from collections import Counter


def count_most_common_words(word_list):
    print(Counter(word_list).most_common(4))


if __name__ == "__main__":
    words = ['London', 'Oslo', 'Paris', 'Rome', 'Paris', 'Geneva', 'Paris', 'Milano',
             'Geneva', 'Paris', 'Granada', 'Rome', 'Rome', 'London', 'London', 'Geneva',
             'Geneva', "Oslo", 'Rome', 'Oslo', 'Oslo', 'Rome', 'Oslo', 'Rome',
             'Geneva', 'Granada', "Granada", 'London']
    count_most_common_words(words)
