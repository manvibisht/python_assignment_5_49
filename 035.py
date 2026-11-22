with open("sample.txt", "w") as f:
    f.write("Veer Madho Singh Bhandari Uttarakhand Technical University")

search_word = input("Enter word to search: ")
with open("sample.txt", "r") as f:
    if search_word in f.read():
        print(f"'{search_word}' exists in the file.")
    else:
        print(f"'{search_word}' not found.")