with open("demo.txt", "w") as f:
    f.write("Python Programming")

with open("demo.txt", "r") as f:
    f.seek(7)
    print("From index 7:", f.read())