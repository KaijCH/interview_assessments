import collections
import math


class Solution:    

    def retrack(self, rowt: int, colt: int) -> None:
        queue = collections.deque([(rowt, colt, 0)])
        visits = {(rowt, colt)}
        while queue:
            row, col, val = queue.popleft()
            for rx, cx in self.opts:
                rowx, colx = row + rx, col + cx
                if not 0 <= rowx  < self.rows or not 0 <= colx < self.cols: 
                    continue
                if self.board[rowx][colx] == "#":
                    continue
                curr = (rowx, colx)
                if curr  in visits:
                    continue
                visits.add(curr)
                self.visits[rowx][colx] += 1
                self.dists[rowx][colx] += val
                queue.append((rowx, colx, val + 1))

    def choose_start(self, board: list[list[str]], targets: list[list[int]]) -> list:
        self.rows, self.cols = len(board), len(board[0])
        self.board, self.targets = board, targets
        self.opts = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        visits = len(targets)

        if not self.rows or not self.cols: return []

        self.visits = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.dists = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for rowt, colt in self.targets:
            self.retrack(rowt, colt)
        
        minima, start = math.inf, [-1, -1]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.visits[row][col] != visits: 
                    continue
                if minima <= self.dists[row][col] :
                    continue
                minima = self.dists[row][col]
                start = [row, col]
        return start

