## Dictionary me keys and values hota hai
## Dictionary are mutable
## Key unique hona chahiye


# d = {1:"hello", 2:"Bittu kumar singh",3:56}
# d[1]= 200 #Updating
# d[60]=800 #creating 
# d.update({50:500})
# d[1] = 100
# print(d)
# print(d[1])
# print(type(d))

## traverse over dictionary
# d = {1:"hello", 2:"Bittu kumar singh",3:56,4:400,5:500,6:600}
# for i in d.values():
#     print(i)

## deep copy 
# a = [1,2,3,4,5]
# b=a
# b[0]=100
# print(a)

## Shallow copy
# a = [1,2,3,4,5]
# b=a.copy()
# b[0]=100
# print(a)

## Count the frequency of each element 
a = [1,1,1,1,12,22,2,2,2,3,3,3,4,4,4,4,5,5,6,6,6,7,7,7,8,8,8,9,9]
#dict = {1:4,2:3,3:3,4:4,5:5,6:3,7:3,8:3,9:2}
d = {}
for i in a:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1
print(d)


