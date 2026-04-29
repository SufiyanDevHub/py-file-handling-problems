
words = ["Donkey","Monkey","Lion"]
with open("file.txt") as f:
    data = f.read()
    # print(data)
for word in words:
    data = data.replace(word,"#"*len(word))
        

with open ("file.txt","w") as f:
    f.write(data)
