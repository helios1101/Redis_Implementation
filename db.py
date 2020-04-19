from style import style
from info import infoDB
from test import testDB
from size import sizeDB


def dbMenu():
    again = 'yes'
    while (again=='yes'):
        style("Getting more of Redis DB")
        print("1. test connectivity")
        print("2. get current DB zise")
        print("3. get redis DB info")
        print("9. Exit")
        ch = int(input("> "))

        if ch==1:
            testDB()
        if ch==2:
            sizeDB()
        elif ch==3:
            infoDB()
        elif ch==9:
            exit()


        print()

        again = input("enquire more about redis DB? (yes/no) :")