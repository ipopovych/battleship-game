from funcs import create_field


class Field:
    def __init__(self):
        self._field = create_field()
        print(self._field)

    def shoot_at(self, cell):
        pass

    def field_without_ships(self):
        pass

    def fiel_with_ships(self):
        pass

