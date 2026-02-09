H = int(input("Enter initial height : "))
V = int(input("Enter initial volume : "))
Vn = int(input("Enter final velocity : "))
e = V / Vn
rebound_height = int(H * (e ** 2))
print(rebound_height)
