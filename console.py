#!/usr/bin/python3
''' Defines a class HBHBCommand'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' Represents the class HBNBCommand.'''
    prompt = "((hbnb) "

    new_inst = None
    classes = ['BaseModel']

    def do_create(self, line):
        ''' Creates a new instance of BaseModel, saves it (to the JSON file) and
            prints the id.
            usage: create <obj class name>
        '''
        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        HBNBCommand.new_inst = BaseModel()
        HBNBCommand.new_inst.save()
        print(HBNBCommand.new_inst.id)

    def do_show(self, line):
        ''' Prints the string representation of an instance based on the class
            name and id
            usage: show <class name> <class object id>
        '''
        obj_dict = storage.all()
        args = line.split()

        if len(args) < 2:
            if not args:
                print("** class name missing **")
                return
            elif args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''Exits the program cleanly'''
        return True
    def emptyline(self):
        '''Does nothing when n empty line + enter is issued'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
