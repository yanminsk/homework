my_digit=int(input("Введите число: "))
text=""
for i in range(2,my_digit+1):
    if i % 2 == 0:
        text = text+str(i) + " "
        if text.count(" ")==5:
            print(text)
            text=""
# print(text)
