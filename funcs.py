import random
from ship import Ship


def create_field():
    f = empty_field()
    ships = []
    left_coordinates = []

    for i in range(10):
        for a in range(10):
            left_coordinates.append((i, a))

    def locate_ship(length):

        def check_placing(ship_cells):
            for cell in ship_cells:
                sur = surrounding_cells(cell)
                for cell in sur:
                    if f[cell[0]][cell[1]] is None:
                        pass
                    else:
                        return False
            return True

        while True:
            found = False
            while found is False:
                horiz = random.choice((True, False))
                cell = random.choice(left_coordinates)
                if horiz:
                    bowcol = cell[1]
                    if bowcol <= 10 - length:
                        found = True
                else:
                    bowraw = cell[0]
                    if bowraw <= 10 - length:
                        found = True

            s = Ship(length, bow=cell, horizontal=horiz)
            shipcells = s.coordinates()

            if check_placing(shipcells):
                for cell in shipcells:
                    f[cell[0]][cell[1]] = s
                break
            else:
                continue
        ships.append(s)
        return s

    # Locating required ships
    locate_ship(4)
    locate_ship(3)
    locate_ship(3)
    locate_ship(2)
    locate_ship(2)
    locate_ship(2)
    for i in range(4):
        locate_ship(1)

    return f, ships


def empty_field():
    f = []
    for i in range(10):
        a = []
        for i in range(10):
            a.append(None)
        f.append(a)
    return f


def field_with_ships(field):
    f = empty_field()
    for i in range(10):
        for k in range(10):
            s = field[i][k]
            if s is not None:
                f[i][k] = 'Ship'
    return f


def surrounding_cells(cell):
    x, y = cell[0], cell[1]
    if x == 0:
        if y == 0:
            return [cell, (x, y + 1), (x + 1, y), (x + 1, y + 1)]
        elif y == 9:
            return [cell, (x + 1, y), (x, y - 1), (x + 1, y - 1)]
        else:
            return [cell, (x + 1, y), (x, y - 1),
                    (x, y + 1), (x + 1, y + 1), (x + 1, y - 1)]
    elif x == 9:
        if y == 0:
            return [cell, (x - 1, y), (x - 1, y + 1), (x, y + 1)]
        elif y == 9:
            return [cell, (x, y - 1), (x - 1, y - 1), (x - 1, y)]
        else:
            return [cell, (x - 1, y), (x, y - 1), (x, y + 1),
                    (x - 1, y - 1), (x - 1, y + 1)]
    elif y == 0:
        return [cell, (x - 1, y), (x + 1, y), (x, y + 1),
                (x - 1, y + 1), (x + 1, y + 1)]
    elif y == 9:
        return [cell, (x - 1, y), (x + 1, y), (x, y - 1),
                (x - 1, y - 1), (x + 1, y - 1)]
    else:
        return [cell, (x - 1, y), (x + 1, y), (x, y - 1),
                (x, y + 1), (x - 1, y - 1), (x - 1, y + 1),
                (x + 1, y + 1), (x + 1, y - 1)]
