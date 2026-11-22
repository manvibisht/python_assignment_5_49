import os
with open("old_name.txt", "w") as f:
    f.write("Sample content")

if os.path.exists("new_name.txt"):
    os.remove("new_name.txt")
os.rename("old_name.txt", "new_name.txt")
print("File renamed to new_name.txt.")