

from Guild import *



def exit():
    return 1

G = Guild()

MENU =[
       ["Add Character", G.input],
       ["Change Character", G.change],
       ["Delete Character", G.delete],
       ["Display Guildlist", G.output],
       ["Write Guildlist to the file", G.outputfile],
       ["Read Guildlist from the file", G.inputfile],
       ["Clear Guildlistlist", G.clear],
       ["Exit",exit]
       ]


def main():
    while True:
        i=0
        print("------------------------------")
        print("Select")
        for i, item in enumerate(MENU):
            print("{0:2}. {1}".format(i, item[0]))
        print("------------------------------")
        obtained_value = int(input())
        MENU[obtained_value][1]()
        if obtained_value == 7:
            break




if __name__ == "__main__":
    main()



