import math

def get_cordinates(cordinate: list):
    x = cordinate[0]
    y = cordinate[1]
    z = cordinate[2]
    return x, y, z

def creator(cordinate: list):
    x, y, z = get_cordinates(cordinate)
    print(f"Position Created : ({x}, {y}, {z})")

def calculator(cor1, cor2=(0, 0, 0)):
    x1, y1, z1 = get_cordinates(cor1)
    x2, y2, z2 = get_cordinates(cor2)

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between ({x2}, {y2}, {z2}) and "
        f"({x1}, {y1}, {z1}): {distance}")

def check_cordinates(cordinate):
    for position in cordinate:
        if int(position):
            pass
        else:
            raise ValueError("Error parsing coordinates: invalid"
                            f"literal for int() with base 10: {position}")


def Parsing(position: str):
    cordinate = position.split(",")
    try:
        check_cordinates(cordinate)
    except ValueError as error:
        print(error)
    return cordinate


def ft_coordinate_system(cordinate: str):
    cordinate_list = Parsing(cordinate)
    

def test_cordinates():
    ## test without parsing   (10, 20, 5)

    ft_coordinate_system("4,46,6")
test_cordinates()