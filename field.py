from funcs import create_field, field_with_ships


class Field:
    """Represents a battleship game field."""
    def __init__(self):
        """Initializes field with field and ships lists."""
        self._field, self.ships = create_field()
        self._withships = field_with_ships(self._field)

    def shoot_at(self, cell):
        """
        Represents shooting at one ship from field.
        return: None if no ship in the cell
                - 1 if cell was shot before
                call ship.shoot_at function if there is ship:
                    return 0 if killed,
                           1,2,3 - number of alive parts left.
        :param cell: tuple(number, letter)
        """
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

    def field_without_ships(self):
        """
        Returns string showing current situation on the field,
        but without located not shoot ships.
        """
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
        """
        Returns string showing current situation on the field,
        with located not shoot ships.
        """
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
        """
        Returns field as a list(list(Ship, None))
        """
        return self.field
