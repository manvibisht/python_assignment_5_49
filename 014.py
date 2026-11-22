user_text = input("Enter text to save in file: ")
with open("user_note.txt", "w") as f:
    f.write(user_text)
print("Saved to user_note.txt.")