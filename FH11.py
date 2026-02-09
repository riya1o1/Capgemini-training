try:
    with open (r"C:\Users\mailr\OneDrive\Desktop\Notepad.txt", "x", encoding="utf-8") as f:
        f.write("Creaded using exclusive modes")
except:
    print("Notepad.txt already exists, exclusive creation abroad")
