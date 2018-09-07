import pickle,os


from Character import *
from Stat import *


class Guild:


    def __init__(self):
        self.l = list()


    def input(self):
        receivedvalue = input("For Character press 1, for Stat press 2\n")
        if (receivedvalue == '1'):
            self.l.append(Character())
        elif (receivedvalue == '2'):
            self.l.append(Stat())
        else:
            print("Wrong number")
            return 0
        self.l[len(self.l)-1].input()
        return 1
            
            
    def output(self):
        i = 1
        for obj in self.l:
            print("Character number:",i)
            obj.output()
            i += 1
        if(len(self.l) == 0):
            print("NO Objects")


    def change(self):
        self.output()
        if(len(self.l) != 0):
            try:
                charnumber = int(input("Choose Character(by number):"))
                if(charnumber > 0) and (charnumber <= len(self.l)):
                    if(self.input() == 1):
                        self.l[charnumber-1] = self.l[len(self.l)-1]
                        self.l.pop()
                        print("Changed")
                else:
                    print("Wrong value")

            except:
                print("Wrong value")


    def delete(self):
        self.output()
        if (len(self.l)!=0):
            print("Choose Character")
            charnumber = int(input())
            if (charnumber>0) and (charnumber<=len(self.l)):
                self.l.pop(charnumber-1)
                print("Deleted")
            else:
                print("Wrong value")


    def inputfile(self):
        if (os.path.exists("file.txt")):
            self.l = pickle.load(open("file.txt", "rb"))
            print("File successfully read")
        else:
            print("File not found!")


    def outputfile(self):
        pickle.dump(self.l, open("file.txt", "wb"))
        print("File successfully recorded")


    def clear(self):
        self.l.clear()










