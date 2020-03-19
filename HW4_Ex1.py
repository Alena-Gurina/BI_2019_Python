# Task 1
# Let's continue examining words. You are given two string with words separated by commas. ' \
#    'Try to find what is common between these strings. The words are not repeated in the same string.
#
# Your function should find all of the words that appear in both strings.
# The result must be represented as a string of words separated by commas in **alphabetic order.**
#
# **Input:** Two arguments as strings.
#
# **Output:** The common words as a string


def checkio(first, second):
    res_list = []
    arg_1 = first.split(",")
    arg_2 = second.split(",")
    for word in arg_1:
        if word in arg_2:
            res_list.append(word)
    res_list = sorted(res_list)
    res = ",".join(res_list)
    return res


print(checkio("hello,world", "hello,earth") == "hello")
print(checkio("one,two,three", "four,five,six") == "")
print(checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
