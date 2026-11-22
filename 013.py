lines = ["First line\n", "Second line\n", "Third line\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)
print("Lines written using writelines().")