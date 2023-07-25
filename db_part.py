from query_maker import  query_maker

class DB_interact:
    __border_x = 1000
    __border_y = 1000
    def insert_wire_data(self):
        type = input("Введите тип провода:")
        diameter = float(input("Введите диаметр провода:"))
        cmd = query_maker(f'''insert into wire_data values (default, '{type}', {diameter})''')

    def insert_boards(self):
        board_name = input("Введите название платы:")
        cmd = query_maker(f'''insert into boards values (default, '{board_name}')''')

    def insert_imimitator(self):
        quan_pins = int(input("Введите кол-во пинов:"))
        x, y = map(int, input().split(','))

    def insert_knots(self):
        knot_num = input("Введите номер узла:")
        x, y = map(int, input("Введите через запятую:").split(','))
        cmd = query_maker(f'''insert into knots values (default, {num}, {x}, {y})''')

    def insert_wires(self):
        wire_num = input("Введите номер провода:")
        cmd = query_maker(f'select id_data, type, diameter from wire_data order by id_data')
        for i in range(len(cmd)):
            print(f'{i+1}. {cmd[i][1]} 1x{cmd[i][2]}')
        data_num = int(input())
        id_data = cmd[data_num][0]
        cmd = query_maker(f'''insert into wires values(default, '{wire_num}',{id_data})''')


    # def insert_knots(self):
    #     print("Выберите провод:")
    #     cmd = query_maker(f'''select wire_num from wires order by wire_id''')
    #     for i in range(len(cmd)):
    #         print(f'{i + 1}.', cmd[i][0])
    #     wire_id = int(input()) - 1
    #     while (True):
    #         if wire_id >= 0 and wire_id <= len(cmd):
    #             break
    #         else:
    #             print("Повторите ввод")
    #         wire_id = int(input()) - 1
    #     num = int(input("Введите количество узлов:"))
    #     print(query_maker(f'''select * from wires where wire_id = {wire_id}'''))
    #     x_beg = query_maker(f'''select "X_beg" from wires where wire_id = {wire_id}''')[0][0]
    #     y_beg = query_maker(f'''select "Y_beg" from wires where wire_id = {wire_id}''')[0][0]
    #     x_end = query_maker(f'''select "X_end" from wires where wire_id = {wire_id}''')[0][0]
    #     y_end = query_maker(f'''select "Y_end" from wires where wire_id = {wire_id}''')[0][0]
    #     x_pr = x_beg
    #     y_pr = y_beg
    #     x_kn = []
    #     y_kn = []
    #     x = int
    #     y = int
    #     for i in range(num - 2):
    #         x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{i + 1}:").split(','))
    #         while (True):
    #             if x_end < DB_interact.__border_x and y_end < DB_interact.__border_y:
    #                 break
    #             print("Данная точка выходит за границы плаза, повторите ввод!")
    #             x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{i + 1}:").split(','))
    #         while (True):
    #             if not (((x == x_beg) and (y == y_beg)) or ((x == x_end) and (y == y_end))):
    #                 break
    #             print(x_end, y_end)
    #             print("Узел не должен совпадать с началом и концом!")
    #             x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{i + 1}:").split(','))
    #         while (True):
    #             if ((x == x_pr) != (y == y_pr)):
    #                 x_kn.append(x)
    #                 y_kn.append(y)
    #                 x_pr = x
    #                 y_pr = y
    #                 break
    #             print("Введите корректные данные. Одна из координат узла должна совпадать с предыдущей!")
    #             x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{i + 1}:").split(','))
    #     x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{num - 1}:").split(','))
    #     while (True):
    #         if not (((x == x_beg) and (y == y_beg))) and ((x != x_end) and (y != y_end)) and (
    #                 (x == x_pr) != (y == y_pr)):
    #             x_kn.append(x)
    #             y_kn.append(y)
    #             x_pr = x
    #             y_pr = y
    #             break
    #         print(
    #             "Точка не должна совпадать с началом и иметь совпадающую координату с концом, одна из координат должна совпадать с координатой предыдущего узла!")
    #         x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{num - 1}:").split(','))
    #     x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{num}:").split(','))
    #     while (True):
    #         if (((x != x_beg) and (y != y_beg) and ((x == x_end) != (y == y_end)) and ((x == x_pr) != (y == y_pr)))):
    #             x_kn.append(x)
    #             y_kn.append(y)
    #             break
    #         print(
    #             "Введите корректные данные. Одна из координат узла должна совпадать с предыдущей и не должна совпадать с началом и концом!")
    #         x, y = map(int, input(f"Введите через запятую коррдинаты X, Y узла №{num}:").split(','))
    #     for i in range(num):
    #         cmd = query_maker(f'''insert into knots values(default, '{wire_id}', {i + 1}, {x_kn[i]}, {y_kn[i]})''')

    def insert_wires(self):

        print("Введите номер провода вида '1-1':")
        num = input()
        print("Введите координаты X,Y начала через запятую:")

        x_beg, y_beg = map(int, input().split(','))
        while (True):
            if x_beg < DB_interact.__border_x and y_beg < DB_interact.__border_y:
                break
            print("Данная точка выходит за границы плаза, повторите ввод!")
            x_beg, y_beg = map(int, input().split(','))

        print("Введите координаты X,Y конца через запятую:")
        x_end, y_end = map(int, input().split(','))
        while (True):
            if x_end < DB_interact.__border_x and y_end < DB_interact.__border_y:
                break
            print("Данная точка выходит за границы плаза, повторите ввод!")
            x_end, y_end = map(int, input().split(','))
        cmd = query_maker('''select data from wire_data''')
        print("Выберите тип провода, для этого введите цифру от 1 до 3:")
        cmd = query_maker('''select data from wire_data''')
        for i in range(len(cmd)):
            print(f'{i + 1}.', cmd[i])
        id_data = int(input())
        while (True):
            if id_data > 0 and id_data <= len(cmd):
                break
            else:
                print("Повторите ввод")
            id_data = int(input())
        id_data = query_maker(f'''select id_data from wire_data where data = '{cmd[id_data - 1][0]}';''')
        cmd = query_maker(
            f'''insert into wires values(default, '{num}', {x_beg}, {y_beg}, {x_end}, {y_end}, {id_data[0][0]}) ''')

    def insert_con(self):
        con_name = input("Введите обозначение разъема (например Х1):")
        print("Выберите плату, на которой располагается соединение:")
        cmd = query_maker(f'''select name_board from boards''')
        for i in range(len(cmd)):
            print(f'{i + 1}.', cmd[i][0])
        board_id = int(input())
        print(len(cmd))
        while (True):
            if board_id > 0 and board_id <= len(cmd) + 1:
                break
            else:
                print("Повторите ввод")
            id_data = int(input())
        cmd = query_maker(f'''select id_board from boards where name_board = '{cmd[board_id - 1][0]}';''')
        quan_pins = int(input("Введите количество пинов разъема:"))
        cmd = query_maker(f'''insert into connections values(default, '{con_name}', {board_id}, {quan_pins})''')



    def insert_con_wire(self):
        cmd1 = query_maker(f'select wire_num from wires order by wire_id')
        for i in range(len(cmd1)):
            print(f'{i + 1}.', cmd1[i][0])
        wire_num = int(input("Выберите провод:")) - 1
        print(cmd1[wire_num][0])

        while (True):
            cmd2 = query_maker((f'select con_name from connections order by con_id'))
            for i in range(len(cmd2)):
                print(f'{i + 1}.', cmd2[i][0])
            con1 = int(input("Выберите 1ое соединение:")) - 1
            print(cmd2[con1][0])
            con2 = int(input("Выберите 2ое соединение:")) - 1
            print(cmd2[con2][0])
            if (con1 != con2):
                break
            print("Выбрано одно и тоже соединение! Повторите ввод")

        buf1 = query_maker(f'''select con_id from connections where con_name = '{cmd2[con1][0]}';''')
        buf2 = query_maker(f'''select con_id from connections where con_name = '{cmd2[con2][0]}';''')
        buf3 = query_maker(f'''select wire_id from wires where wire_num = '{cmd1[wire_num][0]}';''')
        cmd = query_maker(f'''insert into con_wire values({buf1[0][0]}, {buf2[0][0]},{buf3[0][0]})''')


