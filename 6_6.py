
mytxt=list(input("Введите список: "))
my_summa=[]
yu=len(mytxt)
for i in range(len(mytxt)):
    if i==0:
        k=len(mytxt)
        l=i
    elif i==len(mytxt)-1:
        k=i
        l=-1
    else: k=l=i

    my_summa.append(int(mytxt[k-1])+int(mytxt[l+1]))

print(my_summa)
