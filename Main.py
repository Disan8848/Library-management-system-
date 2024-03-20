import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("To Display       : Enter 1")
        print("To Borrow a book : Enter 2")
        print("To return a book : Enter 3")
        print("To exit          : Enter 4")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
