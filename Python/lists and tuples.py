'''
List:
Built-in Data type
as same as Array
0-Indexed
-1 - Indexed
slicing also possible
we can store any type of data in single list
lists are mutable {we can change}
'''

nums = [1, 2, 3, 4, 5]
print(nums)
nums[0] = 8
print(nums)
print(nums[1:4])
#all String Slicing properties can be used

list = [1,2,3,4,5,6,7]
list.append(0)# add end of the list
print(list)
list.sort()
print(list)
print(list.sort())#returns None
print(list.append(0))#returns None
list.sort(reverse=True)
print(list)
# can sort Strings also based on alphabetic order
list = ["venu", "apple" , "mango"]
list.sort()
print(list)

list.reverse()
print(list)

#insert(idx,ele)
list.insert(2,5)
print(list)

#pop
list.pop(2) #removes element at index
print(list)
list.remove("mango")#removes 1st occur elements
print(list)

'''Tuple:
A built-in datatype that lets us create immutable sequence of values.
It is mutable - we can access but we can't modify this.
Slicing also possible.
'''
tuple = (1,2,3,3,4,5,)
print(type(tuple))

print(tuple.index(3))
print(tuple.count(3))