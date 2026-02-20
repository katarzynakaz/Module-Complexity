# def count_letters(s: str) -> int:
#     """
#     count_letters returns the number of letters which only occur in upper case in the passed string.
#     """
#     only_upper = set()
#     for letter in s:
#         if is_upper_case(letter):
#             if letter.lower() not in s:
#                 only_upper.add(letter)
#     return len(only_upper)


# def is_upper_case(letter: str) -> bool:
#     return letter == letter.upper()


def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    seen_in_string = {}

    for letter in s:
        #emptyval for key because found by key
        seen_in_string[letter] = True

    only_upper = {}
    for letter in s:
        if is_upper_case(letter):
            if letter.lower() not in seen_in_string:
                    only_upper[letter] = True

    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
