def get_value_error():
    list = ["12", "100", "abc"]
    return list

def get_zero_div_error():
    number = 0
    42 / number

def get_file_error():
    f = open("missing.txt", "r")
    print(f.read())
def get_key_error():
    dic = {
        "rose" : "red",
        "oak" : "pink",
        "jasmine" : "white"
    }
    return dic

def garden_operations(type):
    if type == "ValueError":
        try:
            list = get_value_error()
            for number in list:
                int(number)
        except ValueError:
            print("Caught ValueError: invalid literal for int()")

    elif type == "ZeroDivisionError":
        try:
            get_zero_div_error()
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")

    elif type == "FileNotFoundError":
        try:
            get_file_error()
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")

    elif type == "KeyError":
        try:
            plants = get_key_error()
            print(plants['missing'])
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")


def test_error_types():
    list = [
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError"
    ]
    print("=== Garden Error Types Demo ===\n")
    for e in list:
        print(f"\ntesting {e} ...")
        try:
            garden_operations(e)
        except Exception as e:
            print(e)
    print("\nAll error types tested successfully!")
if __name__ == "__main__":
    test_error_types()