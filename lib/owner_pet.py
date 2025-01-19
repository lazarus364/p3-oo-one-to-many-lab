# lib/owner.py  

class Owner:  
    def __init__(self, name):  
        self.name = name  
        self.pets_list = []  

    def pets(self):  
        """Returns the list of the owner's pets."""  
        return self.pets_list  

    def add_pet(self, pet):  
        """Adds a pet to the owner's pets if it is an instance of Pet."""  
        if not isinstance(pet, Pet):  
            raise Exception("Only pets of type Pet can be added.")  
        pet.owner = self  
        self.pets_list.append(pet)  

    def get_sorted_pets(self):  
        """Returns a sorted list of pets by their names."""  
        return sorted(self.pets_list, key=lambda pet: pet.name)
# lib/pet.py  

class Pet:  
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]  
    all = []  

    def __init__(self, name, pet_type, owner=None):  
        self.name = name  
        self.pet_type = pet_type  
        
        if pet_type not in Pet.PET_TYPES:  
            raise Exception(f"{pet_type} is not a valid pet type. Valid types are: {Pet.PET_TYPES}")  

        if owner is not None:  
            if not isinstance(owner, Owner):  
                raise Exception("Owner must be of type Owner.")  
            self.owner = owner  
            owner.add_pet(self)  

        Pet.all.append(self)  