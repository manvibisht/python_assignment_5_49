students = ["Manvi", "Aarav", "Riya", "Kabir", "Ananya"]
with open("students.txt", "w") as f:
    for name in students:
        f.write(name + "\n")
print("Student names written.")