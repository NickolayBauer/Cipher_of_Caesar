list_alpha = []
list_word = []
alpa = "абвгдеёжзийклмнопрстуфхшщыэюя"

for i in alpa:
    list_alpha.append(i)

word = input("слово: ")
key = int(input("ключ: "))
new = ''
for i in word:
    if i == ' ':
        new += i
    else:
        new += list_alpha[(list_alpha.index(i)) - key]
print(new)
