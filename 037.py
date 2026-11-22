with open("sample.txt", "w") as f:
    f.write("Apple\nBanana\nApricot\nCherry\n")

ch = "A"
with open("sample.txt", "r") as f:
    for line in f:
        if line.startswith(ch):
            print(line.strip())