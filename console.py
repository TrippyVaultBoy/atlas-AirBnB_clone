#!/usr/bin/python3
"""
Includes HBNBCommand class
"""
import cmd
from models.base_model import BaseModel


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
            print(new_instance.id)
            return

    def do_show(self, arg):
        pass

    def destroy(self, arg):
        pass

    def all(self, arg):
        pass

    def update(self, arg):
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
