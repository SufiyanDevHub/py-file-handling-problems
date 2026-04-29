# def generateTable(n):
#     table = ""

#     for i in range(1,11):
#         table = table + f"{n} x {i} = {n*i}\n"


#     print(table)
#     with open(f"tables/table_{n}","w") as f:
#         f.write(table)





# for i in range(2,21):
#     generateTable(i)

#Another way to do this program

def generateTable(n):
    with open(f"Another_T/table_{n}","w") as f:
        for i in range(1,11):
            line = f"{n} x {i} = {n*i}\n"
            f.write(line)

for i in range(2,21):
    generateTable(i)