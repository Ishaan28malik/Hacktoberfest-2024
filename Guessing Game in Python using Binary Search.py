# Python implementation for the 
# number guessing using 
# Binary Search 

# Global Arguments for playing game 
args = ["N", "N", "Y"] 
index = -1

# Temporary function for taking 
# input from the local arguments list 
def input(): 
	global index, args; 
	index += 1
	return args[index] 

# Function to guess the number in 
# a defined range of the number 
def guessNumber(startRange, endRange): 
	if startRange > endRange: 
		return True
	
	# Middle of the range 
	mid = (startRange + endRange)//2
	
	# Asking user about the 
	# actual number 
	print("Is the number is ", 
		mid, "?", end = " ") 
	user = input() 
	print(user) 
	
	# Condition to check if the 
	# guessed number is actual number 
	if user == "Y" or user == "y": 
		print("Voila ! Successfully Guessed Number.") 
		return False
		
	# Condition to check if the 
	# guessed number is not correct 
	elif user == "N" or user == "n": 
		print("Actual number is greater than",\ 
						mid, "?", end = " ") 
		user = input() 
		print(user) 
		if user == "Y" or user == "y": 
			return guessNumber(mid+1, endRange) 
		elif user == "N" or user == "n": 
			return guessNumber(startRange, mid-1) 
		else: 
			print("Invalid Input. Print 'Y'/'N'") 
			return guessNumber(startRange, endRange) 
	
	# Condition to check if the user 
	# input was invalid 
	else: 
		print("Invalid Input. Print 'Y'/'N' ") 
		return guessNumber(startRange, endRange) 

# Driver Code 
if __name__ == "__main__": 
	print("Number Guessing game in python") 
	startRange = 1
	endRange = 10
	print("Guess a number in range (1 to 10)") 
	
	out = guessNumber(startRange, endRange) 
	
	if out: 
		print("Bad Choices") 
