mytxt=list(input("Введите список: "))

for i in range(len(mytxt)):
    mytxt.insert(i,mytxt.pop(len(mytxt)-1))

print(mytxt)