import os
with open("size_test.txt", "w") as f:
    f.write("1234567890")

if os.path.exists("size_test.txt"):
    print("File size (bytes):", os.path.getsize("size_test.txt"))