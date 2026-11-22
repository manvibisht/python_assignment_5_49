with open("demo.txt", "w") as f:
    f.write("0123456789ABCDEF")

pos = int(input("Enter starting byte position: "))
with open("demo.txt", "r") as f:
    f.seek(pos)
    print("Content from position:", f.read())