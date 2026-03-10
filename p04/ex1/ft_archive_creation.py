def main() -> None:
    file_name = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    data = ["[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee\n"
            ]
    file = open(file_name, "w")
    for item in data:
        print(item, end="")
        file.write(item)
    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
