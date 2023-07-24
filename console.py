#!/usr/bin/python3
"""Defines the console"""
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(line):
    ''' parses the line (string) from prompt  before execution'''
    argv = line.split(' ')
    if len(argv) > 4:
        argv = argv[:4]
    if len(argv) != 4:
        return argv

    # parses update command (remove quotes)
    print(argv)
    if argv[3][0] in ['"', '"']:
        argv[3] = argv[3][1:]
    if argv[3][-1] in ['"', '"']:
        argv[3] = argv[3][:-1]
    if argv[2][0] in ['"', "'"]:
        argv[2] = argv[2][1:]
    if argv[2][-1] in ['"', "'"]:
        argv[2] = argv[2][:-1]

    return argv


def err_manager(line, argc):
    ''' manages errors while parsing '''
    if not line:
        print("** class name missing **")
        return -1
    argv = parse(line)
    if argv[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return -1

    if argc == 1:
        return argv

    if len(argv) < 2:
        print("** instance id missing **")
        return -1

    cls_name, id = argv[0], argv[1]
    keys = storage.all().keys()

    if f'{cls_name}.{id}' not in keys:
        print("** no instance found **")
        return -1

    if len(argv) == 2 and argc == 4:
        print("** attribute name missing **")
        return -1

    if len(argv) == 3 and argc == 4:
        print("** value missing **")
        return -1
    return argv


def type_checker(value):
    '''
        typecasts value into adequate type before
        updating instance attributes
    '''
    if value.isdigit():
        return int(value)
    try:
        float(value)
        return float(value)
    except ValueError:
        return value


class HBNBCommand(cmd.Cmd):
    ''' Defines the HBNBCommand interpreter '''

    prompt = '(hbnb) '

    classes = {
        'BaseModel', 'User', 'Place',
        'State', 'City', 'Amenity', 'Review'
    }

    def do_quit(self, line):
        '''
        Description:
        - quits command interpreter when quit is inputed
        -> Usage: quit
        '''
        return True

    def do_EOF(self, line):
        '''
        Description:
        - quits command interpreter on
            EOF marker (if no text in cmd line)
        - performs forward delete if in between two
            characters or line beginning
        -> Usage: Ctrl + D
        '''
        return True

    def emptyline(self):
        ''' Do nothing upon receiving an empty line.
            or an empty line + space
        '''
        pass

    def do_create(self, cls):
        '''
        Usage: create
        - creates a new instance of class
        - saves it in the JSON file
        - prints the id
        - Usage: create <class name>
        '''
        if err_manager(cls, 1) == -1:
            return
        obj = eval(cls)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        ''' implements the show command '''
        argv = err_manager(line, 2)
        if argv == -1:
            return

        cls_name, id = argv[0], argv[1]
        objects = storage.all().values()
        for obj in objects:
            print(obj) if obj.id == id else ""

    def do_destroy(self, line):
        ''' implements the destroy command '''
        argv = err_manager(line, 3)
        if argv == -1:
            return

        cls_name, id = argv[0], argv[1]
        del storage.all()[f'{cls_name}.{id}']
        storage.save()

    def do_all(self, cls_name):
        ''' implements the create command '''
        objects = storage.all().values()
        if not cls_name:
            # this is for, <all> without class name
            [print(obj) for obj in objects]
            return
        argv = err_manager(cls_name, 1)
        if argv == -1:
            return
        for obj in objects:
            print(obj) if obj.__class__.__name__ == cls_name else ""

    def do_update(self, line):
        '''
        Description:
            Updates the instance attributes either through a key value pair
            or a dictionary representation

        Usage:
            - update <class name> <id> <attr name> <attr value>
            - <class name>.update(<id>, <attribute name>, <attribute value>)
            - <class name>.update(<id>, <dictionary representation>)
        '''
        attributes = re.search(r"\{(.*?)\}", line)
        if not attributes:
            argv = err_manager(line, 4)
            if argv == -1:
                return
            cls_name, id, attr, value = argv[0], argv[1], argv[2], argv[3]
            obj = storage.all()[f'{cls_name}.{id}']

            value = type_checker(str(value))
            obj.__dict__[attr] = value
            storage.save()
            return

        args = line.split(' ', 2)
        cls_name, id, attr_dict = args[0], args[1], args[2]
        attr_dict = json.loads(attr_dict)
        for key, value in attr_dict.items():
            test_line = ' '.join([cls_name, id, key, str(value)])
            argv = err_manager(test_line, 4)
            if argv == -1:
                return
            cls_name, id, attr, value = argv[0], argv[1], argv[2], argv[3]
            obj = storage.all()[f'{cls_name}.{id}']
            value = type_checker(str(value))
            obj.__dict__[attr] = value
            storage.save()

    def default(self, line):
        ''' implements the default commands  '''
        objects = storage.all().values()
        argv = line.split('.', 1)

        if len(argv) != 2 or argv[0] not in HBNBCommand.classes:
            print('*** unknown syntax:', line)
            return

        if argv[0] in HBNBCommand.classes and argv[1].endswith('()'):
            command = argv[1][:-2]

            if command not in ['all', 'count']:
                print('*** unknown syntax:', line)
                return

            if command == 'all':
                attrs = \
                    [obj for obj in objects if type(obj).__name__ == argv[0]]
                [print(att, end=', ' if att != attrs[-1] else '\n')
                    for att in attrs]
                return

            if command == 'count':
                count = 0
                for obj in objects:
                    if type(obj).__name__ == argv[0]:
                        count += 1
                print(count)
                return

        cls_name = argv[0]
        param = re.search(r"\((.*?)\)", argv[1])
        attributes = re.search(r"\{(.*?)\}", param[1])

        if param:
            method = argv[1][:param.span()[0]]
            param_list = param[1].split(', ', 2)
            id = param_list[0][1:-1]
            if len(param_list) == 1:
                line = ' '.join([cls_name, id])
                eval('self.do_' + method)(line)
            elif not attributes:
                param_list = ' '.join(param_list)
                line = ' '.join([cls_name, param_list])
                eval('self.do_' + method)(line)
            else:
                param_list = param[1].split(', ', 1)
                attr_dict = param_list[1].replace("'", '"')
                line = ' '.join([cls_name, id, attr_dict])
                eval('self.do_' + method)(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
