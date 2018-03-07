from field import Field
from player import Player


class Game:
    def __init__(self):
        f0, f1 = Field(), Field()

        n0 = input("Player 1, please enter your name: ")
        pswd0 = input("{}, please create password: ".format(n0))
        p0 = Player(name=n0, password=pswd0)

        n1 = input("Player 2, please enter your name: ")
        pswd1 = input("{}, please create password: ".format(n1))
        p1 = Player(name=n1, password=pswd1)

        self.players = {0: (p0, f0), 1: (p1, f1)}
        self._current_player = 0

    def run(self):
        while (self.players[0][1].present_ships() > 0 and
                       self.players[1][1].present_ships() > 0):

            password = ""
            while not self.players[self._current_player][0].login(password):
                password = input(self.players[self._current_player][0].name() +
                                 ", your move. Enter password: ")
            enemy = abs(self._current_player - 1)
            print("Your field:\n",
                  self.players[self._current_player][1].field_with_ships())
            print("Enemy's field:\n",
                  self.players[enemy][1].field_without_ships())

            left = self.players[enemy][1].shoot_at(self.players[
            self._current_player][0].read_position())

            if left == 0:
                if (self.players[0][1].present_ships() > 0 and
                            self.players[1][1].present_ships() > 0):
                    print("Ship destroyed!")
                else:
                    print("Congrats, winner!")
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
