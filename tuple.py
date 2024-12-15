#Creating an empty tuple
tuple1 = ()
print(tuple1)

#creating tuples with integer elements
tuple2 = (1,2,3)
print(tuple2)

#creating with mixed datatypes
tuple3 = (101, "Anirban", 2002, "HR Dept")
print(tuple3)


#---------------------------------------------------------

#creation of nested tuples
tuple4 = ("points", [1,4,3], (7,8,6))
print(tuple4)

#tuple can be created without any parenthesis
#also called tuple packing
tuple5 = 101,"Hari",20002, "HR dept"
print(tuple5)

#tuple unpacking is also possible
empid,empname,empsal,empdept = tuple5
print(empid)
print(empname)
print(empdept)
print(empsal)

print(type(tuple5))
