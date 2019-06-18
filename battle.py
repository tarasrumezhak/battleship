def read_field(filename):
    """
    Function to read the current state of field
    """
    field = []
    with open(filename) as f:
        field_lines = f.readlines()
    for line in field_lines:
        line_data = []
        for j in line:
            line_data.append(j)
        line_data = line_data[:-1]
        for i in range(10 - len(line_data)):
            line_data.append(' ')
        field.append(line_data)
    return field
# print("".join(read_field("field.txt")))
print(read_field("field.txt"))

def has_ship(data, tup):
    """
    Return True if current cell has a ship
    and False otherwise
    """
    dct = {"A":1,"B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "J":8, "K":9, "L":10}
    if data[dct[tup[0]]-1][tup[1]-1] == "*":
        return True
    else:
        return False

data = read_field("field.txt")
print(has_ship(data, ("A", 3)))

