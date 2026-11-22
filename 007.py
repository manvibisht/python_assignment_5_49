with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\n")

with open("sample.txt", "r") as f:
    print("Total lines:", len(f.readlines()))