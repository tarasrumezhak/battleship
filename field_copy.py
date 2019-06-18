class Field:
    def __init__(self, ships):
        self.__ships = ships
        self.combo = 0
        self.water = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
        self.hiden_water = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

    def set_ships(self):
        for ship in self.__ships:
            for coord in reversed(ship.coords):
                self.water[coord[0]-1][coord[1]-1] = "+"
    def shoot_at(self, coords):
        if self.water[coords[1]-1][coords[0]-1] == "+":
            self.hiden_water[coords[1]-1][coords[0]-1] = "X"
            self.combo = self.combo + 1
        elif self.hiden_water[coords[1]-1][coords[0]-1] == "~":
            self.hiden_water[coords[1]-1][coords[0]-1] = "o"

    def field_without_ships(self):
        return self.hiden_water

if __name__ == "__main__":
    import random
    from ship import Ship
    def generate_ship(length):
        x = random.randint(1, 11)
        y = random.randint(1, 11)
        horizontal = random.choice([True, False])
        return Ship((x, y), horizontal, length)
    def place_ship(field):
        ship1 = generate_ship(4)
        try:
            field._Field__ships.append(ship1)
            field.set_ships()
        except:
            return place_ship(field)


    field1 = Field([])
    place_ship(field1)
    print("   a b c d e f g h i j".upper())
    for digit, line in enumerate(field1.water, 1):
        print("{:<3}".format(digit) + " ".join(line))
