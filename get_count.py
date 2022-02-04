# This Is task 2

class DBStorage:
    """ Just a class"""
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

