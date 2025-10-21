#File Handling
# Any name with an extension is file 
# Now that extension can be .py,.txt,.mp3 ect and when we want to handle these files we will use file handling

p =  open("Sperman.txt",'w')
p.write("Hello this Bittu and i am writing inside this file")
p.close()
# 'r' Read(default)-fie must exist
# 'w' Write- create file or overwrites
# 'a' Append - adds to end of file.
# 'x' Create - creat a new file,fails if it exist
