coun_digit=int(input("Сколько выводить чисел: "))
kratno_digit=int(input("Кратно какому числу: "))
bolshe_digit=int(input("Больше какого числа: "))

for i in range(1,coun_digit+1):
    while bolshe_digit:
        bolshe_digit+=1
        if bolshe_digit%kratno_digit==0:
            print(f"{i} число: ", bolshe_digit)
            break
