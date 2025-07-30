name = input("Enter Your Name:") 
greet = input(f"hello {name}! , how are you?: ")

if greet == "ok":
    print("Glad to hear it!")
    glad = input("it is a beautiful day today isn't it?: ")
    if glad == "yup":
        print("you have a good one")
    elif glad != "yup":
        print("see you later!")
elif greet == "not ok":
    print("sorry to hear that")
    sad =input("anything i can do to help?: ")
    if sad == "no":
        print("well let me know if you need anything")
    elif sad == "yes":
        print("tell me what's wrong")
else: 
    print("Invalid Response")