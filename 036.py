with open("sample.txt", "w") as f:
    f.write("Python file handling simplifies data persistence")

with open("sample.txt", "r") as f:
    words = f.read().split()
    print("Longest word:", max(words, key=len))