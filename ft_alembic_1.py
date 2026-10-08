import alchemy


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reched")
    print("This will raise an exception!")
    print(f"Testing the hidden create_earth: ", end="")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError as e:
        print(f"AttributeError: {e}")
