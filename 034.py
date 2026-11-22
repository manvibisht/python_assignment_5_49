with open("sample.txt", "w") as f:
    f.write("Python is great. I enjoy coding in Python. Python rocks!")

word = "Python"
with open("sample.txt", "r") as f:
    words = [w.strip(".,!?") for w in f.read().split()]
    print(f"Occurrences of '{word}':", words.count(word))