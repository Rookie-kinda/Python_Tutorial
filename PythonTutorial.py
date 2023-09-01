from time import sleep
import sys
class PythonTutorial:
    def slow_print(self, *items, sep: str="", slp:int=0.5):
        for string in items:
            if not isinstance(sep, str):
                raise TypeError(f"'sep' parameter only accepts str as arguments not {type(sep).__name__}")
            string = string + sep
            sleep(slp)
            for letter in string:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    sleep(5/100)
            string += "\n"