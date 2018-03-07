class Player:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def read_position(self):
        st = "ABCDEFGHIJ"
        pos = input("Enter position. For example, '1 A' :\n").split(' ')
        try:
            if len(pos) != 2 or int(pos[0]) not in range(1, 11) or pos[1].upper() not in st:
                print("Please, enter right position")
                return self.read_position()
        except ValueError:
            print("Please, enter right position")
            return self.read_position()

        return int(pos[0])-1, st.index(pos[1].upper())

    def name(self):
        return self._name

    def login(self, password):
        return True if password == self._password else False
