from query_maker import query_maker
from controller import Controller


class DBWires(Controller):
    __border_x = 1000
    __border_y = 1000

    def __is_in_border(self, x, y):
        if (x < self.__border_x and y < self.__border_y):
            return True
        else:
            return False

    def insert_im_type(self):
        name = input("Введите имя имитатора")
        quan_pin = int(input("Введите число пинов"))
        height, width = map(float, input("Введите высоту и ширину имитатора").split())
        cmd = query_maker(f'''insert into im_type values(default, '{name}', {quan_pin}, {height}, {width})''')

    def insert_im(self):
        cmd = query_maker('select * from im_type')
        for i in range(len(cmd)):
            print(f'{i + 1}.{cmd[i][1]}. {cmd[i][2]} пинов. Высота и ширина {cmd[i][3]}, {cmd[i][4]}')
        im_id = int(input("Выберите тип имитатора:"))
        im_id = cmd[im_id - 1][0]
        x, y, angle = map(float, input("Введите через запятую центр имитатора(x, y) и угол поворота:").split(','))
        cmd = query_maker(f'insert into imitator values(default, {im_id}, {x}, {y}, {angle})')