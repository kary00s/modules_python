def harvest() -> None:
    days = int(input("Days until harvest : "))

    def harvest_recur(i=0):
        if i == days:
            print("harvest time .")
        else:
            print(f"day {i + 1}")
            harvest_recur(i + 1)

    harvest_recur()
