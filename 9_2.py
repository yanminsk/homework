# Дан CSV файл с колонками: article, name, description, price - описание товаров.
# Необходимо прочитать файл в список словарей с ключами взятых из первой строки (названия колонок)
# без использования встроенной библиотеки CSV

file = open(file="file.csv", mode="r+")
key_number=0
my_new_dict={}
my_list=[]
rez_list=[]
for line in file:
    my_list=line.strip().strip("\n").split(",")
    if key_number==0:
        first_key=my_list[0]
        second_key=my_list[1]
        third_key=my_list[2]
        four_key=my_list[3]
        key_number+=1
    else:
         my_list = line.strip().strip("\n").split(",")
         my_new_dict[first_key]=my_list[0]
         my_new_dict[second_key]=my_list[1]
         my_new_dict[third_key]=my_list[2]
         my_new_dict[four_key]=my_list[3]
         rez_list.append(my_new_dict)
         print(my_new_dict)
         print(rez_list)
         # print(rez_list)
         # key_number += 1
print(rez_list)