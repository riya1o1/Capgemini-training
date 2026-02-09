f = open(r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r")
for line in f:
    print(line.strip())
f.close()
