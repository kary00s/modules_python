
def cheacker_file(file_name: str, mode: str) -> None:

    try:
        if mode == "r":
            with open(file_name, "r") as file:
                file.read()
        elif mode == "w":
            with open(file_name, "w"):
                pass
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")

        print("SUCCESS: Archive recovered - "
              "''Knowledge preserved for humanity''")

        print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as error:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print(f"Unexpected error during {mode}: {error}\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    cheacker_file("lost_archive.txt", "r")
    cheacker_file("classified_vault.txt", "w")
    cheacker_file("standard_archive.txt", "r")


if __name__ == "__main__":
    try:
        main()
        print("All crisis scenarios handled "
              "successfully. Archives secure.")
    except Exception as e:
        print(e)
        print("One of crisis scenarios failed")
