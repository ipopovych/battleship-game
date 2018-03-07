from funcs import create_field, empty_field, field_with_ships


class Field:
    def __init__(self):
        self._field, self.ships = create_field()
        self._withships = field_with_ships(self._field)

    def shoot_at(self, cell):
        ship = self._field[cell[0]][cell[1]]
        if ship:
            ship.shoot_at(cell)
            self._withships[cell[0]][cell[1]] = 'Shotship'
        else:
            self._withships[cell[0]][cell[1]] = 'Shot'

    def field_without_ships(self):
        s = '      A   B   C    D    E   F    G   H   I    J  \n'
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
        s = '      A   B   C    D    E   F    G   H   I    J  \n'
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


f = Field()
print(f.field_with_ships())
print(f.field_without_ships())
f.shoot_at((0, 4))
print(f.field_without_ships())
print(f.field_with_ships())
