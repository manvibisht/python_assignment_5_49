with open("demo.txt", "w") as f:
    f.write("Python File Pointer")

with open("demo.txt", "r") as f:
    f.read(6)
    print("Current pointer position:", f.tell())