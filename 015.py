with open("notes.txt", "w") as f:
    f.write("Initial content.\n")

with open("notes.txt", "a") as f:
    f.write("Appended content.\n")

with open("notes.txt", "r") as f:
    print(f.read())