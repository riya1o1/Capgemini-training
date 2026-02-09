n = int(input("Enter the jobs: "))
x = int(input("Time duration after which next job arrives: "))
current_time = 0
wait = 0
for i in range (n):
    arrival = i*x
    if arrival >= current_time:
        wait = 0
        current_time = current_time - x
    else:
        wait = current_time - arrival
        current_time += x
print(wait)
        
    