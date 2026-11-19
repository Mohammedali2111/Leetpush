class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        res = []
        r, c = rStart, cStart
        steps = 1

        while len(res) < rows * cols:

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])

                    r += dr
                    c += dc

                if dr == 1 or dr == -1:
                    steps += 1

        return res