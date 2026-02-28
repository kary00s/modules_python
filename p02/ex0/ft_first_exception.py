def check_temperature(temp_str: str) -> None:
    try:
        temperature = int(temp_str)
        return temperature
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def is_it_valid(temperature: int) -> None:
    if temperature > 40:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")

    elif temperature < 0:
        print(f"Error: {temperature}°C is too cold for plants (max 0°C)\n")

    else:
        print(f"Temperature {temperature}°C is perfect for plants!\n")


def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===\n")
    list = ["25", "abc", "100", "-50"]
    for nbr in list:
        print(f"test tempreture : {nbr}")
        temperature = check_temperature(nbr)
        if temperature is not None:
            is_it_valid(temperature)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
