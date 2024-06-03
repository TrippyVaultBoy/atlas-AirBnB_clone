# <p align="center">AirBnB Clone - The Console</p>

## :bookmark: Table of Contents
<details>
        <summary>
        CLICK TO ENLARGE :star2:
        </summary>
        :dart: <a href="#objective">Objective</a>
        <br>
        :shell: <a href="#description">Description</a>
        <br>
        :clipboard: <a href="#requirements">Requirements</a>
        <br>
        :floppy_disk: <a href="#compilation/installation">Compilation/Installation</a>
        <br>
        :ocean: <a href="#flowcharts">Flowcharts</a>
        <br>
        :computer: <a href="#testing">Testing</a>
        <br>
        :sparkles: <a href="#authors">Authors</a>
</details>

## :dart: <span id="objective">Objective</span>
To write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## :shell: <span id="description">Description</span>

The AirBnB clone: The console project is the initial step in creating a Python-based application that emulates the functionality of the AirBnB website. The primary objective of this project is to develop a command-line interpreter (CLI) that enables users to manage various objects within the application.
<br><br>
To support this, the project requires the implementation of the following key components:
- BaseModel Class
- Serialization & Deserialization Flow
- Object Classes
- File Storage Engine

## :clipboard: <span id="requirements">Requirements</span>
- Allowed editors: **vi, vim, emacs**
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly **#!/usr/bin/python3**
- A **README.md** file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using **wc**
- All your modules should have a documentation **(python3 -c 'print(__import__("my_module").__doc__)')**
- All your classes should have a documentation **(python3 -c 'print(__import__("my_module").MyClass.__doc__)')**
- All your functions (inside and outside a class) should have a documentation **(python3 -c 'print(__import__("my_module").my_function.__doc__)'** and **python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')**
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## :floppy_disk: <span id="compilation/installation">Compilation/Installation</a>

To start the AirBnB Clone command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/TrippyVaultBoy/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the commande interpreter:
   ```bash
   ./console.py
   ```

### How to Use
Once the command interpreter is running, you can use various commands to interact with the AirBnB Clone system. Here are some common commands:

* `create`: Create a new property or user.
* `show`: Display details of a property or user.
* `all`: List all properties or users.
* `book`: Book a property for a specific date range.
* `quit`: Exit the command interpreter.
For detailed information on available commands and their usage, you can use the help command within the interpreter.

**Examples**
Here are some examples of how to use the AirBnB Clone command interpreter:
1. Creating a new property:
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
2. Showing instance:
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
3. Listing all instances:
```bash
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```
## :ocean: <span id="flowcharts">Flowcharts</a>

![Image](/flowchart.png)

## :computer: <span id="testing">Testing</a>

## :sparkles: <span id="authors">Authors</span>
**Tanner Saint**
- Github: [@TrippyVaultBoy](https://github.com/TrippyVaultBoy)

**Jaylen Perez**
- Github: [@Jaylenperez](https://github.com/Jaylenperez)