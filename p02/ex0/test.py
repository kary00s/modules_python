e = Exception()


def display():
    try:
        nbr = int(input("print nbr"))
    except ValueError:
        ("=>   error value error <=")
        print("=>   error the print error <=")

display()
