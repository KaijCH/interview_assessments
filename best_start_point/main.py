from select_start import Solution


def main() -> None:
    sol = Solution()
    board, targets  = [['#','#','#','#','#','#','#','#','#'],
                       ['#',' ','#',' ',' ','#','#',' ','#'],
                       ['#',' ',' ','#',' ','#','#',' ','#'],
                       ['#',' ',' ','#',' ',' ','#',' ','#'],
                       ['#',' ',' ',' ','#',' ','#',' ','#'],
                       ['#',' ',' ',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ','#','#','#','#'],
                       ['#','#','#','#','#','#','#','#','#']], [[1, 1], [5, 4], [2, 7]]
    res = sol.choose_start(board, targets)
    assert res in [[5,3],[5,2], [5,4]], "failure in yeilding optimal start"

    board, targets = [['#', '#', '#', '#', '#'],
                      ['#', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', ' ', '#'],
                      ['#', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', '#']], [[1, 1], [1, 3], [3, 3]]
    res = sol.choose_start(board, targets)
    assert res in [[1,2], [1,1], [1,3], [3,3], [2,3]], "failure in yeilding from single path"

    board ,targets = [['#', '#', '#'],
                      ['#', ' ', '#'],
                      ['#', '#', '#']], [[1, 1]]
    res = sol.choose_start(board, targets)
    assert res in [[1, 1]], "failure in yeilding start from non-walkable place except target"


    board ,targets = [['#', '#', '#', '#', '#', '#', '#', '#'],
                      ['#', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                      ['#', ' ', '#', '#', '#', '#', ' ', '#'],
                      ['#', ' ', '#', ' ', ' ', '#', ' ', '#'],
                      ['#', ' ', '#', '#', '#', '#', ' ', '#'],
                      ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                      ['#', '#', '#', '#', '#', '#', '#', '#']], [[0, 0], [2, 2], [0, 2]]
    res = sol.choose_start(board, targets)
    assert res in [[-1, -1]], "failure in yeilding from none reach-able targets"


    print("overall success")


if __name__ == "__main__":
    main()