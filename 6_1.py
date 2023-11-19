# Перевод десятичного числа в двоичное
def my_bin(a):
    c=""
    while int(a)>1:
         b=divmod(int(a),2)
         a=b[0]
         c+=str(b[1])

    c+=str(a)
    c=c[::-1]
    return f"0b"+c

number=input("Введите десятичное число: ")
print(f"Двоичное число: "+my_bin(number))
