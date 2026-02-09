def close_account(balance):
    try:
        if balance != 0:
            raise Exception("Account has pending balance.")
        print("Account closed.")
    except Exception as e:
        raise
try:
    bal = float(input("Enter account balance: "))
    close_account(bal)
except Exception as e:
    print(e)

