with open("file1.txt", "w") as f1:
    f1.write("Content from File 1.\n")
with open("file2.txt", "w") as f2:
    f2.write("Content from File 2.\n")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    out.write(f1.read() + f2.read())
print("Files merged into merged.txt.")