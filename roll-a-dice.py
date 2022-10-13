import random


print('''
[-----]
[     ]
[  0  ]
[     ]
[-----]
''')
wannaroll=input("press y to roll again and n to exit - ")
while wannaroll !="n":
    if(wannaroll == "y"): 
        num=random.randint(1,6)
        if num == 1:
            print('''
    [-----]
    [     ]
    [  0  ]
    [     ]
    [-----]''')
        elif num == 2:
            print('''
    [-----]
    [     ]
    [ 0   ]
    [   0 ]
    [-----]''')
        elif num == 3:
            print('''
    [-----]
    [     ]
    [0 0 0]
    [     ]
    [-----]''')
        elif num == 4:
            print('''
    [-----]
    [0   0]
    [     ]
    [0   0]
    [-----]''')
        elif num == 5:
            print('''
    [-----]
    [0   0]
    [  0  ]
    [0   0]
    [-----]''')
        elif num == 6:
            print('''
    [-----]
    [0   0]
    [0   0]
    [0   0]
    [-----]''')
    wannaroll=input("press y to roll again and n to exit - ")
