print("Hello, world!")
with open("output.txt", "w") as f:
    print("Hello, world!", file=f)
