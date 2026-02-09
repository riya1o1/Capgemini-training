n = int(input("Enter the size : "))
matrix = []
for i in range(n):
    r = list(map(int, input().split()))
    matrix.append(r)
for c in range(n):
    max_val = matrix[0][c]
    for r in range(1, n):
        if matrix[r][c] > max_val:
            max_val = matrix[r][c]
    print(f"Max of column {c+1}: {max_val}")