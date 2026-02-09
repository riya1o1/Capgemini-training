n = int(input("Enter the number:"))
pos = int(input("Enter the position:"))
for i in range(1,pos):
    n //= 10
if n==0 :
    print(-1)
else:
    print(n%10)