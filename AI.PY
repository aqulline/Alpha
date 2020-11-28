import os
import sys
ever = True

def first_time():
    print("My name is ALPHA!")
    print("What's your name?")
    name = input("your name>> ")
    main = open("library.txt", "a")
    main.writelines(name+"\n")



def the_ai():
    listen = ""
    filen = open("library.txt", "r")
    name = filen.readline()
    print("hey",name)
    listen = input("listening_-_-_-")

   def remove(self, linen, filename):
        count = 1
        all_lines = []
        with open(filename, "r") as f:
            lines = f.readlines()
            number = lines.__len__()
            # number = number - 1
            for line in lines:
                all_lines.append(line)
        with open(filename, "w") as f:
            for i in range(number):
                if str(i) != linen:
                    f.write(all_lines[i])
                else:
                    termcolor.cprint("removed line" + " " + str(i) + " " + "''" + all_lines[i] + "''", "blue")

def find(self, removable, filenamee):
    filename = filenamee
    name = removable
    count = 0
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "r") as f:
        for line in lines:
            count = count + 1
            remove = line.strip().split(" ")
            lent = remove.__len__()
            lent = lent - 1
            for i in range(lent):
                if name == remove[i]:
                    termcolor.cprint("line" + " " + str(count - 1) + "''" + name + "''", "red")

while ever:
    file_name = "reference"
    filen = open("library.txt", "r")
    #print("me")
    x = filen.readline()
    if x == "":
        first_time()
    else:
        the_ai()