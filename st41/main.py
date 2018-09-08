from .group import Group

g = Group()

def editMember():
    i = int(input("Index: "))
    g.edit(i - 1)
       
def deleteMember():
    i = int(input("Index: "))
    g.remove(i - 1)

methods = [g.addPerson, g.addStudent, editMember, deleteMember, g.print, g.saveToFile, g.loadFromFile]

def printMenu():
    print("1 - Add person")
    print("2 - Add student")
    print("3 - Edit member")
    print("4 - Remove member")
    print("5 - Print group")
    print("6 - Save to file")
    print("7 - Load from file")
    print("8 - Exit")

def main():  
    while True:
        printMenu()
        try:
            i = int(input("Num: "))
            if i == 8:
                break
            if i >= 1 and i <= 7:
                methods[i - 1]()
            else:
                print("Incorrect input")
        except ValueError:
            print("Incorrect input")
        except IndexError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    
if __name__ == '__main__':
	main()