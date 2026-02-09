n = int(input())
A = list(map(int, input().split()))
summit = A[0]
for i in range(1, n):
    if A[i] > summit:
        summit = A[i]
print(summit)
