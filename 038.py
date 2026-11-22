with open("input.txt", "w") as f:
    f.write("Convert this text to uppercase.")

with open("input.txt", "r") as src, open("output_upper.txt", "w") as dst:
    dst.write(src.read().upper())
print("Converted file written to output_upper.txt.")