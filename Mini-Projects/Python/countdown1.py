# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
    
    while t:
        
        #divmod functions return quotient and remainder
        mins, secs = divmod(t, 60) 
        
        #:02d repesents that minutes and seconds will be represented in 2 digits
        timer = '{:02d}:{:02d}'.format(mins, secs) 

        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Time\'s up!!!') 


# input time in seconds 
t = input("For how many seconds do you want to set the timer? ") 

# function call 
countdown(int(t)) 

