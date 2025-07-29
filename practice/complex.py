config = {
    "host": "localhost", 
    "port" : 8080, 
    "ssl": True
}

print(config["host"]) 
config["port"] = 9090
print(config)

mylist = ["egg", "meat" , "milk", "bread" , "butter" , "banana"]
print(mylist[5])
print(mylist)
mylist.append("salt")
print(mylist) 

mylist.remove("butter")
print(mylist)
  
del mylist[1]
print(mylist)