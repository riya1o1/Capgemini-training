num = int(input("Enter the integer : "))
def digits(n):
    if n < 10:
        return 1
    return 1 + digits(n // 10)
print(digits(num))
