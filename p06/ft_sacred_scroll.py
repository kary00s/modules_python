import alchemy


def main():
    print("=== Sacred Scroll Mastery ===")
    print("\nTesting direct module access:")

    direct_access_fire = alchemy.elements.create_fire()
    direct_access_water = alchemy.elements.create_water()
    direct_access_earth = alchemy.elements.create_earth()
    direct_access_air = alchemy.elements.create_air()

    print(f"alchemy.elements.create_fire(): {direct_access_fire}")
    print(f"alchemy.elements.create_water(): {direct_access_water}")
    print(f"alchemy.elements.create_earth(): {direct_access_earth}")
    print(f"alchemy.elements.create_air(): {direct_access_air}")

    print("\nTesting package-level access (controlled by __init__.py):")
    
    try:
        package_access_fire = alchemy.create_fire()
        print(f"alchemy.elements.create_fire(): {package_access_fire}")
    except AttributeError:
        print("AttributeError - not exposed")
    
    try:
        package_access_water = alchemy.create_water()
        print(f"alchemy.elements.create_water(): {package_access_water}")
    except AttributeError:
        print("AttributeError - not exposed")
    
    try:
        package_access_earth = alchemy.create_earth()
        print(f"alchemy.elements.create_earth(): {package_access_earth}")
    except AttributeError:
        print("AttributeError - not exposed")
    
    try:
        package_access_air = alchemy.create_air()
        print(f"alchemy.elements.create_air(): {package_access_air}")
    except AttributeError:
        print("AttributeError - not exposed")
    
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)