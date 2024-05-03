#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
        
    def set_name(self, name):
        if isinstance(name, str) and 25 >= len(name) >= 1:
            self._name = name
# insinstance allows me to check if an object is an instance of a specific class or type. In this case, I can use isinstance(name, str) to check if name is a string.
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed 
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(get_breed, set_breed)