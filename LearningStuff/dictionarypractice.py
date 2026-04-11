#my_list = ['terrier', 'cat', 'parrot']
#print(my_list)

#print('-' * 30)
my_dict = {'available': 'terrier', 'not available': 'cat', 'dead': 'parrot'}
#print(my_dict)
#Lists and dictionaries are mutable and ordered
#Lists are square brackets
#Dictionaries are curly brackets with key:value

#Call specific values
#for a list
#print(my_list[0])
#print(my_dict['available'])
#Call the key for dictionary

#ADDING MULTIPLE VALUES:
#First and simplest way to add multiple values is adding a list in place of a value when creating a dictionary
my_dict = {'available': ['terrier'], 'not available': 'cat', 'dead': 'parrot'}
print(my_dict)
#Now terrier is a list and the key available contains a value list with one value terrier
