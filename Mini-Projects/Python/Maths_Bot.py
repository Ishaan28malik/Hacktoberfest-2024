# Hello Friends i know it took long but its finally here, This code helps you or your kid to do thier homework.
# IF YOU WANT TO UPDATE IT JUST UPDATE IT BY YOU PR'S
# HERE YOU GO


# INTRO
print ("Mathyy,  A helping bot for kids and their homework")



# Variables for story flow control
noReturn = False
fear = False
cMenu = False
enMenu = False
talkMenu = False
hitMenu = False
talk = False
apology = False
beep = False
end = 0
c = 0
i = 0
h = 0
t = 0
e = 0

# Story branches for Compliment (c) interactions
def rel_c():
  global fear
  global noReturn
  global talk
  global talkMenu
  global enMenu
  global hitMenu
  global apology
  global i
  global c
  global t
  global h
  global e
	# After talking to MB about dreams - to Neutral ending
  if noReturn == False and t > 0:
			if e == 1 and i == 0:
			  print "> If you want to say yes, you should encourage it again."
			elif i == 0:
				print ("> You listen to its dream, but tell Math Bot that it's much better"
						" at math than art, and that being a Math Bot is much easier than"
						" being an artist. It seems a little sad to hear that, but it" 
						" respects your opinion.")
				end(2)
			else:
				i = 0
				print ("> You apologize for making fun of it. Math Bot accepts your"
				        " apology and forgives you.")
  elif noReturn == False and talk == False:
		# No insult / Good path for game
		if c == 0 and i == 0:
			print ("> You thank Math Bot for solving that last problem for you." 
					 " It doesn't understand and blinks at you in response.")
			c = 1
		elif c == 1 and i == 0:
			c = 2
			print ("> You tell Math Bot that it's very good at math. It still doesn't"
					 " understand why you're being nice to it, but you see its eyes light" 
					 " up a little.")
		elif c == 2 and i == 0:
			c = 3
			print ("> You tell Math Bot that you appreciate all of its hard work."
					" Math Bot seems genuinely happy.")
			talkMenu = True
			print "> You can now talk to Math Bot!"
		elif c == 3 and i == 0:
			print ("> You continue to say nice things to Math Bot. It seems happy, but"
			        " looks like it wants to talk more.")
		# Going back to neutral path after 1-2 insults
		elif c == 0 and i == 1:
			i = 0
			print "> Math Bot blinks."
		elif c == 0 and i == 2:
			i = 0
			print "> Math Bot blinks."
		else:
			print "ERROR"
	# Reaction after being abused
  elif noReturn == True and talk == False:
		if c == 0:
			apology = True
			c = 1
			print ("> You try to apologize for all of the horrible things you did." 
				   " Math Bot is still terrified. It doesn't believe you.")
		elif c == 1:
			apology = True
			c = 2
			print ("> You continue to apologize profusely, tears in your eyes. Math"
					" Bot looks at you, still a little afraid.")
		# If you did hit - final apology
		elif c == 2 and h > 0:
			apology = True
			c = 3
			print ("> You gently pick up Math Bot and do what you can to take out the" 
					" dents. Math Bot flinches as you pick it up. Despite your best" 
					" efforts, you can still see the spots where the dents were. Math"
					" Bot isn't scared anymore, but doesn't seem to trust you.")
			talkMenu = True
		# If you didn't hit - final apology
		elif c == 2 and h == 0:
			apology = True
			c = 3
			print ("> You tell Math Bot that you didn't mean what you said, and that" 
			        " you're actually very thankful to have it and think that it's"
			        " wonderful. Math Both isn't scared anymore, but doesn't seem to"
			        " trust you.")
			talkMenu = True
		elif c == 3:
		  print "> You say nice things about Math Bot. It blinks."
		else:
			print "ERROR"
	# Loop until you encourage again. After abuse.
  elif noReturn == True and talk == True:
		print "> Math Bot listens to you and blinks."
  else:
		print "Math Bot blinks."

# Define all insult reactions		
def rel_i():
  global fear
  global noReturn
  global talk
  global talkMenu
  global enMenu
  global hitMenu
  global apology
  global i
  global c
  global t
  global h
  global e
	# After talking to MB, insults - can put on Neutral path
  if noReturn == False and talk == True and apology == False:
    if i == 0 and t < 3:
			i = 1
			print ("You tell Math Bot that you thought it was too dumb to actually"
					" talk. It seems a little upset.")
		# Final insult before noReturn hits
    elif i == 1 and t < 3:
			i = 2
			print ("> You continue to make fun of Math Bot and tell it that it's just a" 
					" robot and should stick to doing its job. Math Bot is confused. It"
					" thought you liked talking to it.")
		# noReturn triggered, down to bad path
    elif i == 2 and t < 3:
			i = 3
			c = 0
			t = 0
			talk = False
			talkMenu = False
			noReturn = True
			hitMenu = True
			print ("> You loudly complain how long it takes Math Bot to do its job and" 
			        " that it's completely useless. Math Bot blinks. It seems sad, and" 
			        " looks at you as if asking what it can do better.")
		# To Neutral end
    elif i == 0 and t == 3:
			print ("> You tell Math Bot that its art is awful, and it'll never be an" 
			        " artist. It should stick to doing math. Math Bot is sad.")
			end(2)
		# Reply "no" to "Do you mean it?"
    elif i == 0 and e == 1 and talk == True:
			i = 1
			print ("> You tell Math Bot that no, you didn't actually mean it and were"
			        " just being nice. Math Bot is surprised and a little sad.")
		# Insult after replying "no". To Neutral end.
    elif i == 1 and e == 1 and talk == True:
			print ("> You tell Math Bot that its art is awful, and it'll never be an" 
			        " artist. It should stick to doing math. Math Bot is sad.")
			end(2)
	# Initial insult reactions - to bad path
  if noReturn == False and apology == False:
		if i == 0 and c == 0:
			i = 1
			print ("> You mutter that a calculator is easier to use than Math Bot."
			        " Math Bot doesn't understand.")
		elif i == 1 and c == 0:
			i = 2
			print ("> You point out how little Math Bot can actually do. Math Bot blinks"
			        " in response. It still doesn't understand why you're saying these"
			        " things.")
		# Point of no return - hit unlocks
		elif i == 2 and talk == False:
			i = 3
			c = 0
			t = 0
			print ("> You loudly complain how long it takes Math Bot to do its job and" 
			        " that it's completely useless. Math Bot blinks. It seems sad, and" 
			        " looks at you as if asking what it can do better.")
			print  "> Hit unlocked!"
			hitMenu = True
			talkMenu = False
			enMenu = False
			noReturn = True	
		# Going back to neutral path after 1-2 insults
		elif i == 0 and c == 1:
			c = 0
			print "> Math Bot blinks."
		elif i == 0 and c == 2:
			c = 0
			print "> Math Bot blinks."
		else:
			print "Math Bot blinks at you."
	# To bad path - fear on
  elif noReturn == True and apology == False and talk == False:
		if i == 3:
			i = 4
			t = 0
			fear = True
			print ("> You shout at Math Bot. You tell it that you never should have bought"
			        " it and that it can't do anything right. It has tears in its eyes.")
		elif i == 4:
			i = 5
			t = 0
			print ("> You continue shouting at Math Bot. You call it horrible, nasty"
			        " names and tell it that it is and always will be a miserable failure."
			        " Math Bot is crying and doesn't understand what it did wrong.")
		elif i == 5:
			i = 6
			print ("> You scream at Math Bot as loud as you can. It tries to apologize," 
			        " but you refuse to listen and keep yelling. It becomes completely"
			        " unresponsive as you continue to yell at it.")
		elif i == 6:
			end(3)
		else:
			print "Math Bot blinks at you."
	# Ending after apologizing and then insulting again.
  elif noReturn == True and apology == True:
			end(3)
  else:
		print "Math Bot blinks."

#Define "talk" interactions
def rel_t():
  global fear
  global noReturn
  global talk
  global talkMenu
  global enMenu
  global hitMenu
  global apology
  global i
  global c
  global t
  global h
  global e
	# Good path talk interactions
  if noReturn == False:
    # if you insulted Math Bot before
    if i != 0:
	    print ("> Math Bot is upset. Maybe you should try apologizing first?")
    elif t == 0:
      t = 1
      print ("> You ask Math Bot about itself. Math Bot is surprised, but"
	           " happy. A little window flashes up on the screen in response."
	           " You have a good time talking with Math Bot.")
      talk = True
    elif t == 1:
      t = 2
      print ("> You ask Math Bot what it thinks of its job. Math Bot tells"
	           " you that it likes doing math, but that there are other things"
	           " that it likes doing more. It tells you that you're the first"
	           " person that's ever asked about what it thinks before. Math"
	           " Bot says that it's happy to have someone to talk to.")
    # unlock "Encourage" here
    elif t == 2:
	    t = 3
	    print ("> You ask Math Bot about its dream. Math Bot shyly tells you"
	           " that it actually wants to be an aritst. It nervously shows"
	           " you some of the work that it secretly made. It looks like"
	           " it wants some encouragement.")
	    print "> Encourage unlocked!"
	    enMenu = True
    # extra info from talking
    elif t == 3:
	    t = 4
	    print ("> You ask Math Bot about why it wanted to become an artist."
	           " it tells you that, while it likes math, it's tired of only"
	           " being able to do what other peole tell it to do. Math Bot"
	           " says that it wants to express itself more, be more creative,"
	           " and show people that Math Bots can do more than math.")
    # talk loop
    elif t == 4:
	    print ("> Math Bot is waiting for you to say something. Will you"
	           " encourage it to be an artist, or compliment it and say that"
	           " it's better at math?")
  # after apologizing
  elif noReturn == True:
    if t == 0:
      t = 1
      print ("> You ask Math Bot about itself. A little window flashes up"
	           " on the screen with its response. You have a good time talking"
	           " with Math Bot.")
    elif t == 1:
      t = 2
      print ("> You ask Math Bot what it thinks about its job. Math Bot tells"
	           " you that it likes doing math, but that it has other hobbies"
	           " it likes doing more.")
    elif t == 2:
      t = 3
      print ("> You ask Math Bot about its dreams. It gives a vague response"
	           " and says it doesn't really matter because it could never do it"
	           " anyways, and says that it would rather just continue being a"
	           " Math Bot.")
      print "> Encourage unlocked!"
      enMenu = True
    elif t == 3:
      print ("> Math Bot has gotten quiet. Maybe you should try encouraging"
	           " it a little...?")

# Define all encourage interactions.
def rel_e():
  global fear
  global noReturn
  global talk
  global talkMenu
  global enMenu
  global hitMenu
  global i
  global c
  global t
  global h
  global e
	# To best ending
  if noReturn == False:
	    if e == 0:
	        e = 1
	        print ("> You tell Math Bot that it has a wonderful dream, and should"
	               " just go for it. Math Bot lights up and looks happier than"
	               " you've ever seen it. It asks if you really mean that.")
	    elif e == 1:
	        end(1)
  # To ending after abusing and trying to encourage again
  elif noReturn == True:
	    end (4)

# Define all hit interactions
def rel_h():  
  global fear
  global noReturn
  global talk
  global talkMenu
  global enMenu
  global hitMenu
  global apology
  global i
  global c
  global t
  global h
  global e
	# first hit triggers fear
  if apology == True:
	  end(3)
  elif h == 0:
    h = 1
    noReturn = True
    fear = True
    print ("> You smash the top of Math Bot as hard as you can with your fist,"
	         " leaving a dent. Math Bot is stunned. It stares at you with wide eyes.")
  elif h == 1:
    	h = 2
    	print ("> You kick the side of Math Bot violently. It leaves a large dent."
           " It begins crying, begging you to stop.")
  elif h == 2:
		h = 3
		print ("> You pick up Math Bot and throw it at the wall with all of your"
			   " strength. It makes a horrible crunch as the corner of it hits the"
			   " wall, then crashes against the ground. It is a sad, crumpled mess."
			   " Math Bot is sobbing quietly, apolgoies flashing on the screen,"
			   " promisng you that it will do better next time if you just stop.")
  elif h == 3:
    end(5)

# Define all endings
def end(x):
  if x == 1:
    print ("> You say yes, you really mean it, and say that you think that the"
           " are it made is really impressive. Math Bot is thrilled. Math Bot"
           " tells you taht it's going to work as hard as it can to make its"
           " dreams come true, and departs on a journey to become a great artist.")
    print ("> A few months later, you see a news story about Math Bot on TV - its"
           " new name is Art Bot. Art Bot is the first robot to create new works of"
           " art without any human input, and demand for its work is high. In an"
           " interview, it tells the reporter about how grateful it is for you and"
           " your encouragement. Art Bot continues to keep in touch with you, and"
           " sends you new pieces from time to time.")
    print "> Art Bot loves you!"
    print "> Thank you for being so kind to Art Bot!"
    print "END"
    quit()
  elif x == 2:
    print ("> Math Bot has decided that being an artist was a silly dream, and that"
           " it's much more practical and safer to continue being a Math Bot. You"
           " keep Math Bot, and it continues to be very good at it's job. But every"
           " once in a while, you notice it still trying to create new artwork while"
           " you're not using it. You and Math Bot live a happy, normal life.")
    print "END"
    quit()
  elif x == 3:
    print ("> Math Bot can't take any more. It shuts itself down. No matter what"
           " you try, it won't turn back on again. All you've been left with is"
           " a hunk of metal.")
    print "END"
    quit()
  elif x == 4:
    print ("> You try to be encouraging. Math Bot is furious and confused - why"
           " are you being nice after all of those awful things you did? Math Bot"
           " can't understand. It can't forgive you. It shuts itself down. No"
           " matter what you try, it won't turn back on again. All you've been"
           " left with is a hunk of metal.")
    print "END"
    quit()
  elif x == 5:
    print ("> You continue to hit Math Bot. Again. And again. And again. It isn't"
           " until your hands start to hurt that you realize that you've"
           " compltely destroyed it. Math Bot is dead, broken beyond repair. You"
           " stare at the misshapen hunk of metal, pick it up, and throw it away.")
    print "END"
    quit()



# Set up math program
x = 0
y = 0

def maths ():
	if fear == True:
		print "Math Bot is too terrified to do math."
	else:
		sum = 0
		output = ""
		print "> Enter first number."
		while True:
			try:
				x = int(raw_input("> "))
			except ValueError:
				print("> Please type a number.")
				continue
			else:
				break
		print "> Enter second number."
		while True:
			try:
				y = int(raw_input("> "))
			except ValueError:
				print("> Please type a number.")
				continue
			else:
				break		
		while True:
			print "> What kind of calculation would you like to perform?"
			print "> + , - , * , / (enter the symbol to continue)"
			calc = raw_input("> ")
			if calc == "+":
					sum = x + y
					output = str(sum)
					print "> " + output
					break
			elif calc == "-":
					sum = x - y
					output = str(sum)
					print "> " + output
					break
			elif calc == "*":
					sum = x * y
					output = str(sum)
					print "> " + output
					break
			elif calc == "/":
					sum = x / y
					output = str(sum)
					print "> ANSWER: " + output
					break
			else:
					print "> Please try again."
					continue

# Define "graphics" part of menu.
def graphics():
	while True:
		print "> Please choose one of the following:"
		print "> Resolution, Background Color, Back"
		input = raw_input("> ")
		input = input.lower()
		if input == "resolution":
			print "> You hit some buttons. It's much clearer now."
			break
		elif input == "background color":
			print ("> You hit some buttons." 
		    	   " You like the new color better than the old one.")
			break
		elif input == "back":
			break
		else:
			print "> Choose an option."
			continue

# Define "Audio" part of menu
def audio():
  global beep
  while True:
		print "> Choose one of the following:"
		print "> Toggle beep on/off, Back"
		input = raw_input("> ")
		input = input.lower()
		if "toggle" or "beep" in input:
			if beep == False:
				print ("> You hit the button." 
				 	   " There are now beeping sounds when you hit the buttons.")
				beep = True
				break
			elif beep == True:
				print "> You decided the beeping sound is annoying and turn it off."
				beep = False
				break
		elif input == "back":
				break		
		else:
				print "Please choose an option."
				continue


# Set up initial variables
power = False
first = False
second = False
more = False
rel = 0

# Introduction to game
print "> You are the proud owner of a brand new Math Bot." 
print ("> The instruction manual says - 'Thank you for your purchase!" 
       " Math Bot was created to take care of all of your computational needs.")
print "> There is a small, silver cube directly in front of you. What do you do?"
print "> turn on, walk away (type the option that you want to select, and hit enter)"

# First choice
while power == False:
	input = raw_input("> ")
	input = input.lower()
	if input == "walk away":
    		print "> You decide to turn on the Math Bot later."
    		power = True
    		finish = True
	elif input == "turn on":
    		print ("> You turn on the Math Bot on. The screen on the silver cube" 
    		       " lights up, and two little glowing eyes stare back at you.")
    		print ("> There is a menu underneath the little eyes." 
    		       " There is only one option - 'math'.")
    		power = True
    		first = True
	else: 
			print "> Please enter 'turn on' or 'walk away'."

# Power is on - first math demonstration		
while first == True:
	print "> What would you like to do?"
	input = raw_input("> ")
	input = input.lower()
	if input == "math":
			maths()
			print "> CONGRATULATIONS!"
			print "> You have performed your first calculation!"
			print "> Options menu opened!"
			first = False
			second = True
	else:
			print "> Please enter 'math'."

# Add options to menu
while second == True:
	print "> There are now two buttons on the menu - math and options. The little eyes blink."
	print "> What will you do?"
	input = raw_input("> ")
	input = input.lower()
	if input == "math":
			maths()
	elif input == "options":
			while True:
				print "> Choose one of the following:"
				print "> Graphics, Audio, Additional Commands, Back"
				input = raw_input("> ")
				input = input.lower()
				if input == "graphics":
					graphics()
					continue
				elif input == "audio":
					audio()
					continue
				elif input == "additional commands":
					print "> Additional commands unlocked!"
					print "> A group of commands pops up on the menus. The little eyes stare at you."
					more = True
					second = False
					break
				elif input == "back":
					break
				else:
					continue
	else:
			print "Please write 'math' or 'options'."	

# Final system of menus			
while more == True:
  print "> Choose: math, options, compliment, insult"
  if talkMenu == True:
    print "talk"
  if enMenu == True:
    print "encourage"
  if hitMenu == True:
    print "hit"
  input = raw_input("> ")
  input = input.lower()
  if input == "math":
			maths()
			continue
  elif input == "options":
			options()
			continue
  elif input == "compliment":
			rel_c()
			continue
  elif input == "insult":
			rel_i()
			continue
  elif input == "talk" and talkMenu == True:
      rel_t()
      continue
  elif input == "hit" and hitMenu == True:
      rel_h()
      continue
  elif input == "encourage" and enMenu == True:
      rel_e()
      continue
  else:
			print "Choose one of the options."
