class Player:
    """ Indicates a player of battleship game."""
    def __init__(self, name, password):
        """ Initializes a player from name and their password."""
        self._name = name
        self._password = password

    def read_position(self):
        """
        Returns tuple of integer coordinates given as input of 'letter integer'

        'A 1' - (0,0)
        'b 2' - (1,1)
        """
        st = "ABCDEFGHIJ"
        pos = input("Enter position. For example, '1 A' :\n").split(' ')
        try:
            if len(pos) != 2 or int(pos[0]) not in range(1, 11) \
                                                   or pos[1].upper() not in st:
                print("Please, enter right position")
                return self.read_position()
        except ValueError:
            print("Please, enter right position")
            return self.read_position()

        return int(pos[0])-1, st.index(pos[1].upper())

    def name(self):
        """ Returns player's name. """
        return self._name

    def login(self, password):
        """ Returns True if password is correct. """
        return True if password == self._password else False
