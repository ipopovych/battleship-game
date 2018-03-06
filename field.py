from funcs import create_field, create_empty_field
from ship import Ship


class Field:
    def __init__(self):
        self._field = create_field()
        self._noships = create_empty_field()
        self._withships = create_empty_field()
        print(self._field)

    def shoot_at(self, cell):
        self._noships[cell[0] - 1][cell[1] - 1] = 'Shot'
        ship = self._field[cell[0] - 1][cell[1] - 1]

        if ship:
            ship.shoot_at(cell)
        else:
            self._field[cell[0] - 1][cell[1] - 1] = 'Shot'

    def field_without_ships(self):
        s = ''
        for f in self._noships:
            for c in f:
                if c:
                    s += '■'
                else:
                    s += '□'
            s += '\n'
        return s

    def field_with_ships(self):
        for c in range(10):
            for e in range(10):
            #i = self._withships.index(c)
                if isinstance(self._field[c, e], Ship):
                    pass
        pass

