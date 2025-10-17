## In pyhton there are 4 types of in-built data-structure List,Tuple,Dictionary,set.
##Custom data structure stack,queue,linked list, graph,etc


#List data structure
#Syntax
# a = [1,2,2,4,5,True,print(),"bittu"]
# print(a[-1])

# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values
# for i in a:
#     print(i)


#list methods
#print(dir(list))
# a= [1,2,3,4,5,-49,-55,-33,-66] 
# for i in a:
#     if i>=0:
#         print(f"The positive element is :- {i}")
#     elif i<0:
#         print(f"All negative element is :- {i}")    

## mean value of list

# l = [1,2,3,4,5,6,7,8,10]
# sum = 0
# for i in l:
#     sum  = sum + i
# print(sum/len(l))

## find the greatest element 

# b = [12,14,66,48,65,99,200,100]
# largest = b[0]
# index = 0
# for i in range(len(b)):
#     if b[i]>largest:
#         largest = b[i]
#         index = i
# print(f"Your largest number is :- {largest} at index :- {index} ")


##Check if list is sorted or not 

b = [12,14,66,48,65,99,200,100]
for i in range(len(b)):
    if b[i]<b[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("your list is sorted")