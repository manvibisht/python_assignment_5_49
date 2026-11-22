with open("sample.txt", "w") as f:
    f.write("Programming in Python")

with open("sample.txt", "r") as f:
    text = f.read().lower()
    vowels = sum(1 for ch in text if ch in "aeiou")
    print("Vowel count:", vowels)