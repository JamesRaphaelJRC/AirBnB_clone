#!/usr/bin/python3
''' Defines a class HBHBCommand'''
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' Represents the class HBNBCommand.'''
    prompt = "(hbnb) "

    classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }
    new_inst = None

    def do_create(self, line):
        ''' Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.
            usage: create <obj class name>
        '''
        arg = line.split()
        if not arg:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if arg[0] == 'BaseModel':
            HBNBCommand.new_inst = BaseModel()
        elif arg[0] == 'User':
            HBNBCommand.new_inst = User()
        elif arg[0] == 'State':
            HBNBCommand.new_inst = State()
        elif arg[0] == 'City':
            HBNBCommand.new_inst = City()
        elif arg[0] == 'Place':
            HBNBCommand.new_inst = Place()
        elif arg[0] == 'Amenity':
            HBNBCommand.new_inst = Amenity()
        elif arg[0] == 'Review':
            HBNBCommand.new_inst = Review()

        print(HBNBCommand.new_inst.id)
        storage.save()

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
                return False
            elif args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return False
            else:
                print("** instance id missing **")
                return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return False
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
                return False
            elif args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return False
            else:
                print("** instance id missing **")
                return False
        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict:
            print("** no instance found **")
            return False

        del obj_dict[key]
        storage.save()

    def do_all(self, line):
        ''' Prints all string representation of all instances based or not on
            the class name.
            Usage: all <class name> or all
        '''
        obj_dict = storage.all()
        args = line.split()

        if args:
            if args[0] not in HBNBCommand.classes or len(args) > 1:
                print("** class doesn't exist **")
                return False
        obj_list = []
        for obj in obj_dict.values():
            if len(args) == 1 and args[0] == obj.__class__.__name__:
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
            return False
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        obj_key = "{}.{}".format(arg[0], arg[1])
        if obj_key not in obj_dict:
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False

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
