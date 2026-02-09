try:
    user_name = input("Enter your name: ")
    requested_tickets = int(input("Enter number of tickets required: "))
    available_seats = int(input("Enter number of available seats: "))
    if requested_tickets <= 0:
        raise Exception("Number of tickets must be positive.")
    if requested_tickets > available_seats:
        raise Exception("Requested tickets exceed available seats.")
    print(f"Booking successful for {user_name}.")
except ValueError:
    print("Invalid input.")
except Exception as e:
    print(e)
finally :
    print("Transaction completed.")