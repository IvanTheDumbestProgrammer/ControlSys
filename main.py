import math
from timeit import default_timer as timer
import pandas
from db_part import DB_interact as database
from parser import Parser
from array import *
start = timer()
p = database()

# while(True):
#     print('''Выберите операцию из следующих:
#              0.Выход из программы
#              1.Ввод данных жгута
#              2.Ввод данных соединения
#              3.Ввод данных узлов
#              4.Ввести соответствие провода и соединения
#              5.''')
#
#     cmd = int(input())
#     match cmd:
#         case 0:
#             print("Программа завершена")
#             break
#         case 1:
#             p.insert_wires()
#         case 2:
#             p.insert_con()
#         case 3:
#             p.insert_knots()
#         case 4:
#             p.insert_con_wire()
# p.insert_wire_data()

# p = Parser()
# p.foooo()
# end = timer()
# print(end - start)


