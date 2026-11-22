with open("sample.txt", "w") as f:
    f.write("First Line\nSecond Line\nThird Line\n")

with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()