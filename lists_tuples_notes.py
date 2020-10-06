#List & Tuples
#Membership Testing

fruits_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables_tuple = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits # False
'eggplant' not in fruits # True

'eggplant' in vegetables # True
'eggplant' not in vegetables # False

#Index

my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list

#Count

my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat') # 2
my_pets.count('lizard') # 0

#Range
#Membership Testing
nums = range(10)

0 in nums # True
10 in nums # False
4 in nums # True

0 not in nums # False
15 not in nums # True
10 not in nums # True

nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True

#Index
nums = range(1, 10, 2)

nums.index(5) # 2
nums.index(10) # ValueError: 10 is not in list
nums.index(1) # 0


