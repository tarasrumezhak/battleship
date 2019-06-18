class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [i*0 for i in range(self.__length)]
        if self.horizontal:
            self.coords = [(self.bow[1], self.bow[0] + i) for i in range(self.__length)]
            self.surroundings = [(self.bow[1] + 1, self.bow[0] + i) for i in range(-1, self.__length + 1)]
            self.surroundings += [(self.bow[1] - 1, self.bow[0] + i) for i in range(-1, self.__length + 1)]
            self.surroundings += [(self.bow[1], self.bow[0] + i) for i in [-1, self.__length]]
        else:
            self.coords = [(self.bow[1] + i, self.bow[0]) for i in range(self.__length)]
            self.surroundings = [(self.bow[1] + i, self.bow[0] + 1) for i in range(-1, self.__length + 1)]
            self.surroundings += [(self.bow[1] + i, self.bow[0] - 1) for i in range(-1, self.__length + 1)]
            self.surroundings += [(self.bow[1] + i, self.bow[0]) for i in [-1, self.__length]]

    def shoot_at(self, coords):
        if reversed(coords) in self.coords:
            index = self.coords.index(reversed(coords))
            self.__hit[index] = "X"
    @staticmethod
    def surr_dot_coords(x, y):
        coords = []
        coords.append((x+1, y))
        coords.append((x-1, y))
        coords.append((x + 1, y + 1))
        coords.append((x + 1, y - 1))
        coords.append((x - 1, y + 1))
        coords.append((x - 1, y - 1))
        coords.append((x, y + 1))
        coords.append((x, y - 1))
        return coords





if __name__ == "__main__":
    ship = Ship((4,3), True, 2)
    print(ship.coords)
    print(ship.surroundings)
    ship.shoot_at((1,1))
    print(ship._Ship__hit)
    print(ship.surr_dot_coords(3, 7))