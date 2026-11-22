with open("sample.txt", "w") as f:
    f.write("Hello World")

with open("sample.txt", "r") as f:
    text = f.read()
    print("Total characters:", len(text))