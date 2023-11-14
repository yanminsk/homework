my_string=input("Введите текст:")
my_spisok=list(my_string)
my_dict={i: my_string.count(i) for i in my_string}
print(my_dict)
#
# my_string=input("Введите текст:")
# my_dict={}
# my_dict={i: int(my_dict.get(i,0))+1 for i in my_string}
# print(my_dict)