#!/usr/bin/python3
"""
Includes HBNBCommand class
"""
import cmd
from models.base_model import BaseModel
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb)"

    classes = {
        'BaseModel': BaseModel,
    }

    def emptyline(self):
        """
        Over writes the emptyline method
        """
        pass


    def do_quit(self, arg):
        """
        Exits the program
        """
        return True


    def do_EOF(self, arg):
        """
        Exits the program
        """
        return True
    

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)
            return


    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id
        """
        show_args = args.split(' ')

        if len(show_args) < 1:
            print("** class name missing **")
        else:
            class_name = show_args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        
        if len(show_args) < 2:
            print("** instance id missing **")
            return False
        else:
            instance_id = show_args[1]

        key = class_name + "." + instance_id
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")
            return False


    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        destroy_args = args.split(' ')

        if len(destroy_args) < 1:
            print("** class name missing **")
        else:
            class_name = destroy_args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        
        if len(destroy_args) < 2:
            print("** instance id missing **")
            return False
        else:
            instance_id = destroy_args[1]

        key = class_name + "." + instance_id
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")
            return False
        

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        pass


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        attributes = [
            "id",
            "created_at",
            "updated_at",
        ]
        update_args = args.split(' ')

        if len(update_args) < 1:
            print("** class name missing **")
            return False
        else:
            class_name = update_args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        
        if len(update_args) < 2:
            print("** instance id missing **")
            return False
        else:
            instance_id = update_args[1]

        key = class_name + "." + instance_id
        all_instances = models.storage.all()

        if key not in all_instances:
            print("** no instance found **")
            return False
        
        if len(update_args) < 3:
            print("** attribute name missing **")
            return False
        else:
            attribute_name = update_args[2]

        if len(update_args) < 4:
            print("** value missing **")
            return False
        else:
            attribute_value = update_args[3]

        instance = all_instances[key]

        attribute_type = type(getattr(instance, attribute_name))
        casted_value = attribute_type(attribute_value)

        setattr(instance, attribute_name, casted_value)

        models.storage.save()

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
