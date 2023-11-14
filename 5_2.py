try:
    first_digit=int(input("Введите первое число: "))
    arithmetic=input("Введите арифметическую операцию вида (+ - / * % ^): ")
    second_digit=int(input("Введите второе число: "))
except ValueError as e:
    print(f"Ошибка с типом {e}")

result=0

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