# inheritance
class Animal:
    def legs(self):
        print("I have 4 legs")
    def fur(self):
        print("My body is covered with fur")
      
class Dog(Animal):
    def bark(self):
        print("The dog barks")
     
class horse(Dog):
    def neigh(self):
        print("The horse neighs")
        
class cow(Animal):
    def moow(self):
        print("The cow moows")
       
class cat(horse,cow):
    def purr(self):
        print("A cat purrs")

        
        
       
d=Dog()
d.bark()
d.legs()
d.fur()
h=horse()
h.neigh()
c=cow()
c.moow()
a=cat()
a.purr()
       
        