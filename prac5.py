N = int(input("Enter the size of array : "))
B = list(map(int,input("Enter the elements : ").split()))
mul = 1
for i in B:
    if i%7==0:
        mul*=i
print(mul)