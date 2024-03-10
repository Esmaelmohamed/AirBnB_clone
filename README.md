# HBnB (HomeBnB) Project

HBnB (HomeBnB) is a project aimed at creating a simplified version of the Airbnb platform, allowing users to manage and book accommodations. The project consists of a command-line interface (CLI) for managing data and interacting with the system.

## Command Interpreter

### How to Start

To start the HBnB command interpreter, follow these steps:

1. Clone the HBnB repository to your local machine.
2. Navigate to the root directory of the project.
3. Run the `console.py` file using Python 3.

```bash
python3 console.py

How to Use
Once the command interpreter is started, you can interact with it using various commands. Here are the available commands and their usage:

create: Create a new instance of a class. 
(hbnb) create BaseModel

show: Display the string representation of an instance. 
(hbnb) show BaseModel 1234-5678

destroy: Delete an instance based on the class name and ID.
(hbnb) destroy BaseModel 1234-5678

all: Display all instances of a class.
(hbnb) all BaseModel

update: Update an instance with new information.
(hbnb) update BaseModel 1234-5678 name "New Name"

