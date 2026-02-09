N = int(input("Enter total no.of problems : "))
P = int(input("Enter the time to travel from home to party : "))
time_left = 240 - P
time_used = 0
count = 0
for i in range(1, N + 1):
    if time_used + 5 * i <= time_left:
        time_used += 5 * i
        count += 1
    else:
        break
print(count)
