s = input("Enter the statement : ")
def count(s, i=0, alpha=0, digit=0):
    if i == len(s):
        return alpha, digit
    if s[i].isalpha():
        alpha += 1
    elif s[i].isdigit():
        digit += 1
    return count(s, i + 1, alpha, digit)
a, d = count(s)
print("Total alphabetic characters : ",a)
print("Total numeric characters : ",d)
print("total alphanumeric characters : ", a+d)
