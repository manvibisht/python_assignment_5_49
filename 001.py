with open("sample.txt", "w") as f:
    f.write("Hello Python File Handling!\nWelcome to Assignment 5.")

f = open("sample.txt", "r")
print(f.read())
f.close()