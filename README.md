CS 340 CRUD README
About the Project

The CRUD Python module is designed to provide basic functionalities for creating, reading, updating, and deleting records in a MongoDB database. This module is part of an ongoing project to streamline database interactions and improve code reusability across Python projects, facilitating easier management of data operations.

Motivation

The motivation behind developing this CRUD Python module is to simplify the complexities involved in database operations. By abstracting CRUD functionalities into a reusable module, developers can focus more on business logic and less on underlying database handling, thereby enhancing productivity and code maintenance.

Getting Started

Prerequisites
Before you can use the CRUD Python module, ensure you have the following installed:
• Python 3.x
• MongoDB
• pymongo Python library
Setup
1.	Clone the repository from GitHub.
git clone <repository-url>

2.	Install the required dependencies using pip: pip install -r requirements.txt.
pip install pymongo


Installation

This CRUD Python module leverages several tools:
• Python 3: A powerful programming language used to create the module.
• MongoDB: A NoSQL database used to store and manage your application's data.
• PyMongo: A Python library providing tools for working with MongoDB from Python.

Why These Tools?
• Python 3 is chosen for its simplicity and the powerful ecosystem of data handling libraries.
• MongoDB offers flexible data structures, scalability, and is widely adopted for modern web applications.
• PyMongo is the standard MongoDB driver for Python, which simplifies performing database operations.

Usage
Here's how to use the CRUD Python module to perform database operations:

from AnimalShelter import AnimalShelter

# Creating an instance of the class
shelter = AnimalShelter()

# Creating a new document in the database
shelter.create({"name": "Max", "type": "Dog", "age": 5})

# Reading documents from the database
documents = shelter.read({"type": "Dog"})
print(documents)

# Deleting a document from the database
shelter.delete({"name": "Max", "type": "Dog"})

Code Example

Creating a Record:
shelter.create({"name": "Bella", "type": "Cat", "age": 3})

Reading Records:
cats = shelter.read({"type": "Cat"})
print(cats)



Screenshots

 

Contact
Jonathan M. Walker
Jonathan.walker4@snhu.edu
https://github.com/oQuickZzz
