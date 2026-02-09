n = int(input())
arr = list(map(int, input().split()))
m = list(set(arr))
m.sort(reverse = True)
second_largest = m[1]
count = arr.count(second_largest)
print(count)
