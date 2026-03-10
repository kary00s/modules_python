def get_content(name: str) -> None:
    try:
        file = open(name, "r")
        file_content = file.read()
        print("\nRECOVERED DATA:\n")
        print(file_content)
        file.close()
    except IsADirectoryError:
        print("\nERROR: cant read from directory")
    except IOError:
        print("\nERROR: Unable to access storage vault")
    except FileNotFoundError:
        print(f"\nERROR: file not found (file : {name}).")
    except PermissionError:
        print("\nERROR: No permission to read this file.")


def main() -> None:

    name = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print(f"\nAccessing Storage Vault: {name}")
        print("Connection established...")
        get_content(name)
    except Exception as e:
        print(e)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
