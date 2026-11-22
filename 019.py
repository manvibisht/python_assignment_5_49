num = int(input("Enter a number: "))
with open("table.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{num} x {i} = {num * i}\n")
print("Multiplication table saved to table.txt.")