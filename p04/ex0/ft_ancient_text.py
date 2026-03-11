def get_data(name: str) -> None:
    try:
        file = open(name, "r")
        file_data = file.read()
        print("\nRECOVERED DATA:\n")
        print(file_data)
        file.close()
    except IOError:
        print("\nERROR: Storage vault not found.")
    except FileNotFoundError:
        print(f"\nERROR: file not found (file : {name}).")
    except PermissionError:
        print("\nERROR: No permission to read this file.")
    except IsADirectoryError:
        print("\nERROR: cant read from directory")


def main() -> None:

    file_name = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print(f"\nAccessing Storage Vault: {file_name}")
        print("Connection established...")
        get_data(file_name)
    except Exception as e:
        print(e)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
