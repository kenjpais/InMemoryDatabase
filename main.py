from table import * 
from database import *

fields = [
    {
    "field": 'id',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    },
    {
    "field": 'name',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    },
    {
    "field": 'salary',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    }
]

rows = [
 {
    "id" : 2004,
    "name" : "Emily",
    "salary": 12123
  },
 {
    "id" : 2005,
    "name" : "Emily",
    "salary": 12123
  },
 {
    "id" : 200,
    "name" : "Emily",
    "salary": 1212
   }
]

location_fields = [
    {
    "field": 'id',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    },
    {
    "field": 'name',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    },
    {
    "field": 'cost',
    "datatype": 'integer',
    "size":'20',
    "loc":0,
    "val":''
    }
]

location_rows = [
 {
    "id" : 2004,
    "name" : "UK",
    "cost": 12123
  },
 {
    "id" : 2005,
    "name" : "Berlin",
    "cost": 12123
  },
 {
    "id" : 200,
    "name" : "India",
    "cost": 1212
   }
]

employees = Table(fields,rows, "employee")
locations = Table(location_fields,location_rows, "locations")
employees.print()
employees.select(id=200,name="UK")
employees.insert({"salary":200}, id=200)
employees.select(id=200,name="India")
locations.print()
locations.select(id=200,name="Berlin")
locations.insert({"cost":200}, id=200)
locations.select(id=200,name="India")
db = Database("ADMIN", employees, locations)
db.print()
db.get_tables()