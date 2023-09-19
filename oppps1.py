# Parent class: Family Member
class FamilyMember:
    def talk(self):
        print("I can talk!")

    def laugh(self):
        print("I can laugh!")

    def walk(self):
        print("I can walk!")


# Child class: Dad
class Dad(FamilyMember):
    def fix_things(self):
        print("I can fix things using a toolbox.")
    def laugh(self):
        print("I can laugh loudly!")  # Override the laugh method from the parent class

# Child class: Mom
class Mom(FamilyMember):
    def cook(self):
        print("I can cook delicious meals without using a recipe book.")
    def dance(self):
        print("I can dance.")
    def talk(self):
        print("I can talk without stop")

# Child class: Kid
class Kid(Mom,FamilyMember):
    def play(self):
        print("I love to play games!")
    def walk(self):
        print("I can walk slowly")  # Override the laugh method from the parent class
    def cook(self):
        print("I can cook")
    def talk(self):
        print("I can talk but not long")

dad = Dad()
mom = Mom()
kid = Kid()


# dad.walk()
# dad.laugh()
# mom.laugh()
# mom.talk()
# kid.dance()
# Creating objects and using the abilities

# dad = Dad()
# mom = Mom()
# kid = Kid()

# try:
#     mom.fix_things()  # Try to call the walk method which is not defined in Mom class
# except AttributeError:
#     print("Mom doesn't know how to fix!")

#Inherited abilities
mom.talk()
dad.laugh()
kid.walk()

# # Unique abilities
# dad.fix_things() 
# mom.cook() 
# kid.play()


# kid.dance()
# kid.cook()
# kid.talk()
# # mom.fix_things()
# dad.walk()