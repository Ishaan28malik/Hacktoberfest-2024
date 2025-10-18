import pyautogui
import time

def screenshot():
    choice = input("Do you want custom options(y/n): ")
    
    if choice.lower() == 'y':
        file_name = input("Enter a file name: ")
        
        file_ext = input("Enter a file extension: ")
        
        delay = int(input("Enter delay(seconds): "))
        
        name = f'{file_name}.{file_ext}'
        
        time.sleep(delay)
        
    elif choice.lower() == 'n':
        name = int(round(time.time() * 1000))
        
        name = f'{name}.png'
    else: 
        print('invalid input ')
        
    img =  pyautogui.screenshot(name)
    
    img.show()   
    
if __name__ == "__main__":
    screenshot()
