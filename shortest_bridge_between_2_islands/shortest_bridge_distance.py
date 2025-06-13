import collections


def build_bridge(board: list[list[int]]) -> int:
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    rows, cols = len(board), len(board[0])
    # enumerating first pixel for any of the 2 islands
    rf, cf = -1, -1
    for idx in range(rows):
        for jdx in range(cols):
            if board[idx][jdx] == 0:
                continue
            rf, cf = idx, jdx
            board[rf][cf] = 2
            break
        if rf != -1 or cf != -1:
            break
    
    # using dfs shape first island, enquing every pixel of such island to queue of bridge start
    firsts = [(rf, cf)]
    departs = collections.deque([(rf, cf)])
    while firsts:
        row, col = firsts.pop()
        for rx, cx in dirs:
            rowx, colx = row + rx, col + cx
            if not 0 <= rowx < rows or not 0 <= colx < cols:
                continue
            if board[rowx][colx] == 2 or board[rowx][colx] == 0:
                continue
            board[rowx][colx] = 2
            departs.append((rowx, colx))
            firsts.append((rowx, colx))
    
    # using bfs departing from first island, finding any traceof the second island
    conn = 0
    while departs:
        for _ in range(len(departs)):
            row, col = departs.popleft()
            for rx, cx in dirs:
                rowx, colx = row + rx, col + cx
                if not 0 <= rowx < rows or not 0 <= colx < cols:
                    continue
                if board[rowx][colx] == 2:
                    continue
                if board[rowx][colx] == 1:
                    return conn
                departs.append((rowx, colx))
                board[rowx][colx] = 2
        conn += 1
    # never happen but just in case sth wrong we shall know
    return -1
    