from query_maker import query_maker


class Parser:
    __lst = open("Coords.txt", encoding='utf-8')
    __lines = __lst.readlines()
    __border_x = 1000
    __border_y = 1000

    def __links_seg(self, lines):
        ar_wires = []
        for i in range(len(lines)):
            if lines[i][0:6] == "Трасса":
                ar_wires.append(i)
        ar_wires.append(len(lines))
        return ar_wires

    def __string_in_float_arr(self, line):
        start = 0
        coord = []
        for i in range(len(line)):
            if line[i] == ',' or line[i] == ';':
                s = float(line[start:i])
                coord.append(s)
                start = i + 1
        return coord

    def __val_seg(self, line):
        arr = []
        seg = []
        for i in range(len(line)):
            if line[i] == ':' or line[i] == '_':
                seg.append(i)
        for i in range(len(seg) - 1):
            arr.append(line[seg[i] + 1:seg[i + 1]])
        line = line[:-1]
        arr.append(line[seg[-1] + 1:])
        return arr

    def __cont_exists(self, con_id):
        cmd = query_maker(f'''select count(*) from con_wire where con_beg_id = {con_id} or con_end_id = {con_id} ''')[0][0]
        if cmd == 1:
            return True
        else:
            return False

    def __is_in_border(self, x, y):
        if (x < self.__border_x and y < self.__border_y):
            return True
        else:
            return False

    def __insert_con(self):
        seg = self.__links_seg(self.__lines)
        for i in range(len(seg) - 1):
            vals = self.__val_seg(self.__lines[seg[i]])
            print(seg[i])
            try:
                cmd = query_maker(f'''insert into connections(con_id, con_name) values(default, '{vals[0]}')''')
            except:
                print("Ошибочка")
            try:
                cmd = query_maker(f'''insert into connections(con_id, con_name) values(default, '{vals[2]}')''')
            except:
                print("Ошибочка")

    def __insert_cont(self):
        seg = self.__links_seg(self.__lines)
        for i in range(len(seg) - 1):


    def __insert_knots(self):
        seg = self.__links_seg(self.__lines)
        for i in range(len(seg) - 1):
            try:
                cmd = query_maker(
                    f'''insert into wires (wire_id, wire_num) values (default, '{self.__lines[seg[i]][7:]}');''')
            except:
                print('Запись уже существует или произошла другая неполадка')
            wire_id = query_maker(f'''select wire_id from wires where wire_num = '{self.__lines[seg[i]][7:]}';''')[0][0]
            k = 1
            for j in range(seg[i] + 2, seg[i + 1] - 1):
                if (not (self.__is_in_border(self.__string_in_float_arr(self.__lines[j])[0],
                                             self.__string_in_float_arr(self.__lines[j])[1]))):
                    print(
                        f"Узлы выходят за границу плаза. Связь {self.__lines[seg[i]][7:]}.\n Номер узла {k}. Координаты узла ",
                        self.__string_in_float_arr(self.__lines[j]))
                    continue
                cmd = query_maker(f'''insert into knots values (default,
                                                                {self.__string_in_float_arr(self.__lines[j])[0]},
                                                                {self.__string_in_float_arr(self.__lines[j])[1]},
                                                                {self.__string_in_float_arr(self.__lines[j])[2]},
                                                                {self.__string_in_float_arr(self.__lines[j])[3]})''')
                knot_id = query_maker(f'''select knot_id from knots where  x = {self.__string_in_float_arr(self.__lines[j])[0]} and
                                                                           y = {self.__string_in_float_arr(self.__lines[j])[1]} and
                                                                           z = {self.__string_in_float_arr(self.__lines[j])[2]} and
                                                                           angle = {self.__string_in_float_arr(self.__lines[j])[3]}''')[0][0]
                cmd = query_maker(f'''insert into wire_knots values({wire_id}, {k}, {knot_id})''')
                k = k + 1

    def __init__(self):
        self.__insert_con()
        self.__insert_knots()

    # def __control_ends(self):
    #     cons = query_maker('''select cont_id from contacts''')
    #     temp_cons1 = query_maker('''select ''')
    #     temp = 0
    #     for i in cons:

    # def checking_sys(self):

    # def foo(self):
    #     # for i in range(len(self.__lines)):
    #     #     print(self.__lines[i], i)
    #     seg = self.__links_seg(self.__lines)
    #     for i in range(len(seg)):
    #         print(i+1, self.__lines[seg[i]])
    #     # for i in range(len(seg)):
    #     #     print(i+1, seg[i])
    #
    # def boo(self):
    #     seg = self.__links_seg((self.__lines))
    #     self.__lines[0].replace("_", "—")
    #     print(self.__lines[seg[0]][7:])

    def foooo(self):
        # cmd = query_maker('''select knot_id from knots''')
        # for i in range(len(cmd)):
        #     print(cmd[i][0])
        cmd = query_maker('''select count(*) from knots where knot_id = 666''')
        print(cmd[0][0])
