1.3 / 9
# class TravelBlog:
#     total_blogs = 0
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#         TravelBlog.total_blogs += 1
# tb1 = TravelBlog('Франция', 6)
# tb2 = TravelBlog('Италия', 5)

1.3 / 10
# class Figure:
# type = 'ellipse'
# color = 'red'
# new_attr = {
#     'start_pt': (10, 5),
#     'end_pt': (100, 20),
#     'color': 'blue'}
# fig1 = Figure()
# fig1.__dict__.update(new_attr)
# delattr(fig1, 'color')
# print(*fig1.__dict__)

1.3 / 11
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
# p1 = Person()
# print(hasattr(p1.__dict__, 'job'))


1.4 / 5
# Объявите класс с именем MediaPlayer с двумя методами:
#   open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента
# file в объекте класса MediaPlayer)
#   play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
# Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с
# аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты
# метод play(). При этом, на экране должно отобразиться две строки (без кавычек):
#   "Воспроизведение filemedia1"
#   "Воспроизведение filemedia2"

# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#     def play(self):
#         print(f'Воспроизведение {self.filename}')

# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# media1.play()
# media2.play()

1.4 / 6
# Объявите класс с именем Graph и методами:
#   set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
#   draw() - отображение данных (в том же порядке, что и в списке data)
#       и атрибутом: LIMIT_Y: [0, 10]
# Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться н
# переданный в метод список. Метод draw() должен выводить на экран список в виде строки из чисел, разделенных пробелами
# и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).
# Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел,
# записанных через пробел. Например (вывод без кавычек):
# "10 0 2 5 7"

# class Graph:
#     LIMIT_Y = [0, 10]
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         for i in self.lst:
#             if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
#                 print(i, end=' ')
#         ###############################################
#         a, b = self.LIMIT_Y
#         print(*filter(lambda x: a <= x <= b, self.data))
#         print(*filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

1.4 / 8
# Имеется следующий класс для считывания информации из входного потока:
# import sys
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
# Которым, затем, можно воспользоваться следующим образом:
#     sr = StreamReader()
#     data, result = sr.readlines()
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
#     def create(self, fields, lst_values): ...
# который бы на входе получал список FIELDS из названий локальных атрибутов (передается в атрибут fields) и список
# строк lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с
# именами полей из fields и соответствующими значениями из lst_values.
# Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и
# число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.
# P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.
# Sample Input:
#     10
#     Питон - основы мастерства
#     512

# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) == len(lst_values):
#             for name, value in zip(fields, lst_values):
#                 setattr(self, name, value)
#             return True
#         return False
#         ###############################################
#         self.__dict__ = dict(zip(fields, lst_values))
#         return len(lst_values) == len(fields)

1.4 / 10
#   Из входного потока читаются строки данных с помощью команды:
#       lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
#       1 Сергей 35 120000
#       2 Федор 23 12000
#       3 Иван 13 1200
# ...
#   То есть, каждая строка - это элемент списка lst_in.
#   Необходимо в класс DataBase:
#       class DataBase:
#           lst_data = []
#           FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:
#       insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
#       select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно)
# по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.
#   Каждая запись в списке lst_data должна быть представлена словарем (добавление с помощью метода insert) в формате:
#       {'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
#   Например:
#       {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
#   Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей
# в коллекции FIELDS.
#   P. S. Ваша задача только добавить два метода в класс DataBase.

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#     def insert(self, data):
#         [self.lst_data.append(dict(zip(self.FIELDS, i.split()))) for i in data]
#     def select(self, a, b):
#         return self.lst_data[a:b + 1]
# db = DataBase()
# db.insert(lst_in)

1.4 / 11
#   Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
#       add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже
#       существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
#       remove(self, eng) - для удаления связки по указанному английскому слову;
#       translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
#       соответствующих переводу английского слова, даже если в списке всего одно слово).
#   Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
#       tree - дерево
#       car - машина
#       car - автомобиль
#       leaf - лист
#       river - река
#       go - идти
#       go - ехать
#       go - ходить
#       milk - молоко
#   Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go.
#   Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
#   Вывод в формате: идти ехать ходить

# class Translator:
#     d = {}
#
#     def add(self, eng, rus):
#         self.d.setdefault(eng, []).append(rus)
#
#     def remove(self, eng):
#         del self.d[eng]
#
#     def translate(self, eng):
#         return self.d[eng]
#
#
# tr = Translator()
# for k_v in ('tree - дерево', 'car - машина', 'car - автомобиль',
#             'leaf - лист', 'river - река', 'go - идти',
#             'go - ехать', 'go - ходить', 'milk - молоко'):
#     tr.add(*k_v.split(' - '))
# tr.remove('car')
# print(*tr.translate('go'))


1.5 / 3
#   Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:
#       my_money = Money(100)
#       your_money = Money(1000)
#   Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте)
# money каждого экземпляра класса.
#   P.S. На экран в программе ничего выводить не нужно

# class Money:
#     def __init__(self, money):
#         self.money = money
# my_money = Money(100)
# your_money = Money(1000)
# print(my_money.money)
# print(your_money.money)

1.5 / 4
#   Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
#       p1 = Point(10, 20)
#       p2 = Point(12, 5, 'red')
#   Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный
#   аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по умолчанию принимает
#   значение black.
#   Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой
#   новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points
#   укажите цвет 'yellow'.
#   P.S. На экран в программе ничего выводить не нужно.

# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
# points = [Point(i, i, 'yellow') if i == 3 else Point(i, i) for i in range(1, 2000, 2)]
# print(points)

1.5 / 5
#   Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого
# класса следующими командами:
#       g1 = Line(a, b, c, d)
#       g2 = Rect(a, b, c, d)
#       g3 = Ellipse(a, b, c, d)
#   Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов
# (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и
# ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
#   Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
# (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения).
# Все объекты сохраните в списке elements.
#   В списке elements обнулите координаты объектов только для класса Line.
#   P.S. На экран в программе ничего выводить не нужно.

# from random import choice, randint, sample
# class Figure:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
# class Line(Figure):
#     pass
# class Rect(Figure):
#     pass
# class Ellipse(Figure):
#     pass
# # elements = [choice([Line, Rect, Ellipse])(*sample(range(100), 4)) for _ in range(217)]
# # elements = [Line(0, 0, 0, 0) if isinstance(i, Line) else i for i in elements]
#    #############################################
# elements = [choice([Line, Rect, Ellipse])(*[randint(1, 100) for _ in '____']) for _ in range(217)]
# for i, y in enumerate(elements):
#     if isinstance(y, Line):
#         elements[i].sp = (0, 0)
#         elements[i].ep = (0, 0)

1.5 / 6
#   Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
#       tr = TriangleChecker(a, b, c)
#   Здесь a, b, c - длины сторон треугольника.
#   В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
#       1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
#       2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
#       3 - стороны a, b, c образуют треугольник.
#   Проверку параметров a, b, c проводить именно в таком порядке.
#   Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
#       a, b, c = map(int, input().split())
#   Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод
# is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         a, b, c = self.a, self.b, self.c
#         if not all(map(lambda x: type(x) in (int, float) and x > 0, (a, b, c))):
#             return 1
#         return 3 if a + b > c and b + c > a and a + c > b else 2
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
#############################################
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.s = [a, b, c]
#
#     def is_triangle(self):
#         if [i for i in self.s if not isinstance(i, (int, float))] or min(self.s) <= 0:
#             return 1
#         return 2 if max(self.s) * 2 >= sum(self.s) else 3
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

1.5 / 7
# '''Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
#       gr_1 = Graph(data)
# где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны
# формироваться следующие локальные свойства:
#       data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными);
#       is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
#   В этом классе объявите следующие методы:
#       set_data(self, data) - для передачи нового списка данных в текущий график;
#       show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
#       show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое
#   отображение данных: <строка из чисел следующих через пробел>");
#       show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение:
#   "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
#       set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
#
#   Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить
# сообщение: "Отображение данных закрыто"
#   Прочитайте из входного потока числовые данные с помощью команды:
#       data_graph = list(map(int, input().split()))
#   Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show()
# со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
# '''

# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data.copy()
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data.copy()
#
#     def show_table(self):
#         if self.is_show == False:
#             print("Отображение данных закрыто")
#
#     def show_graph(self):
#         if self.is_show == False:
#             print("Отображение данных закрыто")
#         else:
#             print("Графическое отображение данных:", *self.data)
#
#     def show_bar(self):
#         if self.is_show == False:
#             print("Отображение данных закрыто")
#         else:
#             print("Столбчатая диаграмма:", *self.data)
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()

1.5 / 8
# '''  Объявите в программе следующие несколько классов:
#       CPU - класс для описания процессоров;
#       Memory - класс для описания памяти;
#       MotherBoard - класс для описания материнских плат.
#   Обеспечить возможность создания объектов каждого класса командами:
#       cpu = CPU(наименование, тактовая частота)
#       mem = Memory(наименование, размер памяти)
#       mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
#   Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory,
#   максимум N - по числу слотов памяти на материнской плате (по умолчанию N = 4).
#   Объекты классов должны иметь следующие локальные свойства:
#       для класса CPU: name - наименование; fr - тактовая частота;
#       для класса Memory: name - наименование; volume - объем памяти;
#       для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее
#   число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов
#   класса Memory (максимум total_mem_slots штук по максимальному числу слотов памяти).
#   Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на
# материнской плате в виде следующего списка из четырех строк:
#       ['Материнская плата: <наименование>',
#       'Центральный процессор: <наименование>, <тактовая частота>',
#       'Слотов памяти: <общее число слотов памяти>',
#       'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
#   Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory)
#   P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.'''

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name  # наименование процессора
#         self.fr = fr  # тактовая частота
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name  # наименование памяти
#         self.volume = volume  # размер (объем) памяти
#
# class MotherBoard:
#     def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
#         self.name = name  # наименование платы
#         self.cpu = cpu  # ссылка на процессор (объект класса CPU)
#         self.total_mem_slots = total_mem_slots  # общее число слотов памяти (max = 4)
#         self.mem_slots = mem_slots[:total_mem_slots]  # список из объектов класса Memory
#
#     def get_config(self):
#         return [
#             f"Материнская плата: {self.name}",
#             f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
#             f"Слотов памяти: {self.total_mem_slots}",
#             f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]
#
# cpu = CPU('Intel Core', '3.4 GHz')
# mem1, mem2 = Memory('i7-3770', '32 Gb'), Memory('DDR4-3200AA', '16 Gb')
# mb = MotherBoard('Asus', cpu, [mem1, mem2])
# print(mb.get_config())

1.5 / 9
# '''Объявите в программе класс Cart (корзина), объекты которого создаются командой:
#     cart = Cart()
#   Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки.
#   Изначально этот список должен быть пустым.
#   В классе Cart объявить методы:
#     add(self, gd) - добавление в корзину товара, представленного объектом gd;
#     remove(self, indx) - удаление из корзины товара по индексу indx;
#     get_list(self) - получение из корзины товаров в виде списка из строк:
#
#     ['<наименование_1>: <цена_1>',
#     '<наименование_2>: <цена_2>',
#     ...
#     '<наименование_N>: <цена_N>']
#   Объявите в программе следующие классы для описания товаров:
#     Table - столы;
#     TV - телевизоры;
#     Notebook - ноутбуки;
#     Cup - кружки.
#   Объекты этих классов должны создаваться командой:
#     gd = ИмяКласса(name, price)
#   Каждый объект классов товаров должен содержать локальные свойства:
#     name - наименование;
#     price - цена.
#   Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два
# ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.'''

# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f'{x.name}: {x.price}' for x in self.goods]
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
#
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)

1.5 / 10
# '''Вам необходимо реализовать односвязный список из объектов класса ListObject:
#   Для этого объявите в программе класс ListObject, объекты которого создаются командой:
#     obj = ListObject(data)
#   Каждый объект класса ListObject должен содержать локальные свойства:
#     next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
#     data - данные объекта в виде строки.
#   В самом классе ListObject должен быть объявлен метод:
#     link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут
# next_obj объекта self должен ссылаться на obj).
#   Прочитайте список строк из входного потока командой:
#     lst_in = list(map(str.strip, sys.stdin.readlines()))
#   Затем, создайте первый объект head_obj класса ListObject и сохраните в нем первую строку из списка lst_in.
#   После этого присоедините к head_obj (как это показано на рисунке) последующие объекты класса ListObject
# с соответствующими строками из списка lst_in.
#   P.S. В программе что-либо выводить на экран не нужно.'''

# import sys
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# head_obj = ListObject(lst_in[0])  # h = 4
# for i in range(1, len(lst_in)):
#     new_obj = ListObject(lst_in[i])  # new = 5
#     head_obj.link(new_obj)  # next = None
#     head_obj = new_obj  # head = None
#############################################
# import sys
# class ListObject:
#     next_obj = None
#
#     def __init__(self, data):
#         self.data = data[0]
#         if len(data[1:]) != 0:
#             self.link(ListObject(data[1:]))
#
#     def link(self, obj):
#         self.next_obj = obj
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# head_obj = ListObject(lst_in)
#############################################
# import sys
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         if self.next_obj is None:
#             self.next_obj = obj
#             return True
#         return self.next_obj.link(obj)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # lst_in = [1, 2, 3, 4, 5]
# head_obj = ListObject(lst_in[0])
# for data_ in lst_in[1:]:
#     head_obj.link(ListObject(data_))

1.5 / 11
# '''Объявите два класса:
#       Cell - для представления клетки игрового поля;
#       GamePole - для управления игровым полем, размером N x N клеток.
#   С помощью класса Cell предполагается создавать отдельные клетки командой:
#       c1 = Cell(around_mines, mine)
#   Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие
#   мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
#       around_mines - число мин вокруг клетки (начальное значение 0);
#       mine - наличие мины в текущей клетке (True/False);
#       fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
#   С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
#       pole_game = GamePole(N, M)
#   Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и
# все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.
#   В классе GamePole должны быть также реализованы следующие методы:
#       init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая
# мина должна находиться в отдельной клетке).
#       show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта,
# то отображается символ #).
#   При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной
# инициализации игрового поля.
#   В классе GamePole могут быть и другие вспомогательные методы.
#   Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. '''

# from random import randint
# class Cell:
#     def __init__(self, around_mines=0, mine=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
# class GamePole:
#     def __init__(self, N, M):
#         self._n = N
#         self._m = M
#         self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
#         self.init()
#
#     def init(self):
#         m = 0
#         while m < self._m:
#             i = randint(0, self._n - 1)
#             j = randint(0, self._n - 1)
#             if self.pole[i][j].mine:
#                 continue
#             self.pole[i][j].mine = True
#             m += 1
#         indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self._n):
#             for y in range(self._n):
#                 if not self.pole[x][y].mine:
#                     mines = sum(
#                         (self.pole[i + x][j + y].mine for i, j in indx if
#                          0 <= x + i < self._n and 0 <= y + j < self._n))
#                     self.pole[x][y].around_mines = mines
#
#     def show(self):
#         for row in self.pole:
#             print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))
#
#
# pole_game = GamePole(4, 2)
# pole_game.show()
###############################################
# from random import sample
# from itertools import product
#
# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = True
#
# class GamePole:
#     def __init__(self, n, m):
#         self.pole = [[Cell(0, False) for _ in range(n)] for _ in range(n)]
#         self.init(n, m)
#
#     def init(self, n, m):
#         # генерим произвольное расположение мин
#         mine_coords = sample([*product(range(n), range(n))], m)
#
#         # размещаем мины на игровом поле
#         for x, y in mine_coords:
#             self.pole[x][y].mine = True
#
#         # считаем количество мин вокруг каждой ячейки
#         steps = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
#         # steps = (*product(range(-1, 2), range(-1, 2)),)
#
#         for x, y in product(range(n), range(n)):
#             for st_x, st_y in steps:
#                 if 0 <= x + st_x < n and 0 <= y + st_y < n and self.pole[x + st_x][y + st_y].mine:
#                     self.pole[x][y].around_mines += 1
#
#     def show(self):
#         for i in range(n):
#             for j in range(n):
#                 print(self.pole[i][j].around_mines if self.pole[i][j].fl_open else '#', end=' ')
#             print()
# #       for row in self.pole:
# #           print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))
#
# n, m = 10, 12
# pole_game = GamePole(n, m)
# pole_game.show()


1.6 / 7
# '''Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:
#       obj = AbstractClass()
# переменная obj должна ссылаться на строку с содержимым: "Ошибка: нельзя создавать объекты абстрактного класса"
#   P.S. В программе объявить только класс, выводить на экран ничего не нужно.'''
#
# class AbstractClass():
#     __instanse = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instanse is None:
#             return "Ошибка: нельзя создавать объекты абстрактного класса"#
# obj = AbstractClass()
# print(obj)

1.6 / 8
# '''Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
#       a = SingletonFive(<наименование>)
#   Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
#   Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой
# на последний (пятый) созданный объект.
#   Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
#       objs = [SingletonFive(str(n)) for n in range(10)]
#   P.S. В программе на экран ничего выводить не нужно. '''
#
# class SingletonFive():
#     __instanse = None
#     __count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__count < 5:
#             cls.__count += 1
#             cls.__instanse = super().__new__(cls)
#         return cls.__instanse
#
#     def __init__(self, name):
#         self.name = name
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# print(*objs)

1.6 / 9
'''В программе объявлена переменная TYPE_OS и два следующих класса:
      TYPE_OS = 1 # 1 - Windows; 2 - Linux
      class DialogWindows:
          name_class = "DialogWindows"

      class DialogLinux:
          name_class = "DialogLinux"
  Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
      dlg = Dialog(<название>)
  Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
  Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса 
DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих 
строчках программы. Имейте это в виду, при объявлении класса Dialog.
  P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.'''

TYPE_OS = 2

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        name = None
        if TYPE_OS == 1:
            return  setattr(DialogWindows, 'name', name[0])
            # cls.name = DialogWindows()
            # cls.obj = super().__new__(DialogWindows)
        else:
             setattr(DialogLinux, 'name', name)

            # cls.name = DialogLinux()
        # return cls.name

    def __init__(self, name):
        self.name = name


dlg = Dialog('name')
print(dlg)
