##Set datastructure
##Mutable hota hai
## Sets are unordered and you cannot access them through index value
## s = {} ye dictionary hota hai

s = {1,2,3,4,5}

b = hash("hello")
print(b)

## Sets method 
s = {1,2,34,5}
s.add(77) ## Add an element to the set
s.remove(77) ## Remove 77 (Raises an error if not found )
s.discard(4) ## remove 4 (No error if not found)
popped_element = s.pop() ## Remove a random element 
s.clear() ## Removes all element 
