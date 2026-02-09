lines = ['Line A','Line B','Line C']
text = "\n".join(lines) + "\n"
with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "w", encoding="utf-8") as f:
        f.write(text)
with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r", encoding="utf-8") as f:
        print(f.read())