"""
Problem Statement -
Given a matrix of size n*m, where each position is representing a city.
Initially all city are represented by zero. ( means they are not traversible ).
On each day one city will randomly become traversible. ( matrix[i][j] = 1 )

Write an algorithm that can detect when there is a path from any city of first column to any city of last column.
"""


def solve(A) -> bool:
    n, m = map(len, (A, A[0]))
    vis = [[0 for _ in range(m)] for _ in range(n)]
    q = [(0, i) for i, x in enumerate(A[0]) if x]
    dirs = [(0, 1), (-1, 1), (1, 1)]
    for x, y in q:
        vis[x][y] = 1
    while q:
        x, y = q.pop(0)
        if y == n - 1:
            return True
        for dx, dy in dirs:
            x_new, y_new = x + dx, y + dy
            if 0 <= x_new < n and 0 <= y_new < m:
                if A[x_new][y_new] and not vis[x_new][y_new]:
                    q.append((x_new, y_new))
                    vis[x_new][y_new] = 1
    return False
