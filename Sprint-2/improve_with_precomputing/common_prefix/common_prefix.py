# from typing import List


# def find_longest_common_prefix(strings: List[str]):
#     """
#     find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

#     In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
#     """
#     longest = ""
#     for string_index, string in enumerate(strings):
#         for other_string in strings[string_index+1:]:
#             common = find_common_prefix(string, other_string)
#             if len(common) > len(longest):
#                 longest = common
#     return longest


# def find_common_prefix(left: str, right: str) -> str:
#     min_length = min(len(left), len(right))
#     for i in range(min_length):
#         if left[i] != right[i]:
#             return left[:i]
#     return left[:min_length]

from typing import List


def find_longest_common_prefix(strings: List[str]):
    """
    find_longest_common_prefix returns the longest string common at the start of any two strings in the passed list.

    In the event that an empty list, a list containing one string, or a list of strings with no common prefixes is passed, the empty string will be returned.
    """
    # //empty list test
    if len(strings) < 2:
        return ""

    # add soting alphabetically 
    strings.sort()
    longest = ""
    # for string_index, string in enumerate(strings):
    #     for other_string in strings[string_index+1:]:
    #         common = find_common_prefix(string, other_string)
    #         if len(common) > len(longest):
    #             longest = common
    # return longest
    for i in range(len(strings)-1):
        word_at_this_index = strings[i]
        word_at_next_index = strings[i+1]

        common = find_common_prefix(word_at_this_index, word_at_next_index)
        if len(common) > len(longest):
            longest = common
    return longest

def find_common_prefix(left: str, right: str) -> str:
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_length]
