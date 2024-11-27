Написать программу, которая:

- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение


import random #подключаем библиотеку для рандомных чисел 
kol_neganive_num=0#говорим,что количество отрицательных чисел равно 0
kol_positive_num=0#говорим,что количество положительных чисел равно 0
kol_zero_num=0#говорим,что количество нулевых чисел равно 0
spisok2=[]#создаем пустой список для отрицательных чисел
spisok3=[]#создаем пустой список для положительных чисел
spisok4=[]#создаем пустой список для нулевых чисел
spisok=[(random.randint(-50,50)) for i in range(25)]#создаем список из рандомных чисел в диапазоне от -50 до 50 ,состоящий из 25 элементов с помощью генератора списков 
for i in spisok:#перебираем каждый элемент в списке "spisok"
    if i<0:#проверяем условие 
        kol_neganive_num+=1#если условие верное,то прибавляем 1 к элементу kol_neganive_num
        spisok2.append(i)#если условие верное,то добавляем элемент к спику "spisok2"
    elif i>0:#проверяем условие 
        kol_positive_num+=1#если условие верное,то прибавляем 1 к элементу kol_positive_num
        spisok3.append(i)#если условие верное,то добавляем элемент к спику "spisok3"
    else :#если ни одго условие не верное ,то
        kol_zero_num+=1#добавляем 1 к элементу kol_zero_num
        spisok4.append(i)#добавляем элемент к спику "spisok4"
pr_negatue=kol_neganive_num/25*100#находим процент отрицательных чисел от всех чисел
pr_positive=kol_positive_num/25*100#находим процент положительных чисел от всех чисел
pr_zero=kol_zero_num/25*100#находим процент нулевых чисел от всех чисел
min1=min(spisok)#находим минимальную цифру в списке всех чисел
max1=max(spisok)#находим максимальную цифру в списке всех чисел
print(f"Список со всеми числами: {spisok}")# выводим список со всеми числами
print(f"Список с отрицательными числами: {spisok2}")# выводим список с отрицательными числами
print(f"Список с положительными числами: {spisok3}")#вывоим список с положительными числами
print(f"Список с нулями: {spisok4}")#выводим список с нулями
print(f"Процент отрицательных чисел от общего количества всех чисел: {pr_negatue}")#выводим процент отрицательных чисел от общего количества всех чисел
print(f"Процент положительных чисел от общего количества всех чисел: {pr_positive}")#выводим процент положительных чисел от общего количества всех чисел
print(f"Процент нулевых чисел от общего количества всех чисел: {pr_zero}")#выводим процент нулевых чисел от общего количества всех чисел
print(f"Миннимальное значение элемента списка: {min1}")#вывоим миннимальное значение элемента списка
print(f"Максимальное значение элемента списка: {max1}")#выводим максимальное значение элемента списка
print(f"Количество отрицательных чисел: {kol_neganive_num}")#выводим количество отрицательных чисел
print(f"Количество положительных чисел: {kol_positive_num}")#выводим количество положительных чисел
print(f"Количество нулевых чисел: {kol_zero_num}")#выводим количество нулевых чисел
