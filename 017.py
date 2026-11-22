with open("source.txt", "w") as f:
    f.write("Data to be copied.")

with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
    dst.write(src.read())
print("File copied successfully.")