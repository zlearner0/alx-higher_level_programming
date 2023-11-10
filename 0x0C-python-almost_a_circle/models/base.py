#!/usr/bin/python3
'''this module contains class Base'''

import json
import csv


class Base:
    '''class gives a unique id for child classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initantiate id attribute'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''transfrom list to json string'''
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''put josn string list to a file'''
        if list_objs:
            li = [x.to_dictionary() for x in list_objs]
        else:
            li = []
        filename = '{}.json'.format(cls.__name__)
        jsonstring = cls.to_json_string(li)
        with open(filename, 'w') as wf:
            wf.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        '''from json string to list'''
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create an object with dictionary of arguments'''
        r1 = cls(5, 10)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'r') as rf:
            json_string = rf.read()
            li = cls.from_json_string(json_string)
        return list(map(lambda dictionary: cls.create(**dictionary), li))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''from object t csv file'''
        li = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for d in li:
                if cls.__name__ == 'Rectangle':
                    writer.writerow(
                        [d['id'], d['width'], d['height'], d['x'], d['y']])
                elif cls.__name__ == 'Square':
                    writer.writerow([d['id'], d['size'], d['x'], d['y']])

    @classmethod
    def load_from_file_csv(cls):
        '''read string list of dictionray to python object'''
        filename = '{}.csv'.format(cls.__name__)
        li = []
        with open(filename) as csvfile:
            if cls.__name__ == 'Rectangle':
                fieldnames = ["id", "width", "height", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["width"] = int(row["width"])
                    row["height"] = int(row["height"])
                    row["x"] = int(row["x"])
                    row["y"] = int(row["y"])
                    li.append(row)

            elif cls.__name__ == 'Square':
                fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["size"] = int(row["size"])
                    row["x"] = int(row["x"])
                    row["y"] = int(row["y"])
                    li.append(row)
        return list(map(lambda dictionary: cls.create(**dictionary), li))


@staticmethod
def draw(list_rectangles, list_squares):
    import turtle
    import time
    from random import randrange
    turtle.Screen().colormode(255)
    for i in list_rectangles + list_squares:
        t = turtle.Turtle()
        t.color((randrange(255), randrange(255), randrange(255)))
        t.pensize(1)
        t.penup()
        t.pendown()
        t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
        t.pensize(10)
        t.forward(i.width)
        t.left(90)
        t.forward(i.height)
        t.left(90)
        t.forward(i.width)
        t.left(90)
        t.forward(i.height)
        t.left(90)
        t.end_fill()

    time.sleep(5)
