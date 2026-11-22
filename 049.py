import os
with open("before_rename.txt", "w") as f:
    f.write("Hello after renaming!")

if os.path.exists("after_rename.txt"):
    os.remove("after_rename.txt")
os.rename("before_rename.txt", "after_rename.txt")

with open("after_rename.txt", "r") as f:
    print("Contents:", f.read())