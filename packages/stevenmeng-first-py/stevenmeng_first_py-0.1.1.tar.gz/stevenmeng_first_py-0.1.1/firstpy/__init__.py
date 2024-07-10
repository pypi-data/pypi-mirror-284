# my_awesome_package/__init__.py

class HelloWorld:
    def __init__(self):
        self.message = "Hello, World!"
    
    def say_hello(self):
        print(self.message)

def greet(name):
    return f"Hello, {name}!"
