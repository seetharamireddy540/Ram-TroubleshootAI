import platform
import sys


def add(a: int, b: int) -> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a + b


def main():
    print(sys.implementation.name)
    print(sys.version)
    print(platform.python_implementation())
    print("Hello World!")
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")


if __name__ == "__main__":
    main()

# %%
