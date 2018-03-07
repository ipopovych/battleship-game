from funcs import create_field, field_with_ships


class Field:
    def __init__(self):
        self._field, self.ships = create_field()
        self._withships = field_with_ships(self._field)

    def shoot_at(self, cell):
        ship = self._field[cell[0]][cell[1]]
        if ship:
            self._withships[cell[0]][cell[1]] = 'Shotship'
            return ship.shoot_at(cell)
        else:
            if self._withships[cell[0]][cell[1]] == 'Shot':
                return -1
            else:
                self._withships[cell[0]][cell[1]] = 'Shot'
                return None

    def present_ships(self):
        """
        Returns number of present not killed ships
        """
        p = 0
        for s in self.ships:
            if s.is_alive():
                p += 1
        return p

    def field_without_ships(self):
        s = '     A   B   C    D    E   F    G   H   I    J  \n'
        r = ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10']
        for i, f in enumerate(self._withships):
            s += ' ' + r[i] + ' '
            for c in f:
                if c == 'Shot':
                    s += ' 💣 '
                elif c == 'Ship':
                    s += ' 🔳 '
                elif c == 'Shotship':
                    s += ' ❌ '
                else:
                    s += ' 🔳 '
            s += '\n'
        return s

    def field_with_ships(self):
        s = '     A   B   C    D    E   F    G   H   I    J  \n'
        r = ['1 ', '2 ', '3 ',  '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10']
        for i, f in enumerate(self._withships):
            s += ' '+r[i]+' '
            for c in f:
                if c == 'Shot':
                    s += ' 💣 '
                elif c == 'Ship':
                    s += ' 🚢 '
                elif c == 'Shotship':
                    s += ' ❌ '
                else:
                    s += ' 🔳 '
            s += '\n'
        return s

    def field(self):
        return self.field
