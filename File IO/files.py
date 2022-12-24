my_file = open("C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/File IO/Test folder/test.txt")

print(my_file)
print(my_file.read()) # to read contents of the file(prints whatever is there in it)

# .seek() method to move cursor back to start and need to pass in number to indicate which line
my_file.seek(0)
print(my_file.read()) # will once again read all contents of the file

# .readline() method
print(my_file.readline()) # will only read the first line(would need to type this multiple times if there are multiple lines in the file)

# .readlines() method
print(my_file.readlines()) # will return an array containing every single line in the file

my_file.close() # good practice to include this

###################################################################################

# Read, write, append

# instead of manually closing file, can do this instead

with open("C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/File IO/Test folder/relative.txt", mode = 'r+') as new_file:
    new_file.write("Hi. How are you?")
    print(new_file.readline()) # ideal way to work with files

# open comes with 2nd parameter called mode and can be specified like this: mode = 'r' which is to read the file
# if mode not specified, default is read; to read and write, say mode = 'r+'
# append mode will append to end of file, but r+ will end up resetting cursor to start and replace certain portion of what existed previously
# w mode will completely overwrite everything in file

# can also create and write to a file that didn't exist previously
with open("C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/File IO/Test folder/test2.txt", mode = 'w') as new_file2:
    text = new_file2.write("# 2 testing")
    print(text)

# put code in try except block as a good practice just to make sure file is being read from/written to
# types: FileNotFoundError, IOError