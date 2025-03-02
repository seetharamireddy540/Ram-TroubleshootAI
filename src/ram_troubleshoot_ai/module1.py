import sys
import platform


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
    

