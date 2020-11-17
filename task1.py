#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class Vet:
    animal = None
    name = None
    breed = None
    owner = None
    birthdate = None

    
    def __init__(self):
        self.animal = input("Enter the animal")
        self.breed = input("Enter the breed of your pet")
        self.name = input("Enter the name of your pet")
        self.owner = input("Enter the owners name")
        self.birthdate = input("Enter your pet's birthdate, expressed as year-month-date")

    def displayPet(self):
        output1 = self.name+" "+self.animal
        output2 = self.breed+" is owned by "+self.owner
        print(output1)
        print(output2)
        
    
pets=[]
x=1
while x != 2:
    print("1=Enter a pet")
    print("2=Retrieve Pet")
    print("3=Exit")
    z = int(input(""))
    if z == 1:
        pets.append(Vet())
        x=1
    elif z == 2:
        y = input("Which pet")
        for i in pets:
            if i.name == y:
                print(i.displayPet())
            
        x = 1
    elif z == 3:
        print("Thank you for visiting")
        x = 2