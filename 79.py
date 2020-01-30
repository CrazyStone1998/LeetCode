class Solution:
    def exist(self, board, word: str) -> bool:
        x = len(board)
        y = len(board[0])

        def dfs_search(i, j, loc, word):
            if len(word) == 0:
                return True
            if i > 0 and board[i - 1][j] == word[0] and (i - 1, j) not in loc:
                loc.append((i - 1, j))
                if dfs_search(i - 1, j, loc, word[1:]):
                    return True
                loc.pop()
            if i + 1 < x and board[i + 1][j] == word[0] and (i + 1, j) not in loc:
                loc.append((i + 1, j))
                if dfs_search(i + 1, j, loc, word[1:]):
                    return True
                loc.pop()
            if j > 0 and board[i][j - 1] == word[0] and (i, j - 1) not in loc:
                loc.append((i, j - 1))
                if dfs_search(i, j - 1, loc, word[1:]):
                    return True
                loc.pop()
            if j + 1 < y and board[i][j + 1] == word[0] and (i, j + 1) not in loc:
                loc.append((i, j + 1))
                if dfs_search(i, j + 1, loc, word[1:]):
                    return True
                loc.pop()

            return False

        for i in range(x):
            for j in range(y):
                loc = []
                if board[i][j] == word[0]:
                    loc.append((i, j))
                    if dfs_search(i, j, loc, word[1:]):
                        return True
        return False


print(Solution().exist([["C", "A", "A"],
                        ["A", "A", "A"],
                        ["B", "C", "D"]], "AAB"))
