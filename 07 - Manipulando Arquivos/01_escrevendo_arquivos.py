file = open("C:\Workspace\Python\.txt\hello_world.txt", "w")
file.write("Hello World!")
file.close()

file = open("C:\Workspace\Python\.txt\hello_world.txt", "r")
print(file.read())
file.close()