
mytxt=list(input("Введите список: "))
mytxt.sort()
result = list(filter(lambda x: int(x) % 2, mytxt))
for i in result:
    mytxt.append(i)
    mytxt.remove(i)
print(mytxt)
