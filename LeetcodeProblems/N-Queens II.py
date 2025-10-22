class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # row + col
        diag2 = [False] * (2 * n - 1)  # row - col + n - 1

        def dfs(row: int) -> None:
            if row == n:
                self.ans += 1
                return

            for col in range(n):
                d1_idx = row + col
                d2_idx = row - col + n - 1

                if cols[col] or diag1[d1_idx] or diag2[d2_idx]:
                    continue

                cols[col] = True
                diag1[d1_idx] = True
                diag2[d2_idx] = True

                dfs(row + 1)

                # Backtrack
                cols[col] = False
                diag1[d1_idx] = False
                diag2[d2_idx] = False

        dfs(0)
        return self.ans
