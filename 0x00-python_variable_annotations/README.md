ype annotations in Python 3 allow you to specify the types of variables, function parameters, and return values. They provide a way to document the expected types in your code, which can improve readability and catch certain errors early on. Here's how you can use them:

Specifying Variable Types:
python
Copy code
age: int = 25
name: str = "John"
Function Signatures:
python
Copy code
def greet(name: str) -> str:
    return "Hello, " + name
Here, name: str indicates that the parameter name should be a string, and -> str specifies that the function returns a string.
Duck Typing:
Duck typing in Python refers to the practice of not checking the type of an object directly but instead checking for the presence of certain methods or behaviors. While type annotations can help document expected types, Python is still dynamically typed, meaning that you can often pass different types to functions as long as they support the required operations. For example:
python
Copy code
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm not a duck but I can imitate one!")

def make_sound(entity):
    entity.quack()

donald = Duck()
john = Person()

make_sound(donald)  # Outputs: Quack!
make_sound(john)    # Outputs: I'm not a duck but I can imitate one!
Validating with Mypy:
Mypy is a static type checker for Python that can analyze your code and verify that the types are used correctly. After installing it (typically via pip install mypy), you can run it on your Python files:
bash
Copy code
mypy your_file.py
Mypy will report any type-related errors it finds in your code. For example, if you try to use a variable in a way that violates its annotated type, Mypy will raise an error.
By combining type annotations with tools like Mypy, you can catch type-related errors early in development and write more robust code.
