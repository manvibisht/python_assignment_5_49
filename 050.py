import os

filename = "lifecycle.txt"
f = open(filename, "w")
f.write("Temporary lifecycle data.")
f.close()

f = open(filename, "r")
print("Read data:", f.read())
f.close()

os.remove(filename)
print(f"'{filename}' deleted successfully.")
