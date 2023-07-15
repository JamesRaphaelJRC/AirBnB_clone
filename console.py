#!/usr/bin/python3
''' Defines a class HBHBCommand'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' Represents the class HBNBCommand.'''
    prompt = "(hbnb) "

    new_inst = None
    classes = ['BaseModel']
    attributes = ['name', 'my_number']

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

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id (save the change
            into the JSON file)
            usage: destroy <class name> <object id>
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
        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

    def do_all(self, line):
        ''' Prints all string representation of all instances based or not on
            the class name.
            Usage: all <class name> or all
        '''
        obj_dict = storage.all()
        args = line.split()

        if len(args) > 1 or args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            obj_list = []
            for obj in obj_dict.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        ''' Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file)
            Usage: update <classname> <obj_id> <attribute name>
                    <new attribute value>
            Only one attribute can be updated at a time.
        '''
        arg = line.split()
        obj_dict = storage.all()

        if not arg:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(arg[0], arg[1])
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        dicta = {}
        for key, value in obj_dict.items():
            if key == obj_key:
                dicta = value.__dict__
                dicta[arg[2]] = arg[3].replace('"', '')
        storage.save()

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
