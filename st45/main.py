#!/usr/bin/python3

from .Group import Group
G=Group()
    
def main():
    menu={'1':('ajout',G.Ajout),
          '2':('print',G.Print),
          '3':('write in file',G.WriteFile),
          '4':('read file',G.ReadFile),
          '5':('delete liste',G.Delete),
          '6':('Exit',exit)
        } 

    for key in menu.keys():
        print(key,'',menu[key][0])

    while True:
        choix=input('what u would do: ')
        if choix=='6':
            break

        try:
            menu.get(choix)[1]()
        except:
            print('Enter number between 1 and 6')
            
            
            


if __name__=='__main__':
    main()

