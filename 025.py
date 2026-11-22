with open("demo.txt", "w+") as f:
    f.write("Written in w+ mode")
    f.seek(0)
    print("Read back:", f.read())