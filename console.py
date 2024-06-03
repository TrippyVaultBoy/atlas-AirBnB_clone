#!/usr/bin/python3
"""
Includes HBNBCommand class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb)"

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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
