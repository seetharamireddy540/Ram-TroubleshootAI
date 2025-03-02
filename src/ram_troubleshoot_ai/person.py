
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person = Person("Alice", 30)
print(person)
person.greet()

if __name__ == "__main__":
    person = Person("Alice", 30)
    print(person)
    person.greet()
