"""Dictionaries:
Dictionaries are used to store data values in key:value pairs
they are  unordered, mutable(changeble) & don't allow duplicate keys
"""

info = {
    "name": "venumadhav",
    "age": 20,
    "is_adult": True,
    "tuple" : ("dict", "list")
    }
print(info)
print(info["name"])#returns error if not exists
info["name"] = "VM"
print(info["name"])
null_dict = {}
print(null_dict)
#nested dict
nest = {
    "name" : "VM",
    "marks" : { "physic" : 40,
                "math" : 45,
                }
    }
print(nest)

#dictionary Methods
print(info.keys()) # returns a tuple with keys
print(info.values()) # returns a tuple with values
print(info.items()) # returns a tuple with keys and values
print(info.get("name")) #returns value or None if not exists

newdict = {}
print(info.update(newdict))

"""#Sets
Set:
set is the collection of the unordered items.
Each element in the set must be unique and immutable
we store can all types datatypes in set except list and dictionary
"""

set1 = {1,2,3,4,5,6}
set2 = {2,3,45,66,6,7,7}
print(set1)
print(len(set2))
set3 = set() #syntax for null set

# sets are immutable but set's elements are not mutable
set1.add(9)
print(set1)
set2.remove(45)
print(set2)
set1.clear()
print(set1)

#pops in randomly
print(set2.pop())
set1 = {1,2,3,4,5,6}

#union
print(set1.union(set2))
print(set1)
print(set2)

#intersection
print(set1.intersection(set2))
print(set1)
print(set2)
