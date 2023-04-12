"""Python functions for JavaScript Trials 1."""
#Tuesdaylab


def output_all_items(items):
    for item in items:
        print(item)


# arr = ['a', 'b', 'c']
# output_all_items(arr)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)

    return evenNums


# numsArr = [0, 1, 2, 3, 4, 5]
# print(get_all_evens(numsArr))


def get_odd_indices(items):
    result = []

    for ind, item in enumerate(items):
        if ind % 2 != 0:
            result.append(item)

    return result


# oddArr = ['no', 'yes', 'non', 'si', 'nein', 'oui']
# print(get_odd_indices(oddArr))


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code


def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
