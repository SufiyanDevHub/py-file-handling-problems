f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("Twinkle is present in your txt file")
else:
    print("TWinkle is not present in your txt file")

f.close()