user_fio=input("Введите Имя: ").strip().lower()
while user_fio.isalpha()==False:
    user_fio = input("НЕВЕРНЫЙ ФОРМАТ ВВОДА. В ИМЕНИ НЕ ДОЛЖНО БЫТЬ ЦИФР И ПРОБЕЛОВ\nВведите Имя: ").strip()

user_age=input("Введите свой возраст: ").strip()
while user_age.isnumeric()==False:
    user_age = input("НЕВЕРНЫЙ ФОРМАТ ВВОДА.В ВОЗРАСТЕ НЕ ДОЛЖНО БЫТЬ БУКВ И ПРОБЕЛОВ\nВведите свой возраст: ").strip()

user_city=input("Введите ваш город: ").strip().lower()
while user_city.isidentifier()==False:
    user_city = input("НЕВЕРНЫЙ ФОРМАТ ВВОДА.В НАЗВАНИИ ГОРОДА НЕ ДОЛЖНО БЫТЬ ЦИФР И ПРОБЕЛОВ\nВведите ваш город: ").strip()

result="Приветствуем тебя %s летний %s из города %s" % (user_age, user_fio.capitalize(), user_city.capitalize())
print(result)
result="Приветствуем тебя {} летний {} из города {}".format (user_age, user_fio.capitalize(), user_city.capitalize())
print(result)
result=f"Приветствуем тебя {user_age} летний {user_fio.capitalize()} из города {user_city.capitalize()}"
print(result)