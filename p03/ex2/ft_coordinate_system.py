import math

def ft_coordinate_system():
    args = sys.argv
    i = 1
    lst = []
    while  i < len(args):
        lst.append(args[i])
        i += 1
    print(lst)

ft_coordinate_system()