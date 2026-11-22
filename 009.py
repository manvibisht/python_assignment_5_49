with open("sample.txt", "w") as f:
    f.write("I love Python\nJava is compiled\nPython is interpreted\n")

target = "Python"
with open("sample.txt", "r") as f:
    for line in f:
        if target in line:
            print(line.strip())