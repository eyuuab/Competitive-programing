class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0

        for row in matrix:
            for col in range(1, cols):
                row[col] += row[col - 1]

        for col1 in range(cols):
            for col2 in range(col1, cols):
                prefix_sums = defaultdict(int)
                prefix_sums[0] = 1
                current_sum = 0

                for row in range(rows):
                    if col1 > 0:
                        current_sum += matrix[row][col2] - matrix[row][col1 - 1]
                    else:
                        current_sum += matrix[row][col2]

                    if current_sum - target in prefix_sums:
                        count += prefix_sums[current_sum - target]

                    prefix_sums[current_sum] += 1

        return count