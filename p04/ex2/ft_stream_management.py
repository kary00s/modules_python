import sys


def writer(stdout: any, stderr: any, id: str, status: str) -> None:
    stdout.write(f"\n[STANDARD] Archive status from {id}: {status}\n")

    stderr.write("[ALERT] System diagnostic: Communication channels "
                 "verified\n")

    stdout.write("[STANDARD] Data transmission complete\n")


def main() -> None:

    stdout = sys.stdout
    stderr = sys.stderr

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    try:
        writer(stdout, stderr, id, status)
    except Exception as e:
        print(e)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
