# Перевод двоичного числа в десятичное
def my_bin(a):
    b=0
    for i in range(len(a)) :
         b+=2 ** i*int(a[len(a)-1-i:len(a)-i:1])
    return b

number=input("Введите двоичное число: ")
print(f"Десятичное число: "+str(my_bin(number)))
