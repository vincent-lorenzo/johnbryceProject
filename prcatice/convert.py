mylist = ["egg" , "milk" , "bread" ,"meat" ,"egg", "milk"]

print(mylist, type(mylist))

myset = set(mylist)

print(myset, type(myset))

mytuple= tuple(myset)

print (mytuple, type (mytuple))

if isinstance(mytuple , list) :
  print("mytuple is list")
else:
   print("mytuple is not list")

if isinstance(mytuple, tuple) :
  print("mytuple is tuple")
else: 
  print("mytuple is not tuple")