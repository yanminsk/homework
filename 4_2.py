# my_string=input("Введите текст:")
# my_spisok=list(my_string)
# my_dict={i: my_spisok.count(i) for i in my_string}
# print(my_dict)

my_string=input("Введите текст:")
# my_spisok=list(my_string)
my_dict={}
my_dict={i: int(my_dict.get(i,0))+1 for i in my_string}
print(my_dict)