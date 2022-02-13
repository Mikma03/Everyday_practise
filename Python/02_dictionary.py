
#############################################################################
# dictionary
birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

print(type(birds))  # <class 'dict'>
print(type(prices))  # <class 'dict'>
print(type(empty_dict))  # <class 'dict'>


another_empty_dict = dict()  # using the dict constructor
print(type(another_empty_dict))  # <class 'dict'>


# note that the future dictionary keys are listed without quotes
prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')
print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}


# a nested dictionary example
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

# another nested dictionary example
# note that keys of the outer dictionary are numbers
digits = {1: {'Word': 'one', 'Roman': 'I'}, 
          2: {'Word': 'two', 'Roman': 'II'}, 
          3: {'Word': 'three', 'Roman': 'III'}, 
          4: {'Word': 'four', 'Roman': 'IV'}, 
          5: {'Word': 'five', 'Roman': 'V'}}



my_pet = {}
# add 3 keys and their values into the dictionary
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'


print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}
# get information from the dictionary about an added item
print(my_pet['name'])  # Dolly


# our nested dictionary once again:
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}
print(my_pets['cat']['breed'])  # maine coon


trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
print(trilogy['IV'])  # Star Wars
trilogy['IV'] = 'A New Hope'
print(trilogy['IV'])  # A New Hope


alphabet = {}
alphabet['alpha'] = 1
alphabet['beta'] = 2
print(alphabet)
# Python 3.8 output: {'alpha': 1, 'beta': 2}


# Example
children = {'Emily': {"profession": 'artist', "age": 5},
            'Adam': {"profession": 'astronaut', "age": 9},
            'Nancy': {"profession": 'programmer', "age": 14}}

