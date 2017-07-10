# "Guess the number" 
# mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console 

try: 
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 
import random

guess_range = 100

# helper function to start and restart the game 
def new_game():
    # initialize global variables
    global secret_number, num_guess
    secret_number = random.randrange(0, guess_range)
    if guess_range == 100:
        num_guess = 7
    elif guess_range == 1000:
        num_guess = 10
    print
    print "New game, range = " + str(guess_range)
    print str(num_guess) + " Guesses left"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global guess_range
    guess_range = 100
    
    new_game()
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global guess_range
    guess_range = 1000
    
    new_game()
    
 
def input_guess(guess):
    # main game logic goes here
    global num_guess

    guess = int(guess)
    num_guess -= 1

    print
    print "Guess was " + str(guess)
    if num_guess == 0:
        print "Guesses used up, game reset"
        new_game()
    elif guess > secret_number:
        print "Lower"
        print str(num_guess) + " Guesses left"
    elif guess < secret_number:
        print "Higher"
        print str(num_guess) + " Guesses left"
    elif guess == secret_number:
        print "Correct"
        new_game()
    
        
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame 
f.add_input("Guess", input_guess, 200) 
f.add_button("Range is [0, 100)", range100) 
f.add_button("Range is [0, 1000)", range1000)

# call new_game
new_game()
