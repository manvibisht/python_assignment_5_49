with open("sample.txt", "w") as f:
    f.write("Alpha\nBeta\nGamma\n")

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("Lines list:", lines)