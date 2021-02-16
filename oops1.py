# Constructor and Destructor
class Pet: # defining class
    x='5 sense.'

    def __init__(self): # CONSTRUCTOR -> while creating instance for the class, this will get constructed and called.
        print('I am constructor')

    def animal(self): # a method within the class Pet
        self.x='All pets have '+self.x
        print(self.x)

    def __del__(self): # DESTRUCTOR -> when the instance created,stopped being instance this will be called(seldom used in programs)
        print('I am destructor')


pet=Pet() # creating instance for the class.
pet.animal() # calling the method using the instance.
pet='Done' # all objects will be destructed.
print(f'I am {pet}')