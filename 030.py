f = open("demo.txt", "w")
print("Is file closed before close()?:", f.closed)
f.close()
print("Is file closed after close()? :", f.closed)