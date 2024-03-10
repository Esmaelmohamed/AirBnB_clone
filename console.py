#!/usr/bin/python3
"""HBnB console module - contains the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(arg_string):
    """Parse arguments and return a list."""
    curly_braces = re.search(r"\{(.*?)\}", arg_string)
    brackets = re.search(r"\[(.*?)\]", arg_string)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg_string)]
        else:
            lexer = split(arg_string[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg_string[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBnBConsole(cmd.Cmd):
    """HBnB command console class.

    Attributes:
        prompt (str): The command prompt.
        available_classes (set): Set containing all available class names.
    """

    prompt = "(hbnb) "
    available_classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg_string):
        """Handle unknown commands."""
        command_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg_string)
        if match is not None:
            arg_list = [arg_string[:match.span()[0]], arg_string[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_map.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return command_map[command[0]](call)
        print("*** Unknown syntax: {}".format(arg_string))
        return False

    def do_quit(self, arg_string):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg_string):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg_string):
        """Create a new instance of BaseModel."""
        arg_list = parse_arguments(arg_string)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBnBConsole.available_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg_string):
        """Display the string representation of an instance."""
        arg_list = parse_arguments(arg_string)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBnBConsole.available_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg_string):
        """Delete an instance based on the class name and id."""
        arg_list = parse_arguments(arg_string)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBnBConsole.available_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg_string):
        """Display all instances of a class."""
        arg_list = parse_arguments(arg_string)
        if len(arg_list) > 0 and arg_list[0] not in HBnBConsole.available_classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    object_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    object_list.append(obj.__str__())
            print(object_list)

    def do_count(self, arg_string):
        """Count the number of instances of a class."""
        arg_list = parse_arguments(arg_string)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg_string):
        """Update an instance with new information."""
        arg_list = parse_arguments(arg_string)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBnBConsole.available_classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = value_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for key, value in eval(arg_list[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBnBConsole().cmdloop()

