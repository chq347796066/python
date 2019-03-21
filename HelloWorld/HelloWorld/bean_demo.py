from json import JSONEncoder


class Student(JSONEncoder):
    def __init__(self,name,age):
        self.name=name;
        self.age=age;


