# class Factory:
#     a = 12 #attribute

#     def hello(self):#method
#         print("how are you")

#     print("Hello how are you i am getting initialized")

# # print(Factory().a)
# # Factory().hello()

# obj = Factory()
# obj.hello()

# class Factory:
#     def __init__(self,material,zips,pockets):# Self hamesa location ko target karta hai
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your object details are {self.material},{self.zips},{self.pockets} ")
        

# reebok = Factory("leather",3,2)
# print(reebok.pockets,reebok.zips,reebok.material)
# reebok.show()

## instance means object like self.name,self.age etc.

class animal:
    name = "lion" ## class attributes

    def __init__(self,age):
        self.age = age #instance attribute self loctatio  ko target krta hai

    def show(self):
        print(f"How are you, your age is {self.age} :- ") ## self target krta hai object ke location ko

    @classmethod
    def hello(cls):# cls class ke location ko target karega
        print("How are you brother")
    
    @staticmethod
    def static():
        print("How are you")

obj =  animal(12)
obj.show()
obj.hello()



