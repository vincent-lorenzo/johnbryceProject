file = open("data", "r")
for line in file:
    print(line.strip())

print("*" *100)

with open("data", "r") as file2:
    for line in file2:
        print(line.strip())

with open("data", "r") as file2:
    print(file2.read())