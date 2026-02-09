n = int(input())
sum_odd = 0
for i in range(1, n + 1):
    x = i
    while x % 2 == 0:
        x //= 2
    sum_odd += x
print(sum_odd)



