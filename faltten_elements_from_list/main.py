from flatten_list import flattens_iterative, flattens_recursive
import copy


def main()-> None:
    test1 = []
    exp1 = []
    test11 = copy.deepcopy(test1)
    test12 = copy.deepcopy(test1)
    res11 = flattens_iterative(test11)
    res12 = flattens_recursive(test12)
    assert res11 == exp1, "failure in handling empty elements"
    assert res12 == exp1, "failure in handling empty elements"

    test2 = [1, 2, [3], [4, 5], [6, [7, [8, 9, [10, 11]]]]]
    exp2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    test21, test22 = copy.deepcopy(test2), copy.deepcopy(test2)
    res21 = flattens_iterative(test21)
    res22 = flattens_recursive(test22)
    assert res22 == exp2, "failure in multi-layer elements"
    assert res21 == exp2, "failure in multi-layer elements"

    test3 = [1, 2, []]
    exp3 = [1, 2]
    test31, test32 = copy.deepcopy(test3), copy.deepcopy(test3)
    res31 = flattens_iterative(test32)
    res32 = flattens_recursive(test31)
    assert res31 == exp3, "failure in handling nested empty elements"
    assert res32 == exp3, "failure in handling nested empty elements"

    test4 = [1, 2, 3, 4]
    test4[0] = test4
    exp4 = [2, 3, 4]
    test41, test42 = copy.deepcopy(test4), copy.deepcopy(test4)
    res41 = flattens_iterative(test41)
    res42 = flattens_recursive(test42)
    assert res41 == exp4, "failure in handling recursive elements"
    assert res42 == exp4, "failure in handling recursive elements"

    test5 = [1, 2, 3, 4]
    test5[1] = test5
    exp5 = [1, 3, 4]
    test51, test52 = copy.deepcopy(test5), copy.deepcopy(test5)
    res51 = flattens_iterative(test51)
    res52 = flattens_recursive(test52)
    assert res51 == exp5, "failure in handling recursive elements"
    assert res52 == exp5, "failure in handling recursive elements"

    test6 = [1, 2, 3, 4, 3, 6]
    test6[0] = test6
    exp6 = [2, 3, 4, 3, 6]
    test61, test62 = copy.deepcopy(test6), copy.deepcopy(test6)
    res61 = flattens_iterative(test61)
    res62 = flattens_recursive(test62)
    assert res61 == exp6, "failure in handling duplicate elements"
    assert res62 == exp6, "failure in handling duplicate elements"

    print("overall success")


if __name__ == "__main__": 
    main()