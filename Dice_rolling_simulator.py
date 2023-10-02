#Importing Random Module.

import random

#Using While Loop to continue rolling Dice until User wants to stop.
cont="y"
while cont=="y":
    choice=random.randint(1,6)
    print(choice)

    if choice==1:
        print('''
[       ]
[   o   ]
[       ]''')
    elif choice==2:
        print('''
[ o     ]
[       ]
[     o ]''')
    elif choice==3:
        print('''
[ o     ]
[   o   ]
[     o ]''')
    elif choice==4:
        print('''
[ o   o ]
[       ]
[ o   o ]''')
    elif choice==5:
        print('''
[ o   o ]
[   o   ]
[ o   o ]''')
    elif choice==6:
        print('''
[ o   o ]
[ o   o ]
[ o   o ]''')

    cont=input("Do you want to roll the Dice again?   (y/n)")

