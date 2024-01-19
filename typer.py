from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

codestring = """            
Your code goes here         
"""
#You might want to change this because it will adds a empty line at the start and and. If you dont want it change it like this: codestring="""Your code without line break and the start and end""" (You can still have multiple lines just place the " next to the first and last word)


time.sleep(4)  #<- This will wait 4 second so you have time to switch into the input field


def typeText(keyboard, text, btime):        #<- This function writes the string and takes the following parameter: keyboard (to emulate the keys), text (is the string), btime -> Button time (the time it will wait after each key 0 will basicly paste it in)
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        #if char == '\n':
        #    keyboard.press(Key.enter)  
        #    keyboard.release(Key.enter)
        time.sleep(btime) 


        
def runProgram(keyboard):            #<- Created this function because my plan was to make a bigger project out of it... Basicly just presses one button to debug the program. It takes the keyboard as an argument to emulate the keys
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
        
        
typeText(keyboard, codestring, 0)       #<- Here we just call the type function with the kayboard, text, and btime parameters
runProgram(keyboard)                   #<- at the end it will debug the program (you can remove this and the runProgram function) we dont need a sleep because the compiler takes some time to start (watch examples)
