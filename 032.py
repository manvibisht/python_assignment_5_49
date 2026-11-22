with open("sample.txt", "w") as f:
    f.write("Python Programming 2026")

with open("sample.txt", "r") as f:
    text = f.read()
    upper = sum(1 for ch in text if ch.isupper())
    lower = sum(1 for ch in text if ch.islower())
    print("Uppercase:", upper, "Lowercase:", lower)