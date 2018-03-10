class Ship:
    """Indicates a battleship game ship."""
    def __init__(self, length, bow=(1, 1), horizontal=False):
        """
        :param length: int, size of the ship, 1 <= length <= 4
        :param bow: coordinates of left upper angle of the ship - (raw, column)
        :param horizontal: bool, true if ship is horizontal

        self._hit: list of bool, True indicates shoot ships
        """
        assert 1 <= length <= 4, "Ship init failed. Maximum length = 4"
        self._length = length
        self.bow = bow
        self.horizontal = horizontal

        l = []
        for i in range(length):
            l.append(False)

        self._hit = l

    def coordinates(self):
        """
        Returns list of tuple coordinates  of ship location.
        """
        coordinates = [self.bow]
        if self.horizontal:
            raw, col = self.bow[0], self.bow[1]
            for i in range(self._length - 1):
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
        :param cell: tuple, cell to shoot
        :return:
            None if no ship
            -1 if already shoot
            0 if killed
            1,2, or 3 - parts left to kill
        """
        coor = self.coordinates()
        if self._hit[coor.index(cell)] is False:
            if self._length == 1:
                return 0
            self._hit[coor.index(cell)] = True
            return self._hit.count(False)
        else:
            return -1

    def is_alive(self):
        """Returns True if there are parts that are not shoot"""
        if self._hit[0] and len(set(self._hit)) == 1:
            return False
        else:
            return True
