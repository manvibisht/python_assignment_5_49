with open("demo.txt", "w") as f:
    f.write("Hello World")

with open("demo.txt", "r+") as f:
    print("Before:", f.read())
    f.seek(0)
    f.write("Python")