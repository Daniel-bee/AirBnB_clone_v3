#!/usr/bin/python3
from models.engine.file_storage import FileStorage

class get(FileStorage):
    """ Just a class"""
    def __init__(self):
        """ Inherits from the filestorage"""
        super().__init__()

    def get(self, cls, id):
        """ This one returns info about the class whose id is 'id' """
        if cls in DBStorage.classes and id == cls.id:
            """ If the class' name and id match """
            return cls.all()
        return None

    def count(self, cls=None):
        """ count the number of obects in cls """
        if cls == None:
            return len(self.all())
        return cls.all()

