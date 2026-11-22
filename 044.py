import os
with open("temp_delete.txt", "w") as f:
    f.write("Temporary file")

if os.path.exists("temp_delete.txt"):
    os.remove("temp_delete.txt")
    print("temp_delete.txt deleted.")