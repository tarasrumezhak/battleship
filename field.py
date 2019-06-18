class Field:
    def __init__(self, ships):
        self.__ships = ships
        self.combo = 0
        # self.water_line = ["~"]*10
        # self.water = []
        # for i in range(10):
        #     self.water.append(self.water_line)
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
            for coord2 in reversed(ship.surroundings):
                # print("=========", coord2[0] - 1, coord2[1] - 1)
                if (coord2[0] - 1) in range(10) and (coord2[1] - 1) in range(10):
                    self.water[coord2[0] - 1][coord2[1] - 1] = "*"
                else:
                    pass
    def shoot_at(self, coords):
        destroy = False
        if self.water[coords[1]-1][coords[0]-1] == "+":
            self.hiden_water[coords[1]-1][coords[0]-1] = "X"
            self.water[coords[1] - 1][coords[0] - 1] = "X"
            self.combo = self.combo + 1
            coords_dot = Field.surr_dot_coords(coords[1]-1, coords[0]-1)
            coords_signs = []
            for (x, y) in coords_dot:
                try:
                    coords_signs += self.water[x][y]
                except:
                    pass
            for i in range(len(coords_dot)):
                if "+" not in coords_signs:
                    destroy = True
            if destroy:
                print("\nYou destroyed the ship!\n")
                # for (x_1, y_1) in coords_dot:
                #     try:
                #         self.hiden_water[x_1][y_1] = "0"
                #     except:
                #         pass

        elif self.hiden_water[coords[1]-1][coords[0]-1] == "~":
            self.hiden_water[coords[1]-1][coords[0]-1] = "o"

    # def show_destroyed(self):


    # def check_destroy(self):
    #     for ship in self.__ships:
    #         for (x, y) in reversed(ship.coords):
    #             if self.water[x-1][y-1] == "X":
    # @staticmethod
    # def surr_dot_coords(x, y):
    #     coords = []
    #     coords.append((x + 1, y))
    #     coords.append((x - 1, y))
    #     coords.append((x + 1, y + 1))
    #     coords.append((x + 1, y - 1))
    #     coords.append((x - 1, y + 1))
    #     coords.append((x - 1, y - 1))
    #     coords.append((x, y + 1))
    #     coords.append((x, y - 1))
    #     return coords



    def field_without_ships(self):
        return self.hiden_water

    @staticmethod
    def surr_dot_coords(x, y):
        coords = []
        coords.append((x + 1, y))
        coords.append((x - 1, y))
        coords.append((x + 1, y + 1))
        coords.append((x + 1, y - 1))
        coords.append((x - 1, y + 1))
        coords.append((x - 1, y - 1))
        coords.append((x, y + 1))
        coords.append((x, y - 1))
        return coords

if __name__ == "__main__":
    import random
    from ship import Ship

    def generate_ship(length):
        x = random.randint(1, 11)
        y = random.randint(1, 11)
        horizontal = random.choice([True, False])
        return Ship((x, y), horizontal, length)
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
            if field.water[x1-1][y1-1] == "+" or field.water[x1-1][y1-1] == "*":
                return place_ship(field, length)

        field._Field__ships.append(ship)
        field.set_ships()






    field1 = Field([])
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
    print("   a b c d e f g h i j".upper())
    for digit, line in enumerate(field1.water, 1):
        print("{:<3}".format(digit) + " ".join(line).replace("*", "~"))
