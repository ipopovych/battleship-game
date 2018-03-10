from field import Field
from player import Player


class Game:
    """ Indicates a session of battleship game. """
    def __init__(self):
        """
        Initializes a game with 2 players and fields.

        self.players - dict( player_index : (Player, Field, number of ships) )
        self.current_player - int, 0 or 1, index of current player.
        """

        f0, f1 = Field(), Field()

        n0 = input("Player 1, please enter your name: ")
        pswd0 = input("{}, please create password: ".format(n0))
        p0 = Player(name=n0, password=pswd0)

        n1 = input("Player 2, please enter your name: ")
        pswd1 = input("{}, please create password: ".format(n1))
        p1 = Player(name=n1, password=pswd1)

        self.players = {0: [p0, f0, 10], 1: [p1, f1, 10]}
        self._current_player = 0

    def run(self):
        while (self.players[self._current_player][2] > 0 and
                       self.players[abs(self._current_player - 1)][2] > 0):

            # Ask for password before allowing the next player to move.
            password = ""
            while not self.players[self._current_player][0].login(password):
                password = input(self.players[self._current_player][0].name() +
                                 ", your move. Enter password: ")

            # Set the other player as an enemy
            enemy = abs(self._current_player - 1)
            print("Your field:\n",
                  self.players[self._current_player][1].field_with_ships())
            print("Enemy's field:\n",
                  self.players[enemy][1].field_without_ships())

            left = self.players[enemy][1].shoot_at(self.players[
                                self._current_player][0].read_position())

            if left == 0:
                if self.players[enemy][2] > 0:
                    self.players[enemy][2] -= 1
                    print("Ship destroyed!")
                    if self.players[enemy][2] == 0:
                        print("Congrats, {}, you are the winner!".format(
                        self.players[enemy][0].name()))
                        print("Your field:\n",
                              self.players[self._current_player][1].
                              field_with_ships())
                        print("Enemy's field:\n",
                              self.players[enemy][1].field_without_ships())
                        print("Bye!")

            elif left in [1, 2, 3]:
                print("Ship hurted! Hold on!")
            elif left == -1:
                print("Epic fail. You have already shoot there. Try again.")
            elif left is None:
                print("Not that way..")
                self._current_player = enemy
