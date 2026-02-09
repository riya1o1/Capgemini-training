age = int(input("Enter age: "))
show_time = float(input("Enter show timing: "))
if show_time == 13.30:
    price = 1
else:
    if age >= 13:
        price = 2
    else:
        price = 2
print(f"Ticket Price: ${price}")
