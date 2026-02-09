data = b'\x00\x01\x02\x03\x04'
with open("file.bin","wb") as f:
    f.write(data)
with open("file.bin","rb") as f:
    print(f.read())
