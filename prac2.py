N = int(input("Enter the number of seats in a row : "))
A = list(map(int,input("Enter the values : ").split()))
count = 0
for i in A:
    if i == 0:
        count += 1
print(count)