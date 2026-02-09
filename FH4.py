f = open(r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "r")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()