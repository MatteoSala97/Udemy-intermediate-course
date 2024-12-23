'''
Program #1: Creating a class

1. Create a class named Person
2. Its properties are name and age (initialize the value using the constructor)
3. Create a method, greeting, which will display the name and age properties
4. Create an instance of the Person class
5. Call the method created of the class


Program #2: Operator Overloading

1. Create a class named Book
2. Its properties are name and pages
3. Given two Book objects, we want to add the two objects with the + operator
4. Print the total number of pages for the objects

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
person1 = Person("Alice", 30)

person1.greet()



class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        
    def display(self):
        print(f"Book's name is {self.name} and it has {self.pages} pages.")
        
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
        
book1 = Book('Harry Potter 1', 500)
book2 = Book('Harry Potter 2', 500)

# book1.display()
total_pages = book1 + book2

print(f"The total number of pages in both books is: {total_pages}")