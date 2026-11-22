with open("sample.txt", "w") as f:
    f.write("Python is easy to learn and powerful.")

with open("sample.txt", "r") as f:
    words = f.read().split()
    print("Total words:", len(words))