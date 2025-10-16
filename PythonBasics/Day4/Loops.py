##inpython there are two type of loops
## For loop or while loop


#For loop range me (start,end,step) rahta hai
#a = range(1,20,2) default pe step 1 hi rahta hai

# for i in range(20):
#     print(i)

# for i in range(16,1,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

# n = int(input("Which table you want ? "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])

# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)

# Break statement
# for i in range(1,21):
#     if i ==15:
#         break
#     else:
#         print(i)


# Continue statement means skip kr dena 
# for i in range(1,21):
#     if i ==15:
#         continue
#     else:
#         print(i)


# for i in range(1,21):
#     if i == 15:
#         print("Break statement is executed after 14")
#         break
#     print(i)
# else:
#     print("Break statement is not executed")

# n = int(input("Enter your number"))
# for i in range(n):
#     print("Hello")

# n = int(input("Enter your number"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# sum = 0;
# n = int(input("Enter your number"))
# for i in range(1,n+1,):
#     sum = sum + i
#     print(f"Your sum is {sum}")

## Factorial of n number

# n = int(input("Enter your number:-"))
# Fact = 1;
# for i in range(1,n+1,):
#     Fact = Fact * i
#     print(f"Your factorial is {Fact}")

##Even or odd sum
# n = int(input("Enter your number:-"))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"Your even and odd sum are {even} , {odd}")

# n = int(input("Enter your number :- "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n = int(input("Check your number is perfect or not :- "))
# sum = 0
# for i in range(1,n):
#     if n % i==0:
#         sum = sum + i

# if sum == n:
#     print("Your number is perfect")
# else:
#     print("Your number is not perfect")


# n = int(input("Check wether the number is prime or not :- "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count = count + 1
# if count == 2:
#     print("Your number is prime")
# else:
#     print("Your number is not prime")

# print(f"Count factor is  {count}")

##Reverse an string 
# a = "SHERIYIANS"
# print(a[::-1])

# a = "SHERIYIANS"
# for i in range(len(a)-1,-1,-1):
#     print(i)
##print(a[i])

##Check string palindrome or not 
# a = input("Enter your string :- ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#    b = b + a[i]

# if b ==a:
#    print("Your string is plindrome")
# else:
#    print("Your string is not palindrome")

# a = "daujhjiuneiwubhewb#@$!@%^%&@^@*8"
# char = 0
# dig =0
# spchar= 0
# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchar+=1

# print(f"your digits are {dig}\n your alphabets are {char}\n your special characters are {spchar} ")

#print(dir(str))

