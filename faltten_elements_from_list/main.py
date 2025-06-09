from flatten_list import flattens


def main()-> None:
    test1 = []
    exp1 = []
    res1 = flattens(test1)
    assert res1 == exp1, "failure in handling empty elements"

    test2 = [1, 2, [3], [4, 5], [6, [7, [8, 9, [10, 11]]]]]
    exp2 = [val for val in range(1, 12)]
    res2 = flattens(test2)
    assert res2 == exp2, "failure in multi-layer elements"

    test3 = [1, 2, []]
    exp3 = [val for val in range(1, 3)]
    res3 = flattens(test3)
    assert res3 == exp3, "failure in handling nested empty elements"

    test4 = [1, 2, 3, 4]
    test4[0] = test4
    exp4 = [val for val in range(2, 5)]
    res4 = flattens(test4)
    assert res4 == exp4, "failure in handling recursive elements"

    test5 = [1, 2, 3, 4]
    test5[1] = test5
    exp5 = [1, 3, 4]
    res5 = flattens(test5)
    assert res5 == exp5, "failure in handling recursive elements"

    print("overall success")


if __name__ == "__main__": 
    main()