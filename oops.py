# class -> Abstract characteristics of object(s), its state(values,attributes..) and its behavior(capability).
# object -> instance of the class.
# instance -> actual object of a class created at run time.(object & instance used interchangeably)
# method -> defined capabilities of an object in a class.

class Pet: # defining class
    x='5 sense.'

    def animal(self): # a method within the class Pet
        self.x='All pets have '+self.x
        print(self.x)


pet=Pet() # creating instance for the class
pet.animal() # calling the method using the instance.
print(dir(Pet)) # dir() -> return the methods that can be performed and available within the class.