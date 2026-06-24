file = open("my_text.txt")
contents = file.read()
print(contents)
file.close()

with open("my_text.txt") as file:
    contents = file.read()
    print(contents) #no need to write file.close()

with open("my_text.txt", "w") as file:
    file.write("New text")

with open("my_text.txt", "a") as file:
    file.write("\nHi, Please read me!\n")

with open("new_file.txt", "w") as file:
    file.write("Hello, This is a new file.")

    





