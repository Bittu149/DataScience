##Function
## Syntax
# def hello():
#     print("This is hello function")

# hello()

# def sum(a,b):##parameter pass kiya jata hai
#     print(f"The sum of your number is :- {a+b} ")
# sum(66,34)##yaha argument pass kiya jata hai

# def intro(name,age):
#     print(f"Your name is {name} and your age is  {age} ")
# intro(age=21,name="Bittu kumar singh")##Default argument

# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev +st [i]
#     if rev == st:
#         print("Pallindrome")
#     else:
#         print("Not a Pallindrome")

# pallindrome("NAMAN")
# pallindrome("CURSOR")

##Retun 
def hello():
    return "Hello how are you"
print(hello())