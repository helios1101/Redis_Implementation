from style import style
from db import dbMenu
from commands import mainMenu


if __name__ == "__main__":
    cont = 'yes'
    while (cont == 'yes'):
        style(" Redis Hands-on ")
        print("1. Setup Redis")
        print("2. Play with Redis Commands")
        print("3. More on Redis DB")
        print("--")
        print("4. Exit")
        print()
        ch = int(input("> "))
        print()

        if (ch == 1):
            pass
        elif (ch == 2):
            mainMenu()
        elif (ch== 3):
            dbMenu()
        elif ch==9:
            exit()


        print()
        cont = str(input("Run the entire program again? (yes/no) : "))
        print()