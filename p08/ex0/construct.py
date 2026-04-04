

import sys
import os
import sysconfig

def outside() -> None:
    print("MATRIX STATUS: You're still plugged in")

    path = sys.executable
    print("\nCurrent Python: ", path)
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\Scripts\\activate # On Windows")
    print("\nThen run this program again.")

def inside() -> None:

    print("MATRIX STATUS: Welcome to the construct")
    current_path = sys.executable
    venv_name = os.path.basename(venv_path)
    venv_path = os.environ.get('VIRTUAL_ENV')
    environment_path = sys.prefix

    print("\nCurrent Python: ", current_path)
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {environment_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print(sysconfig.get_paths()["purelib"])


if __name__ == "__main__":
    try:
        '''
            os.environ => dictionary of ALL your system's environment variables
        '''     
        if os.environ.get('VIRTUAL_ENV'):
            inside()
        else:
            outside()
    except Exception as e:
        print(e)
