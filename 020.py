with open("numbers_100.txt", "w") as f:
    for i in range(1, 101):
        f.write(str(i) + "\n")
print("First 100 natural numbers saved.")