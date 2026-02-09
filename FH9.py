with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.")
with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    