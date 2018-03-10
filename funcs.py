import random
from ship import Ship


def create_field():
    """
    Generates field for battleship game, randomly locates 10 ships:
    length - number of ships
       4   -   1
       3   -   2
       2   -   3
       1   -   4

    Return: list field, list of present ships
    tuple( list(list(Ship, None)), list(Ship) )
    """
    f = empty_field()
    ships = []
    left_coordinates = []

    for i in range(10):
        for a in range(10):
            left_coordinates.append((i, a))

    def locate_ship(length):
        """
        Creates a ship of given length and locates on the field f.
        :param length: integer, from 1 to 4
        :return: Ship object
        """
        def check_placing(ship_cells):
            """
            Returns True if it is possible to locate ship on the field.
            :param ship_cells: list of tuple coordinates.
            :return: bool
            """
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
    """
    Returns empty field:
    list of None 10x10
    """
    f = []
    for i in range(10):
        a = []
        for i in range(10):
            a.append(None)
        f.append(a)
    return f


def field_with_ships(field):
    """
    Returns a list field in which 'Ship'
    string represents a ship.

    :param field: list(list(Ship, None))
    :return: list(list('Ship', None))
    """
    f = empty_field()
    for i in range(10):
        for k in range(10):
            s = field[i][k]
            if s is not None:
                f[i][k] = 'Ship'
    return f


def surrounding_cells(cell):
    """
    Returns list of cells that surround given cell on the field 10x10.
    coordinates start from 0, so min cel is (0,0) max is (9,9).

    :param cell: tuple(int, int) - coordinates of the cell
    :return: list(tuple(int, int))

    >>> surrounding_cells((2,1))
    [(2, 1), (1, 1), (3, 1), (2, 0), (2, 2), (1, 0), (1, 2), (3, 2), (3, 0)]

    >>> surrounding_cells((0,0))
    [(0, 0), (0, 1), (1, 0), (1, 1)]

    """
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
