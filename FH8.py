import json
with open (r"C:\Users\mailr\Downloads\New document 1.json","r") as jf:
    data = json.load(jf)
    print(*data)
