mytxt=list(input("Введите список: "))
smestit=input("Введите на сколько смещать: ")

for i in range(int(smestit)):
    mytxt.insert(i,mytxt.pop(len(mytxt)-1))

print(mytxt)
