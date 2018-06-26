#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, io

sys.stdin = io.StringIO(u'''5 6
1 0 0 1 0 0
0 0 1 0 1 0
1 1 1 1 1 0
1 0 0 1 1 1
1 1 1 1 1 1
''')

import sys


def maxAreaOfIsland0(grid):
    return sum([sum(g) for g in grid])

def maxAreaOfIsland(grid):
    seen = set()

    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r + 1, c) + area(r - 1, c) +
                area(r, c - 1) + area(r, c + 1))

    return max(area(r, c)
               for r in range(len(grid))
               for c in range(len(grid[0])))


its = int(sys.stdin.readline().strip()[0])
grid = []
for _ in range(its):
    ai = sys.stdin.readline().strip()
    grid.append([int(i) for i in ai.split()])
# print(grid)
print(maxAreaOfIsland(grid))
