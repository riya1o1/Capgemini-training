current_year = int(input("Enter year: "))
next_year = current_year + 1
while True:
    if (current_year % 400 == 0) or (current_year % 4 == 0 and current_year % 100 != 0):
        print ("The next leap year:",current_year)
        break
    if (next_year % 400 == 0) or (next_year % 4 == 0 and next_year % 100 != 0):
        print("The next leap year:",next_year)
        break
    next_year += 1