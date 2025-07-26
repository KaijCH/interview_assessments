from largest_k_number import find_number


def main():
    
    input1, k1 = "3 2", 2
    n1 = find_number(input1, k1)
    assert n1 == 2, "failure in returning the k largest result"

    input2, k2 = "3 2 323", 2
    n2 = find_number(input2, k2)
    assert n2 == 3, "failure in splitting numbers from input"

    input3, k3 = "3 2e 323", 1
    n3 = find_number(input3, k3)
    assert n3 == 323, "failure in recognizing number from input"

    input4, k4 = "3 e", 2
    n4 = find_number(input4, k4)
    assert n4 == -1, "failure in handling over large k order"

    input5, k5 = "3, e2, 1", 2
    n5 = find_number(input5, k5)
    assert n5 == -1, "failure in splitting number from input"

    input6, k6 = "31 20 11 1221", 10
    n6 = find_number(input6, k6)
    assert n6 == -1, "failure in returning the k largest result"


    print("Overall Success")


if __name__ == "__main__":
    main()
    