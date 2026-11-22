with open("sample.txt", "w") as f:
    f.write("Room #101 @ Dehradun-248001!")

with open("sample.txt", "r") as f:
    text = f.read()
    digits = sum(1 for ch in text if ch.isdigit())
    special = sum(1 for ch in text if not ch.isalnum() and not ch.isspace())
    print("Digits:", digits, "Special characters:", special)