# function to check if two strings are anagram or not 
def check(s1, s2): 
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)): 
		print("The strings are anagrams.") 
	else: 
		print("The strings are not anagrams.")		 
		
# driver code 
s1 =input("Enter first string ")
s2 =input("Enter seconf string ")
check(s1, s2) 
