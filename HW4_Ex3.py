# Task 3

# From a set of ints you have to create a list of closed intervals as tuples,
# so the intervals are covering all the values found in the set.
#
# A closed interval includes its endpoints! The interval *1..5*, for example,
#     includes each value *x* that satifies the condition *1 <= x <= 5*.
#
# Values can only be in the same interval if the difference between
#     a value and the next smaller value in the set equals one, otherwise a new interval begins.
#     Of course, the start value of an interval is excluded from this rule.
#     A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.
#
# **Input:** A set of ints.
#
# **Output:** A list of tuples of two ints, indicating the endpoints of the interval.
# The Array should be sorted by start point of each interval


def create_intervals(data):
    data = list(data)
    data_sort = sorted(data)
    res = []
    start_int = data_sort[0]
    for i in range(len(data_sort) - 1):
        diff = data_sort[i + 1] - data_sort[i]
        if diff > 1:
            fin_int = data_sort[i]
            tup = (start_int, fin_int)
            print(tup)
            res.append(tup)
            start_int = data_sort[i + 1]
        if data_sort[i + 1] == data_sort[-1]:
            last_fin_int = data_sort[-1]
            tup = (start_int, last_fin_int)
            res.append(tup)
    return res


print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)])
print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])
