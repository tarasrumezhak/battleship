from ship import Ship
from field import Field
from player import Player
import random

class Game:
    @staticmethod
    def start():
        print("Welcome to the game Battlefirst_ship")

        name1 = input("Write the name of the first player: ")
        name2 = input("Write the name of the second player: ")

        player1 = Player(name1)
        player2 = Player(name2)

        def place_ship(field, length):
            x = random.randint(1, 11)
            y = random.randint(1, 11)
            horizontal = random.choice([True, False])

            return Ship((x, y), horizontal, length)

        # first_ship_4 = Ship((1,1), True, 4)
        # first_ship_3_1 = Ship((6,1), False, 3)
        # first_ship_3_2 = Ship((2,3), True, 3)
        # first_ship_2_1 = Ship((8,2), True, 2)
        # first_ship_2_2 = Ship((2,5), False, 2)
        # first_ship_2_3 = Ship((4,5), False, 2)
        # first_ship_1_1 = Ship((3,8), True, 1)
        # first_ship_1_2 = Ship((7,6), True, 1)
        # first_ship_1_3 = Ship((8,8), True, 1)
        # first_ship_1_4 = Ship((5,9), True, 1)
        #
        # second_ship_4 = Ship((7,7), False, 4)
        # second_ship_3_1 = Ship((2,2), True, 3)
        # second_ship_3_2 = Ship((8,5), True, 3)
        # second_ship_2_1 = Ship((6,2), True, 2)
        # second_ship_2_2 = Ship((9,1), False, 2)
        # second_ship_2_3 = Ship((3,4), False, 2)
        # second_ship_1_1 = Ship((3,7), True, 1)
        # second_ship_1_2 = Ship((5,4), True, 1)
        # second_ship_1_3 = Ship((2,9), True, 1)
        # second_ship_1_4 = Ship((9,8), True, 1)
        #
        #
        #
        # first_ships = [first_ship_2_1, first_ship_2_2, first_ship_2_3, first_ship_3_1, first_ship_3_2, first_ship_4,
        #                first_ship_1_1, first_ship_1_2, first_ship_1_3, first_ship_1_4]
        # second_ships = [second_ship_1_1, second_ship_1_2, second_ship_1_3, second_ship_1_4, second_ship_2_1, second_ship_2_2,
        #                 second_ship_2_3, second_ship_3_1, second_ship_3_2, second_ship_4]

        current_player = player1

        field1 = Field([])

        field2 = Field([])

        def place_ship(field, length):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            horizontal = random.choice([True, False])
            ship = Ship((x, y), horizontal, length)
            # print(ship.coords)
            x_coords = []
            y_coords = []
            for (x_1, y_1) in ship.coords:
                # print(x_1, y_1)
                x_coords.append(x_1)
                y_coords.append(y_1)
            # print(x_coords)
            for i in x_coords:
                if i > 10:
                    return place_ship(field, length)
            for j in y_coords:
                if j > 10:
                    return place_ship(field, length)
            for (x1, y1) in ship.coords:
                # print("Hello", x1, y1)
                if field.water[x1 - 1][y1 - 1] == "+" or field.water[x1 - 1][y1 - 1] == "*":
                    return place_ship(field, length)
            field._Field__ships.append(ship)
            field.set_ships()

        place_ship(field1, 4)
        place_ship(field1, 3)
        place_ship(field1, 3)
        place_ship(field1, 2)
        place_ship(field1, 2)
        place_ship(field1, 2)
        place_ship(field1, 1)
        place_ship(field1, 1)
        place_ship(field1, 1)
        place_ship(field1, 1)

        place_ship(field2, 4)
        place_ship(field2, 3)
        place_ship(field2, 3)
        place_ship(field2, 2)
        place_ship(field2, 2)
        place_ship(field2, 2)
        place_ship(field2, 1)
        place_ship(field2, 1)
        place_ship(field2, 1)
        place_ship(field2, 1)

        def output1(name, field):
            print("Field of player {}".format(name))
            print("   a b c d e f g h i j".upper())
            for digit, line in enumerate(field.water, 1):
                print("{:<3}".format(digit) + " ".join(line).replace("*", "~"))

        def hiden_output(name, field):
            print("Field of player {}".format(name))
            print("   a b c d e f g h i j".upper())
            for digit, line in enumerate(field.field_without_ships(), 1):
                print("{:<3}".format(digit) + " ".join(line))

        running = True
        while running:
            if current_player == player1:
                output1(name1, field1)

                hiden_output(name2, field2)

                hits_count = field2.combo
                field2.shoot_at(player1.read_position())
                current_hits = field2.combo

                hiden_output(name2, field2)

            else:
                output1(name2, field2)

                hiden_output(name1, field1)

                hits_count = field1.combo
                field1.shoot_at(player1.read_position())
                current_hits = field1.combo
                hiden_output(name1, field1)
            if current_hits > hits_count:
                current_player = current_player
            else:
                if input("Next player? (y/n): ") == "y":
                    if current_player == player1:
                        current_player = player2
                    else:
                        current_player = player1
                    print("\n\n===========================\n\n")
                    print("\n\n===========================\n\n")

            if field1.combo == 20:
                print("{} wins!".format(name2))
                running = False
            elif field2.combo == 20:
                print("{} wins!".format(name1))
                running = False
if __name__ == "__main__":
    game = Game()
    game.start()