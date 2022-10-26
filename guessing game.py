# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:40:09 2021

@author: TOBBY
"""

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
    else:
        print('sorry you failed')
        

#a car game
command = ""
started = False    #to define a statement to symbolise the car is stopped at first in the beginning of the game
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else: 
             started = True
             print("car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""----COMMANDS-----
              \nstart- TO START THE CAR
              \nstop- TO STOP THE CAR
              \nquit- TO QUIT THE GAME""")
    elif command == "quit":
        print("game exited sucessfully")
        break
    else:
        print("sorry i do not understand the command input 'help' to view commands")

