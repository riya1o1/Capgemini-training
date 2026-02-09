try:
    file = open(r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()