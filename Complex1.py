str = input()
lst = []

# Всё в while потому что функции мы еще не проходили
while str != 'Close':
    # Проверяем на то, что к нам поступает задача вписать или удалить число
    if len(str.split(' ')) == 2:
        num = str.split(' ')[1]
        # Траем проверяем на число
        try:
            check = float(num)
            if str.find('PushEnd') > -1:                # >-1 Потому что если find не находит значение, то возвращает -1
                lst.append(num)
                print(lst)
            elif str.find('PushFirst') > -1:
                lst.insert(0, num)
                print(lst)
            elif str.find('Rem') > -1:
                if num in lst:
                    lst.remove(num)
                    print(lst)
                else:
                    print('Такого числа нет')
        except:
            print('Вписывать только числа')
    elif str.find('RemEnd') > -1:
        print(lst[-1])
        lst.pop()
    elif str.find('RemFirst') > -1:
        print(lst[0])
        lst.pop(0)
    elif str.find('Size') > -1:
        print(len(lst))
    elif str.find('Clear') > -1:
        lst.clear()
        print(lst)
    str = input()
print('Пока!')