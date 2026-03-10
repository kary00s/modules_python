def extraction(file_name):
    print("SECURE EXTRACTION:")
    with open(file_name, "r") as f:
        data = f.read()
        print(data)


def preservation(file_name):
    print("\nSECURE PRESERVATION:")
    data = "[CLASSIFIED] New security protocols archived"
    with open(file_name, "w") as f:
        f.write(data)
        print(data)
        print("Vault automatically sealed upon completion")


def main():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        file_name = "extraction.txt"
        extraction(file_name)
        file_name = "preservation.txt"
        preservation(file_name)
    except Exception as e:
        print(e)

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
