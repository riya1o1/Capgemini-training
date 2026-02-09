N = int(input("Enter the count of reserved room : "))
A = list(map(int, input("Enter the vaules : ").split()))
T = int(input("Enter total no.of rooms : "))
result = T - N
print(result)