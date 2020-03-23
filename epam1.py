
#массив
mas = [5, 9, 2, 1, 12, 13]

#сортировка массива встроенной функцией python
mas = sorted (mas)

#результат выполнения встроенной функции сортировки 
print('Вывод после сортировки встроенной функцией Python "sort"', mas)

#массив для функции
mas2 = [5, 9, 2, 1, 12, 13]
# функция:
def sort_func(array):
    if len(array) <= 1:
        return array
    else:
        barrier = array[0] 
        l = []
        m = [] 
        r = []
        for x in array:
            if x < barrier:
                l.append(x)
            elif x == barrier:
                m.append(x)
            else:
                r.append(x)
        sort_func(l)
        sort_func(r)
        k = 0
        for x in l + m + r:
            array[k] = x
            k += 1
sort_func(mas2)
print('Вывод после сортировки функцией "sort_func" Python', mas2)