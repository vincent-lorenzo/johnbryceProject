name = "Vincent"
age = 31
height = 1.96
is_hungry = True
skills = ["Devops_developer" , "smart" , "fast_learner"]

profile = {
    "name" : name , 
    "age" : age , 
    "skills" : skills
}

print("name:",name )
print("age:" , age )
print("height:" , height)
print("skills:",  skills)
print("is_ hungry:", is_hungry)


print(age + 5)
print(len(skills))
print(skills[0])
print(name.upper())
print(name.lower())
skills.append("linux")
print(skills)

profile["wife:"] = "joanna"
print(profile)