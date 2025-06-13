from shortest_bridge_distance import build_bridge

def main() -> None:
    board1 = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    length1 = build_bridge(board1)
    res1 = 1
    assert length1 == res1, "failure in handling surrounded case"

    board1 = [[1,0], [0,1]]
    length1 = build_bridge(board1)
    res1 = 1
    assert length1 == res1, "failure in handling single pixel islands"


    print("overall success")


if __name__ == "__main__":
    main()