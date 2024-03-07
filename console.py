import cmd
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB console."""
    prompt = "(hbnb) "
    file_storage = FileStorage()
    file_storage.reload()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = HBNBCommand.file_storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = HBNBCommand.file_storage.all()
        if key in all_objects:
            del all_objects[key]
            HBNBCommand.file_storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        if arg not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        all_objects = HBNBCommand.file_storage.all()
        for key, obj in all_objects.items():
            if arg == "User" and isinstance(obj, User):
                print(obj)
            elif arg == "BaseModel" and not isinstance(obj, User):
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = HBNBCommand.file_storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        obj = all_objects[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        setattr(obj, attribute_name, value)
        obj.save()

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
