from database import *

class Table:
    fields = []
    rows = []
    name = ""
    def __init__(self,*args):
        self.fields = args[0]
        self.rows = args[1]
        self.name = args[2]
    
    def print(self):
        print("In Print Statement")
        print(self.fields, self.rows, sep='\n\n')

    def select(self,**kwargs):
        print("\nIn select Statement")
        try:
            for key, value in kwargs.items():
                for row in self.rows:
                    for field, val in row.items():
                        if val == value and key == field:
                            print(row.items())
                            return
            raise KeyError
        except KeyError:
                print('{0} is not in table.'.format(kwargs))
        
    
    def insert(self,values,**kwargs):
        print("\nIn insert Statement")

        try:
            for key, value in kwargs.items():
                for row in self.rows:
                    for field, val in row.items():
                        if val == value and key == field:
                            row.update(values)
                            return
            raise KeyError
        except KeyError:
                print('{0} is not in table.'.format(kwargs))
