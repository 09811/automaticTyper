from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

codestring = """
Your code goes here
"""



time.sleep(4)


def typeText(keyboard, text, btime):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        #if char == '\n':
        #    keyboard.press(Key.enter)  # Adjust sleep time if needed
        #    keyboard.release(Key.enter)
        time.sleep(btime)  # Adjust sleep time if needed 
def runProgramm(keyboard):
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
        
        
typeText(keyboard, codestring, 0)
#runProgramm(keyboard)