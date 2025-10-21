## Errors occur due to mistakes in the code that prevent it from running.these can syntax errors or logical errors
## Syntax error
# Indentation error 
# tab error 
#print("Hello world"

# a = int(input("Enter your number :- "))

# try:
#    print(10/a)

# except Exception  as err:
#    print(f"sorry  there is an err as {err}")

# else:
#    print("Good there is no exception")

# finally:
#    print("i will run no matter what")

# print("ok i have done the division")



age = int(input("Enter your age :- "))

try:
    if age < 10 or age >18:
        raise ValueError("Your age must be between 10 and 18 ")
    else:
        print("Welcome to the club")

except Exception as err:
    print( f"An error occured as {err}")


print("The club start soon")
