number=input("Введите числа : ").strip()
number=number.split()
sum_number=0
for i in range(len(number)):
    sum_number+=int(number[i])
print("Среднее арифмитическое = ",round(sum_number/len(number),3))