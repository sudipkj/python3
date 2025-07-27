list = [40,30,'Aa']
print(list)

list.append(3)
print(list)

# List.append doesn't return the list itself, it returns None
# list = list.append(4)
# print(list)

list.pop(-2)
print(list)

list.pop()
print(list)

list.insert(1, 100)
print(list)

list2 = [1, 2, 3]
list += list2
print(list)
list.append(list2)
print(list)

list.extend('Python')
print(list)


for  idx , element in enumerate(list):
    if(element == 't'):
        list.pop(idx)
print(list)

list.remove('P')
print(list)

list.insert(2,'Hello')
print(list)

list.insert(2,['Hello'])
print(list)

# Dictionaries

person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

person['hobbies'] = ['reading', 'traveling']
print(person)
print(person.items())
print(person.keys())
print(person.values())

cities = ["New York", "Los Angeles", "Chicago"]
areas = [8.4, 3.9, 2.7]  # in millions

city_areas = dict(zip(cities, areas))
print(city_areas)

print(tuple(zip(cities, areas)))
print('------------------------------------------------')
dict = {}
dict['Key1'] = 'value1'
dict['Key2'] = 'value2'
dict['Key3'] = 'value3'
print(dict)



print ('---------------------Set---------------------')

x= [90, 80, 70, 60, 50, 40 , 90, 80, 50, 40, 30, 20, 10]
print(x)
print(set(x))

s = {1, 2, 3, 4, 5}

print(s.remove(2))
print(s)
s.pop()


print('---------------------Frozen Set---------------------')
f = frozenset()
print(f)
f = {10, 20, 30, 40, 50, 10}
print(f)














