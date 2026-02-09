n = int(input("Enter size : "))
arr = list(map(int, input("Enter elements : ").split()))
def Sum (arr,n):
    if n==0:
        return 0
    return arr[n - 1] + Sum(arr, n - 1)
print(Sum(arr, n))
