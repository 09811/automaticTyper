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
        if char == '\n':                    #<- You dont have to type this at each line end! At the bottom of this page is an example!
            keyboard.press(Key.enter)  
            keyboard.release(Key.enter)
        time.sleep(btime) 


        
def runProgram(keyboard):            #<- Created this function because my plan was to make a bigger project out of it... Basicly just presses one button to debug the program. It takes the keyboard as an argument to emulate the keys
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
        
        
typeText(keyboard, codestring, 0)       #<- Here we just call the type function with the kayboard, text, and btime parameters
runProgram(keyboard)                   #<- at the end it will debug the program (you can remove this and the runProgram function) we dont need a sleep because the compiler takes some time to start (watch examples)



''' #<- Not content of the string only commented out
codestring = """
//Simple Bubble-Sort in C++
#include <iostream>

void bubbleSort(int arr[], int size) {
	for (int i = 0; i < size - 1; ++i) {
		for (int j = 0; j < size - i - 1; ++j) {
			if (arr[j] > arr[j + 1]) std::swap(arr[j], arr[j + 1]);
		}
	}
}

int main() {
	int arr[] = { 12, 45, 78, 3, 26, 61, 89, 34, 50,
        5, 92, 18, 67, 7, 41, 98, 23, 56, 14, 81}; //Array to sort
	int size = sizeof(arr) / sizeof(arr[0]);
	bubbleSort(arr, size);
	std::cout << "Sorted array: ";
	for (int i = 0; i < size; ++i) std::cout << arr[i] << " ";
	std::cout << std::endl;
	return 0;
}
"""

each line break will be automaticlly dedectet as \n
''' 
