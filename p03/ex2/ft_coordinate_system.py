import math


def position_creator(x: int, y: int, z: int) -> tuple:
    return (x, y, z)


def distance_calculator(point1: tuple, point2: tuple) -> int:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def ft_len(lst: list) -> int:
    counter = 0
    for i in lst:
        counter += 1
    return counter


def parser(coord_string: str) -> tuple:
    parts = coord_string.split(',')
    if ft_len(parts) != 3:
        raise ValueError("Coordinate string must contain exactly 3 values")
    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return position_creator(x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def main() -> None:

    print("=== Game Coordinate System ===\n")

    pos1 = position_creator(10, 20, 5)
    origin = position_creator(0, 0, 0)

    print(f"Position created: {pos1}")
    dist1 = distance_calculator(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}\n")

    print('Parsing coordinates: "3,4,0"')
    pos2 = parser("3,4,5,0")
    if pos2:
        print(f"Parsed position: {pos2}")
        dist2 = distance_calculator(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2:.1f}\n")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    parser("abc,def,ghi")
    print("\nUnpacking demonstration:")

    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(e)
