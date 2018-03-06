def read_field(filename):
    """
    Returns a dictionary with battleship field from file.
    :param filename: name of the file
    :return: dictionary with fieks
    """
    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    # Check if we did not loose spaces and add them back
    for i, line in enumerate(lines):
        if len(line) < 10:
            lines[i] = line + " " * (10 - len(line))
    if len(lines) < 10:
        for i in range(10 - len(lines)):
            lines.append('          ')

    markers = {' ': 0, '*': 1, 'X': 2}
    d = {}
    for i in range(1, len(lines)+1):
        for n, v in enumerate('ABCDEFGHIJ'):
            d[(i, v)] = markers[lines[i-1][n]]
    return d


def has_ship(data, cell):
    if isinstance(cell[1], int):
        cell = (cell[1], cell[0])
    return True if data[cell] != 0 else False


def ship_size(data, cell, get_ship=False):
    if isinstance(cell[1], int):
        cell = (cell[1], cell[0])

    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    raw, column = cell[0], cell[1]

    if data[cell] != 0:
        ship = {}

        for i in range(raw, 0, -1):
            if data[i, column] != 0:
                ship[i, column] = data[i, column]
            else:
                break

        j = columns.index(column)
        for i in range(raw, 0, -1):
            j -= 1
            if data[raw, columns[j]] != 0:
                ship[raw, columns[j]] = data[raw, columns[j]]
            else:
                break

        for i in range(raw, 9):
            if data[i, column] != 0:
                ship[i, column] = data[i, column]
            else:
                break

        j = columns.index(column)
        for i in range(raw, 9):
            j += 1
            if data[raw, columns[j]] != 0:
                ship[raw, columns[j]] = data[raw, columns[j]]
            else:
                break

        return len(ship) if not get_ship else ship
    else:
        return None


def is_valid(data):
    ships = []
    ship_cells = {}
    for cell in data:
        ship = ship_size(data, cell, get_ship=True)
        if ship:
            s = []
            for k in ship.keys():
                if k not in ship_cells:
                    ship_cells[k] = ship[k]
                    s.append(ship[k])
            if s:
                ships.append(s)

    #print(ships)
    if len(ships) == 10:
        on, tw, th, fr = 0, 0, 0, 0
        for s in ships:
            if len(s) == 4:
                fr += 1
            elif len(s) == 3:
                th += 1
            elif len(s) == 2:
                tw += 1
            elif len(s) == 1:
                on += 1

        return True if (on, tw, th, fr == 4, 3, 2, 1) else False
    else:
        return False


def field_to_str(data, bool=False):
    if bool:
        st = ''
        for i in range(1, 11):
            for l in "ABCDEFGHIJ":
                st += str(data[i, l])
            st += '\n'
    else:
        markers = {0: ' ', 1: '*', 2: 'X'}
        st = ''
        for i in range(1, 11):
            for l in "ABCDEFGHIJ":
                st += markers[data[i, l]]
            st += '\n'
    return st



