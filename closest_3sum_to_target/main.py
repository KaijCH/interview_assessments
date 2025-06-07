from closest_triplets import finds_triplets


def validates(exp: list, res: list) -> bool:
    return sorted(sorted(exp)) == sorted(sorted(res))


def main() -> None:
    nums1, target1 = [1, 2, 3], 6
    expt1 = [[1, 2, 3]]
    res1 = finds_triplets(nums1, target1)
    assert validates(expt1, res1) == True, "failure in handing 3 input elements"

    nums2, target2 = [1, 2, 3], 20
    expt2 = [[1, 2, 3]]
    res2 = finds_triplets(nums2, target2)
    assert validates(expt2, res2) == True, "failure in handing closest match"

    nums3, target3 = [9, -1, 1, 1, 2, 3, 3, 20, 19, 11], -1
    expt3 = [[-1, 1, 1]]
    res3 = finds_triplets(nums3, target3)
    assert validates(expt3, res3) == True, "failure in handing closest match with negative elements"

    nums4, target4 = [1, 2, 3, -1, 8, -1, 19], 6
    expt4 = [[1, 2, 3], [-1, -1, 8]]
    res4 = finds_triplets(nums4, target4)
    
    assert validates(expt4, res4) == True, "failure in handing multi-results"
    

    print("overall success")


if __name__ == "__main__":
    main()