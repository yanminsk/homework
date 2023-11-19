
mytxt=list(input("Введите список: "))
result = list(filter(lambda x: not x.isalpha(), mytxt))
for i in result:
    mytxt.remove(i)
print(mytxt)