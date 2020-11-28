import termcolor
import os
from PIL import Image


class texteditor:
    def menu(self):
        termcolor.cprint("in a text editor", 'cyan')
        termcolor.cprint('options', 'yellow')
        termcolor.cprint("o: open a file and edit it", "magenta")
        termcolor.cprint("d: file description", "magenta")
        termcolor.cprint("r: open a file and read it", "magenta")
        termcolor.cprint("e: exit editor", "magenta")
        termcolor.cprint("v: view files in main file", "magenta")
        opt = input("your option😃" + ">>" + " ")
        self.option(self, opt)

    count1 = 1

    def file(self, filename):
        file1 = open(filename, "a")
        file1.o = open(filename, "r")
        print("file", file1.name)
        input1 = " "
        count = 1
        countl = 1
        inputw = []
        for line in file1.o:
            print(self.count1, ">>", line)
            self.count1 = self.count1 + 1
        while input1 != "^s":
            if input1 != "^s":
                input1 = input(str(self.count1) + " " + ">>" + " ")
                self.count1 = self.count1 + 1
                if input1 == "\n":
                    inputw.append(input1)
                elif input1 == "^s":
                    break
                else:
                    inputw.append(input1)
            else:
                break
        if input1 == "^s":
            with open(filename, "a") as f:
                for word in inputw:
                    f.write(word + "\n")
        self.menu(self)

    def filedescription(self, filename):
        file1 = open(filename, "r")
        countw = 0
        countl = 0
        word = " "
        for line in file1:
            countl = countl + 1
            word = line.strip().split(" ")
            countw = countw + word.__len__()

        termcolor.cprint("lines" + " " + str(countl), "yellow")
        termcolor.cprint("words" + " " + str(countw), "blue")
        self.menu(self)

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
    def imad(self,filename):
        img = Image.open(filename)
        img.show()
    def fileread(self, filename):
        real = " "
        dec = " "
        while real != "e":
            file1 = open(filename, "r")
            count = 0
            for lines in file1:
                print("line", str(count), ":", lines)
                count = count + 1
            print("f:find a word", "e:exit read mode", "re: delete a line")
            dec = input()
            real = dec
            if dec == "f":
                word = input("enter word")
                self.find(self, word, filename)
            elif dec == "re":
                word = input("line number. exp=1 ")
                self.remove(self, word, filename)
            else:
                break
        self.menu(self)

    def viewfiles(self):
        filep = "C:\\Users\\WARIDI\\Desktop\\ALPHA"
        filenames = os.listdir(filep)
        for files in filenames:
            print(files)

    def option(self, opt):
        if opt == "o":
            print("enter file name")
            filename = input()
            self.file(self, filename)
        elif opt == "d":
            print("enter file name")
            filename = input()
            self.filedescription(self, filename)
        elif opt == "v":
            self.viewfiles(self)
        elif opt == "e":
            exit()
        else:
            print("enter file name")
            filename = input()
            self.fileread(self, filename)

    ready = True

    def editor(self):
        while self.ready:
            self.menu(self)


texteditor.editor(texteditor)
