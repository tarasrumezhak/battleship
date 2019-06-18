class Player:
    def __init__(self, name):
        self.__name = name
    @staticmethod
    def read_position():
        dct = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
        print("Write the coordinates to hit: ")
        x = input("letter: ").upper()
        try:
            y = int(input("digit: "))
        except:
            print("Incorrect input!")
            return Player.read_position()
        if x in dct.keys() and y in range(1, 11):
            x = dct[x]
            return x, y
        else:
            print("Incorrect input!")
            return Player.read_position()


if __name__ == "__main__":
    pl1 = Player("Taras")
    print(pl1.read_position())
