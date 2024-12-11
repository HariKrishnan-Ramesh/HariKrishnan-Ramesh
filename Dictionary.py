details = {
    'Hari':1234,
    'Ammu':5464,
    'Hena':8373,
    'Ramesh':1111,
}

# for i in details:
#     print(i)

for i in details.items():
    print(i)



print(details)
# details['Hena']={'Hena_No':982829929,'Hena_Adress':'Silver Lane'}
details['Unknown']=97829
details['Unknown1']=978623 #We can add new items to dictionary like this
print(details.keys()) #To get the all keys of a dictionary
print(details.values()) #To get the all values of a dictionary

#To Copy a dictionary
details2=details.copy()
print(details2)

#To get a particular value of a key
print(details.get('Ammu'))


data = {
    1:'Ram',
    2:'Ramesh',
    0:'karan',
}
print(data[0])
# del data
print(data)
# data.pop(1)
print(data)
# data.popitem()
print(data)
data.clear()
print(data)