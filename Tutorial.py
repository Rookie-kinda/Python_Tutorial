# First, Operators:
from PythonTutorial import PythonTutorial #To import slow print
from time import sleep # just sleep function
from Operators import operators # to import the operators tutorial
s_print = PythonTutorial.slow_print() # defining slow print
summation = operators().summation() # defining summation
multiplication = operators().multiplication() # defining multiplication
subtraction = operators().subtraction() # defining subtraction
division = operators().division() # defining division

def op(oper):
    if oper == "+":
        summation()
        s_print("Ok let's try multiplication now")
        sleep(3)
        multiplication()
        s_print("Ok let's try subtraction now")
        sleep(3)
        subtraction()
        s_print("Ok let's try division now")
        sleep(3)
        division()
    elif oper == "*":
        multiplication()
        s_print("Ok let's try summation now")
        sleep(3)
        summation()
        s_print("Ok let's try division now")
        sleep(3)
        division()
        s_print("Ok let's try subtration now")
        sleep(3)
        subtraction()
    elif oper == "-":
        subtraction()
        s_print("Ok let's try division now")
        sleep(3)
        division()
        s_print("Ok let's try summation now")
        sleep(3)
        summation()
        s_print("Ok let's try multiplication now")
        sleep(3)
        multiplication()
    elif oper == "/":
        division()
        s_print("Ok let's try subtraction now")
        sleep(3)
        subtraction()
        s_print("Ok let's try summation now")
        sleep(3)
        summation()
        s_print("Ok let's try multiplication now")
        sleep(3)
        multiplication()
    else:
        print("Please use either (+), (-), (*), (/)")
        op()
s_print("What do you want to start with?\n")
op(input())
        # string = string + "\n"
s_print("Hello, Welcome to your python tutorial, using python itself!",
    "This is supposed to help you understand the language, and maybe refresh your memory a little if you forgot stuff and you already are familiar with python\n", sep="\n")
sleep(0.5)
# journey = input("Are you ready?(y/n)\n")
s_print("Are you ready?(y/n)\n")
def start():
    journey = input().lower()
    if journey == "y":
        operators()
    elif journey == "n":
        s_print("Ok then, have a nice day :D")
    else:
        s_print("Please, respond with either y or n")
        start()
start()