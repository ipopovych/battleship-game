import random
from ship import Ship

def create_field():
    f = []
    for i in range(10):
        a = []
        for i in range(10):
            a.append(None)
        f.append(a)

    coordinates = []
    for i in range(1, 11):
        for a in range(1, 11):
            coordinates.append((i, a))

    present_ships = set()

    def surrounding_cells(cell):
        x, y = cell[0], cell[1]
        if x == 1:
            if y == 1:
                return [cell, (x, y + 1), (x + 1, y), (x + 1, y + 1)]
            elif y == 10:
                return [cell, (x + 1, y), (x, y - 1), (x + 1, y - 1)]
            else:
                return [cell, (x + 1, y), (x, y - 1),
                        (x, y + 1), (x + 1, y + 1), (x + 1, y - 1)]

        elif x == 10:
            if y == 1:
                return [cell, (x - 1, y), (x - 1, y + 1), (x, y + 1)]
            elif y == 10:
                return [cell, (x, y - 1), (x - 1, y - 1), (x - 1, y)]
            else:
                return [cell, (x - 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1)]

        elif y == 1:
            return [cell, (x - 1, y), (x + 1, y), (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        elif y == 10:
            return [cell, (x - 1, y), (x + 1, y), (x, y - 1),
                    (x - 1, y - 1), (x + 1, y - 1)]
        else:
            return [cell, (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1),
                    (x + 1, y + 1), (x + 1, y - 1)]

    def locate_ship(length):

        def check_placing(ship_cells):
            for cell in ship_cells:
                sur = surrounding_cells(cell)
                for cell in sur:
                    if cell not in present_ships:
                        continue
                    else:
                        return False
            return True

        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while True:
            horiz = random.choice((True, False))
            if horiz:
                bowraw = random.choice(a)
                bowcol = random.randint(1, 11 - length)

            else:
                bowraw = random.randint(1, 11 - length)
                bowcol = random.choice(a)

            cell = (bowraw, bowcol)

            s = Ship(length, bow=cell, horizontal=horiz)
            cells = s.coordinates()

            if check_placing(cells):
                for cell in cells:
                    f[cell[0] - 1][cell[1] - 1] = s
                    for c in surrounding_cells(cell):
                        present_ships.add(c)
                #print(len(present_ships))
                break
            else:
                continue
        return cells

    locate_ship(4)
    locate_ship(3)
    locate_ship(3)
    locate_ship(2)
    locate_ship(2)
    locate_ship(2)

    coordinates = []
    for i in range(1, 11):
        for a in range(1, 11):
            coordinates.append((i, a))

    for c in present_ships:
        if c in coordinates:
            coordinates.remove(c)

    def check_cell(c):
        sur = surrounding_cells(c)
        for cell in sur:
            if cell not in present_ships:
                continue
            else:
                return False

        return True

    def place_one():
        for c in coordinates:
            if check_cell(c):
                f[c[0] - 1][c[1] - 1] = Ship(1, bow=c, horizontal=True)
                for cel in surrounding_cells(c):
                    coordinates.remove(cel)
                    break

    for i in range(4):
        place_one()

    return f