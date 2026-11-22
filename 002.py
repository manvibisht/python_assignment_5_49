with open("sample.txt", "w") as f:
    f.write("Line 1: Python\nLine 2: File Handling\n")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)