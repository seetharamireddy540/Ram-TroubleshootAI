def add(a: int, b: int) -> int:
    return a + b


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")


def main():
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")


if __name__ == "__main__":
    main()
