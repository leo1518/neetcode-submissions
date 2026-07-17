class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in hashmap:
                    hashmap[board[row][col]] = []
                hashmap[board[row][col]].append([row,col])
        for positions in hashmap.values():
                    n = len(positions)
                    for i in range(n):
                        r1, c1 = positions[i]
                        for j in range(i + 1, n):
                            r2, c2 = positions[j]
                            if r1 == r2:
                                return False

                            # 同一列
                            if c1 == c2:
                                return False

                            # 同一个3×3宫
                            if r1 // 3 == r2 // 3 and c1 // 3 == c2 // 3:
                                return False

        return True
                