class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] != word[index]:
                return False
            
            visited.add((row, col))
            
            if dfs(row - 1, col, index + 1) or dfs(row + 1, col, index + 1) \
                or dfs(row, col - 1, index + 1) or dfs(row, col + 1, index + 1):
                return True
            
            visited.remove((row, col))
            
            return False
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False
