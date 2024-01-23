def count_islands(matrix):
    def dfs(row, col):
        if row < 0 or row >= m or col < 0 or col >= n or matrix[row][col] == 0:
            return
        matrix[row][col] = 0  # Mark the cell as visited

        # Explore adjacent cells
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    island_count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                island_count += 1
                dfs(i, j)

    return island_count


# Test cases
test_case_1 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 1]
]

test_case_2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]

test_case_3 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1]
]

print(count_islands(test_case_1))
print(count_islands(test_case_2))
print(count_islands(test_case_3))
