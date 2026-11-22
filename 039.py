with open("input.txt", "w") as f:
    f.write("Reverse me!")

with open("input.txt", "r") as src, open("output_rev.txt", "w") as dst:
    dst.write(src.read()[::-1])
print("Reversed file written to output_rev.txt.")