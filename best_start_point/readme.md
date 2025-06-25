# Best Start in Board to Targets

## Description

1. Choosing an optimal start point in the given `board` which is bounded by walls (`#`), satisfying lowest cost to all `targets` which each also lies within the same `board`, briefing with example below:

    ```Python3[]
        board = [['#','#','#','#','#','#','#','#','#'],
                ['#',' ','#',' ',' ','#','#',' ','#'],
                ['#',' ',' ','#',' ','#','#',' ','#'],
                ['#',' ',' ','#',' ',' ','#',' ','#'],
                ['#',' ',' ',' ','#',' ','#',' ','#'],
                ['#',' ',' ',' ',' ',' ',' ',' ','#'],
                ['#',' ',' ',' ',' ','#','#','#','#'],
                ['#','#','#','#','#','#','#','#','#']]

        targets = [[1, 1], [5, 4], [2, 7]]
    ```

2. Implementing the `choose_start()` function, returning any of the most optimal starts in `[x, y]` foramt

## Inspiration

### How to optimize for path exploration? How to efficiently know all costs from start to target?

1. Departuring from all void coordinates in `board1` and performing BFS from those starts are acceptable but costful even with memorization

2. Departuring from all targets and memorizing costs to all voids could be an alternative approach
