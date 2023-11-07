number=input("Введите числа: ").strip()
number=number.split()
negativ=0
positiv=0
zero=0
vsego_digit=0
for i in range(len(number)):
    if number[i].isalpha()==False :
      vsego_digit += 1
      if number[i][0]=="-": negativ+=1
      else:
        if number[i][0] == "0": zero +=1
        else: positiv+=1

print("Введено "+str(vsego_digit)+" цифр, из них отрицательных "+str(negativ)+", положительных "+str(positiv)+", нулей "+str(zero))
