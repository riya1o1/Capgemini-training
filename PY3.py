n = int(input())
m = list(map(int, input().split()))
for i in range (n-1):
    print(m[i+1] - m[i] ,end =" ")