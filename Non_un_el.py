# Your optional code here
# You can import some modules or create additional functions


def checkio(list_with_el):
    un_el = []  # create empty list for unique el
    for x in list_with_el:
        if list_with_el.count(x) < 2:  # find unique el
            un_el.append(x)
    for x in un_el:
        list_with_el.remove(x)
    return list_with_el


if __name__ == "__main__":  # base check for this function
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
