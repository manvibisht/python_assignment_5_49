with open("sample.txt", "w") as f:
    f.write("Python Programming Language")

with open("sample.txt", "r") as f:
    print("First 10 characters:", f.read(10))