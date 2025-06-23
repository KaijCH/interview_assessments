

import collections
import math


class Solution:

    def checked(self, coord: list, seen) -> x:
        for t in targest_p:
            if coord, p in cache:
                seen.add(p)
        return []

    def selects(self, grid: list[list[str]], points: list[list[int]]) -> list:
        rows, cols = len(grid), len(grid[0])
        if not rows or not cols: 
            return []
        cache = {}
        opts = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        minima = math.inf
        best = [-1, -1]
        for row in range(rows):
            for col in range(cols):
                visits = set()
                seen = set()
                queue = collections.deque()
                queue.append([row, col, 0])
                dist = 0
                while queue:
                    rowc, colc, valc = queue.popleft()
                    if [rowc, colc] in points:
                        cache[(row, col, rowc, colc)] = valc
                        dist += valc
                        seen.add((rowc, colc))
                        if len(seen) == len(points):
                            break
                    for rx, cx in opts:
                        rowx, colx = rowc+ rx, colc + cx
                        if grid[rowx][colx] == "#":
                            continue
                        if (rowx, colx) in visits:
                            continue
                        if self.checked(rowx, colx, seen) !=  -1:
                            
                        queue.append([rowx, colx, valc + 1])
                if dist < minima:
                    minima = dist
                    best = [row, col]

        return best

