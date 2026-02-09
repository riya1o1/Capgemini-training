with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")
with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r", encoding="utf-8") as f:
    print(f.read())