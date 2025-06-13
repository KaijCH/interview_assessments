# Shortest Bridge Between 2 Islands

## Description

1. Implementing `build_bridge` to measure shortest bridge between exactly 2 islands on the given map board (0 represents water and 1 represents land)

2. Knowing that any single island is group of 4-directional connected `1`s meanwhile 2 islands are not connecting to each other

3. `2 < len(board) == len(board[0]) < 100`

4. `board[i][j] in {0, 1}`

## Inspriation

### How to distinguish different islands, where to start exploration of bridge

0. Using the given condition says 2 islands are not connecting to each other

1. Enumerating entire map board for the first land cell (`board[i][j] == 1`), furthering the exploration on other cells (also with board val == 1) connect with that cell to form the entire shape of the first island

2. Marking cells after visit with different value like `2` for distinguishment between cell in first island and the potential new cell for the new island

3. Departuring from all found cell in the found first siland using BFS since it is optimal for shortest path problem
