class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map_r = {}
        map_c = {}
        map_squr = {}

        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    r = row // 3
                    c = col // 3
                    key_s = (r, c, board[row][col])
                    key_r = (row, board[row][col])
                    key_c = (col, board[row][col])

                    map_squr[key_s] = map_squr.get(key_s, 0) + 1
                    if map_squr[key_s] >= 2:
                        print('squ')
                        print(board[row][col])
                        return False
                        

                    map_r[key_r] = map_r.get(key_r, 0) + 1
                    if map_r[key_r] >= 2:
                        print(board[row][col])
                        print('squ')
                        return False
                        
                    map_c[key_c] = map_c.get(key_c, 0) + 1
                    if map_c[key_c] >= 2:
                        print('squ')
                        return False
                    
        return True