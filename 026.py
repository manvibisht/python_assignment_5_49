with open("demo.txt", "a+") as f:
    f.write("\nLine added in a+ mode")
    f.seek(0)
    print(f.read())