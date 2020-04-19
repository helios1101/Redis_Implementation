#!/usr/bin/python3
from get import Rget
from set import Rset
from setex import Rsetex
from zadd import Rzadd
from zrange import Rzrange
from zrank import Rzrank
from flush import Rflush

from style import style



def mainMenu():
    again = 'yes'
    while (again == 'yes'):
        style("Choose commands : ")
        print("1. redis get")
        print("2. redis set")
        print("3. redis setex")
        print("4. redis zadd")
        print("5. redis zrange")
        print("6. redis zrank")
        print("7. Redis flush")
        print("--")
        print("8. Back")
        print("9. Exit")
        print()
    
        ch2 = int(input("> "))
        print()

        if ch2==1:
            Rget()
        elif ch2==2:
            Rset()
        elif ch2==3:
            Rsetex()
        elif ch2==4:
            Rzadd()
        elif ch2==5:
            Rzrange()
        elif ch2==6:
            Rzrank()
        elif ch2==7:
            Rflush()
        elif ch2==8:
            break
        elif ch2==9:
            exit()


        print()
        again = input("wanna play again? (yes/no) : ")
        print()