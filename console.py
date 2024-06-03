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
        'BaseModel': BaseModel
    }

    def emptyline(self):
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
        show_args = args.split(' ')
        print(show_args)

        if len(show_args) == 0:
            print("** class name missing **")

        if show_args[0] in HBNBCommand.classes:
            if show_args[1]:
                class_name = show_args[0]
                instance_id = show_args[1]
                key = class_name + "." + instance_id
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **") 

    def do_destroy(self, args):
        destroy_args = args.split(' ')
        print(destroy_args)

        if len(destroy_args) == 0:
            print("** class name missing **")

        if destroy_args[0] in HBNBCommand.classes:
            if destroy_args[1]:
                class_name = destroy_args[0]
                instance_id = destroy_args[1]
                key = class_name + "." + instance_id
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
        

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
