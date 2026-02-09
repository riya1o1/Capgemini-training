n = int(input("Enter the size of array : "))
A = list(map(int, input("Enter the elements : ").split()))
m = max(A)
print(m * A.count(m))
