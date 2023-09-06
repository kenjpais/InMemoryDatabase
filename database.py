from table import *

class Database:
    tables = []
    name = ""

    def __init__(self,name,*args):
        self.name = name
        self.tables = args
    
    def print(self):
        print("In Print Statement")
        print(self.name)
    def get_tables(self):
        for table in self.tables:
            print(table.name)

    