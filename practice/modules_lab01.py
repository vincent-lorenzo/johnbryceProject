import math

print(math.sqrt(10))

print(dir(math))

help(math.sqrt)

def get_root(number):
   return math.sqrt(number)

print(get_root(34))

def add_numbers(b, a):
  sum = a + b 
  return  get_root(sum)
  
print(add_numbers(10 , 30))
