try:
    first_digit=int(input("Введите первое число: "))
    arithmetic=input("Введите арифметическую операцию вида (+ - / * % ^): ")
    second_digit=int(input("Введите второе число: "))
    result=0
except ValueError as e:
    print(f"Ошибка с типом {e}")
    exit()

match arithmetic:
    case "+":
        result=first_digit+second_digit
    case "-":
         result = first_digit - second_digit
    case "/":
         result = first_digit / second_digit
    case "*":
        result = first_digit * second_digit
    case "%":
        result = first_digit % second_digit
    case "^":
        result = first_digit ** second_digit

if result: print(f"Результат операции \"{arithmetic}\" равен", result)
else: print("Неподдерживаемая операция")