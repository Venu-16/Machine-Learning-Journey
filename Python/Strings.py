str1 = "This is str1"
str2 = 'This is str2'
str3 = """This is str3"""


print(str1,str2,str3)

#concatenation {adding two string using +}
str1 = "venu "
str2 = "madhav"
str3 = str1+str2
print(str3)

#length of str
c = len(str3)
print(c)
# whitespaces are also counted

#Indexing starts with 0
str ="Venu Madhav"
ch =str[0]
print(ch)
#Indexing starts with -1 from end to start
str ="Venu Madhav"
ch =str[-1]
print(ch)
#Slicing {Important for Machine learning}

#str[St_idx:End_Idx]
Str = "VenuMadhav"
print(str[2:8])

#Slicing using Negative Index

Str = "VenuMadhav"
print(str[-7:-3])

#String Functions
str = "I am a coder."
print(str.endswith("er.")) #returns true if string ends with substr
str.capitalize( ) #capitalizes 1st char
print(str)
b =str.replace( "c","$" ) #replaces all occurrences of old with new
print(b)

a=str.find("am") #returns 1st index of 1st occurrence
print(a)
c=str.count("am") #counts the occurrence of substr in string
print(c)