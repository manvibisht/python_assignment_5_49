with open("demo.txt", "w") as f:
    f.write("Reading in 'r' mode.")

f = open("demo.txt", "r")
print(f.read())
f.close()
