with open("mode_demo.txt", "w") as f:
    f.write("First write\n")

with open("mode_demo.txt", "w") as f:
    f.write("Overwritten by second 'w'\n")

with open("mode_demo.txt", "a") as f:
    f.write("Added by 'a' mode\n")

with open("mode_demo.txt", "r") as f:
    print(f.read())