# list comprehension

list = [item for item in range(100) if item % 10==0]
print(list)

# dictionary comprehension

dict1 = { i:f"Item:{i}" for i in range(10)}   
print(dict1) 

# reverse a dictionary

dict2 = { value:key for value,key in dict1.items()}
print(dict2)

# set comprehension dictionary

set1 = {'dress1','dress2','dress1'}
print(set1)

# generator comprehension
gen =  (i  for i in range(10))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())