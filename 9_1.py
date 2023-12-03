# Дан файл с многострочным текстом, необходимо подсчитать количество букв в каждой
# строке и результат записать в другой файл в формате:
# 1 строка - N букв
# 2 строка - M букв

file = open(file="file.txt", mode="r+")
my_file_lines=file.readlines()
my_txt=""
for i in range(len(my_file_lines)):
    my_txt+=str(i+1)+f" строка - "+str(len(my_file_lines[i])-1)+" символа(ов)\n"
file.close()
file2 = open(file="file2.txt", mode="w+", encoding="UTF-8")
file2.write(my_txt)
file2.close()
