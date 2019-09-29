list_no_fl = []


def flat_list(list_w_fl):
    list_no_fl.clear()

    def fl_list(list_w_fl):
        for el in list_w_fl:
            if type(el) == list:
                fl_list(el)
            if type(el) == int:
                list_no_fl.append(el)
        return list_no_fl

    return fl_list(list_w_fl)


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
