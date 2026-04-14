from functools import wraps
from typing import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"Spell completed in {(end - start):.3f} seconds")
        print(f"Result: {result}")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[1] if len(args) > 1 else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(
                        f"Spell failed, retrying... (attempt {attempt}/{max_attempts})"
                    )

            print(f"Spell casting failed after {max_attempts} attempts")
            raise last_error

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        elif not all(c.isalpha() or c.isspace() for c in name):
            return False
        else:
            return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(max_attempts=5)
def Testing_retrying_spell(base):
    i = 0
    while i < base:
        i += 1
        raise Exception("Waaaaaaagh spelled !")


@spell_timer
def Testing_spell_timer():
    time.sleep(1)
    return "Fireball cast!"


def Testing_MageGuild(power_test):
    print(MageGuild.validate_mage_name("karim"))
    print(MageGuild.validate_mage_name("fk"))
    guild = MageGuild()
    output = guild.cast_spell(spell_name="Fireball", power=power_test)
    print(output)


def main():

    print("Testing spell timer...")
    Testing_spell_timer()

    print("\nTesting MageGuild...")
    Testing_MageGuild(15)

    print("\nTesting retrying spell...")
    Testing_retrying_spell(3)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
