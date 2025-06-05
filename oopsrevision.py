#This is a class
class Animal: 
    def __init__(self,name,action):   #This is a constructor basically the input it will take ie the attributes
        self.name= name #Attributes of the Animal
        self.action=action 
        self.__health = 100 ##ENCAPSULATION
    def get_health(self):
        return self.__health
       
    def sound(self): #These are the method that will define the actions it will perform
        print(f"The {self.name} performs {self.action}") #so abstraction since it hides the process and gives final op only
    def __str__(self): # show what to print when we print the object 
        return self.name
    
class Snake(Animal): ##This is a example of inheritance
    def sound(self):
        print(f"The {self.name} performs Hiss")
    
        
dog=Animal("Dog","Barks")##This is a object being created

Cat=Animal("Cat","Meows")
Cat.sound()
print(Cat)
print(dog)
Cobra=Snake("Cobra","Hss")
Cobra.sound()

for things in [dog,Cobra]: ##CAN ALSO WRITTEN AS [Animal("Cat","Meows"),Animal("Dog","Barks")]
    #eg of polymorphism..same name method in different classes ie SOUND
    things.sound()
    
print(dog.get_health())
#only be accessed using .get_health(),if use .__health not visible