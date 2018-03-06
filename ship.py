import random

class Ship:

    def __init__(self, length, bow=(1, 1), horizontal=False):
        """
        :param length: int, size of the ship, 1 <= length <= 4
        bow: coordinates tuple of left upper angle of the ship - (raw, column)
        horizontal: bool, true if ship is horizontal
        _hit: list of bool, True indicates shoot ships
        """
        assert 1 <= length <= 4, "Ship init failed. Maximum length = 4"
        self._length = length
        self.bow = bow
        self.horizontal = horizontal
        self._hit = length * [False]

    def coordinates(self):
        coordinates = [self.bow]
        if self.horizontal:
            raw, col = self.bow[0], self.bow[1]
            for i in range(self._length-1):
                col += 1
                coordinates.append((raw, col))
        else:
            raw, col = self.bow[0], self.bow[1]
            for i in range(self._length - 1):
                raw += 1
                coordinates.append((raw, col))
        return coordinates

    def shoot_at(self, cell):
        """
        Returns true if the ship was reached by gun.
        :param cell: tuple, cell to shoot
        :return: bool
        """
        coor = self.coordinates()
        if cell in coor:
            self._hit[coor.index(cell)] = True
            return True
        else:
            return False
