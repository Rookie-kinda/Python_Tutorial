# This tutorial will help you understand the very basics of python, not too deep, just understand the language
from PythonTutorial import PythonTutorial
from time import sleep

s_print = PythonTutorial().slow_print
class operators:
    s_print("Cool!", "Let's start with something simple, operators!",
    "operators are used to preform various operations, and not only mathematical operations, there are other stuff as well",
    "let's start with the most basic and simple operators, which are Summation(+), Subtraction(-), Multiplication(*),and Division(/)\n" ,sep="\n")
    
    
    def summation():
        s_print("Summation is one of the basic operators, and as you probably know from very basic kindergarten math, that it adds stuff to each other, but here's the catch", 
                "In python and most programming languages, summation (or plus) along side some other operators are not only used for numbers, they are used for all types of stuff",
                "First, input two numbers (space seperated but on the same line)", sep="\n")
        a, b = map(int, input().split())
        s_print(f"{a}+{b} = {a+b}", f"Pretty simple, just {a}+{b}", sep="\n")
        s_print("Now, enter two words (they can contain numbers as well, but they have to be space seperated on the same line)")
        word1, word2= input().split()
        s_print(f"{word1+word2}", 
                "What you just enter is called a string, and it is just plain text, python deals with it as such, even if it contains numbers, it just concatenates them together if you add them"
                , sep="\n")
        sleep(3)
        s_print("Now, before we go any deeper into this, you need to know and understand what is going on exactly", 
                f"Now, when we did {a} + {b}, it gave us {a+b}, which is litrally how it is written, just {a}+{b} and voila, you get the answer",
                "And actually, the very same thing when you entered a string(more on data types later)",
                f'We just did "{word1} + {word2}", and it gave us "{word1+word2}", but, if you do not want them to be stuck to each other like that you can add a space (" ") between the two words as such)',
                f'"{word1}" + " " + "{word2}", and this yields "{word1+" "+word2}", we will talk more on formatting in a different tutorial', sep="\n")
        sleep(4)
        s_print("We can do the same thing with containers like lists (more on containers later)", 
                "Lists practically do the same thing with each other when we add a (+) between them, they concatenate, this words means that we add the latter at the end of the earlier one",
                "I'll enter the list this time though", sep="\n")
        s_print("[1, 2, 3] + [4, 5, 6]", 
                f"this gives: {[1, 2, 3] + [4, 5, 6]}",
                "which i think is pretty neat", sep="\n")
        sleep(2)
        s_print("Here's the thing though, you can't add differen data types to each other ,you can only add same data types(again, more on them later), let's try it out, enter a string and an integer")
        word, num = input().split()
        try:
            s_print(f"{int(num) + word}")
        except TypeError:
            s_print(" 'unsupported operand type(s) for +: 'str' and 'int''")
        sleep(3)
        s_print("So, you see, this doesn't work, it gives an error, and this specifc error means that you can't do this operation on those two types together\n")
        
    def subtraction():
        s_print("Subtraction is one of the basic operators, you probably know this, but this operator takes one thing from the other",
                "This one only works with numbers though, You can't subtract strings from each other, nor can you subtract containers from each other, nor numbers from strings/containers, nor strings from containers and vise versa, you get the idea",
                "Go ahead an enter two numbers(space seperated but on the same line)", sep="\n")
        number1, number2 = map(int, input().split())
        s_print(f"{number1} - {number2} = {number1-number2}")
        sleep(3)
        s_print("Ok, now try to enter two words and see what happens")
        word1, word2 = input().split()
        try:
            s_print(f"{word1} - {word2} = {word1-word2}")
        except TypeError:
            s_print("unsupported operand type(s) for -: 'str' and 'str'")
        sleep(3)
        s_print("same thing with containers, like lists, it gives the same error, but with 'list' instead of 'string'\n")
        sleep(5)
        
    def multiplication():
        s_print("Multiplication is one of the four basic operators, this one repeats whatever it is told to repeat the number of time you repeat it, in case of stuff that is not integers or floating point numbers (known as floats)",
                "Go ahead an enter any two numbers (space seperated, but on the same line)",sep="\n")
        num1, num2 = map(int, input().split())
        s_print(f"{num1}*{num2} = {num1*num2}", 
                "pretty cool right, well that's not even the best part yet, we can do this with containers like lists and tuples, we can also do this with strings",
                "Go ahead an enter a string with a number (because obviously we can't multiply text using text), (same line, space seperated)",sep="\n")
        word, num = input().split()
        s_print(f"{word}*{int(num)} = {word*int(num)}", "pretty cool right?", "we can do this using containers too, let me show you", sep="\n")
        s_print(f"[1, 2, 3]*3 = {[1, 2, 3]*3}", "Nice isn't it?", sep="\n")
        s_print("you might've caught on already, but you can't multiply strings with strings or containers, nor can you multiply containers with strings or other containers", "you usually get the following error",
                " can't multiply sequence by non-int of type '{data type}'", 
                "this error means that you can't multiply whatever you are multiplying by a non integer type\n", sep="\n")
        
    def division():
        s_print("Division is on the of the 4 basic operators, and what this does is, it divides a value by another value, but, as you might've guessed, we can't divide anything but numbers (integers or floating point numbers)",
                    "You get a error stating:unsupported operand type(s) for /: '[type]' and '[type]', which means that you can't divide the two types, as long as both of them are not numbers")
        s_print("Go ahead and enter two numbers with (/) sign between them", sep="\n")
        num1, num2 = input()
        s_print(f"{num1}/{num2} = {num1/num2}", "now try strings with (/) between them", sep="\n")
        word1, word2 = input()
        try:
            word1/word2
        except TypeError:
            s_print("unsupported operand type(s) for /: 'str' and 'str'", 
            "as you can see, you can't divide strings with each other, even if they contain numbers, also, you can't divide strings with anything, same thing with containers\n", sep="\n")

