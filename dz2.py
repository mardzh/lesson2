total_sum = [(15*3), (15/3), (15//2), (15**2)]
print(total_sum)
for el in total_sum:
    print(type(el))
# задание 2, понимаю что намудрила, но не знаю как короче
text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 0
for i in range(0, len(text) - 1, 1):
    for ch in text[i + count]:
        if ('0' <= ch <= '9' or ch == '+'):
            text.insert(i + count, '"')
            count += 1
            if (ch == '+'):
                text[i + count] = '{0}{1:02d}'.format(ch, int(text[i + count]))
            else:
                text[i + count] = '{0:02d}'.format(int(text[i + count]))
            text.insert(i + count + 1, '"')
            count += 1
            break
out = ""
add_space = True
for i in text:
    if(i == '"'):
        add_space = ~add_space

    if(add_space == True):
        out += i + ' '
    else:
        out += i
print(out)

# задание 3
a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in a:
    print('Привет,',i.split()[-1].title(),"!")

# задание 4
price = [7.50, 15.25, 45.60, 70.05, 55.89, 54.56, 23.88, 67.30, 90.50, 20.45]
out = ""
for el in price:
    #out += '{0} {1} {2} {3}'.format(int(el), 'руб','{:02d}'.format(((el - int(el))*100).__round__()), 'коп, ')
    out += f'{int(el):02d} руб {round((int(el) - int(el))*100)} коп, '
print(out)





