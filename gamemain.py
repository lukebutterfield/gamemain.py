"""
Title   : gamecode.py
Version : 1.0
Author  : Luke Butterfield
Date    : 09/11/14

Code to be used as a template for any program written using Pygame. Defines
colours and creates three functions which form the basis of the game loop.

"""

# Using Pygame library of functions.
import pygame

# -------------------- Set Constant Values -------------------------------------

# Define colours, each colour uses an RGB value.
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)

RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)

# Set a maximum frames per second.
MAXFPS = 60

# String for the title of the game.
TITLE  = "The Coolest Game in the World!"

# Height and Width of the screen.
SCREENHEIGHT = 1024
SCREENWIDTH  = 768

# ------------------- Game Functions -------------------------------------------

def init():
# This function is called once before entering the game loop, use this
# to set up the program.

    # Initialise the game engine.
    pygame.init()

    # Set the window title
    pygame.display.set_caption(TITLE)
    
# End def GameInit()




def gameMain():
# This function contains an event loop and will not exit until the pygame.QUIT
# event type is come across.

    done  = False                # Flag for Program loop.
    clock = pygame.time.Clock()  # Clock for managing frames per second.

    # Set up the size of the screen and create a window of it's size.
    size   = (SCREENHEIGHT, SCREENWIDTH)
    screen = pygame.display.set_mode(size)

    # Main Program Loop
    while not done:
        # Main Event Loop
        for event in pygame.event.get():  # User Action.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True               # Change done flag to exit loop.

        # PLACE GAME CODE HERE
    
        # Clear the screen, must be above all other draw commands.
        screen.fill(WHITE)

        # PLACE DRAW CODE HERE

        # Flip the back buffer.
        pygame.display.flip()

        # Limit FPS to set Maximum FPS
        clock.tick(MAXFPS)
        
    # End of Main Program Loop

# End def GameMain()




def shutdown():
# Called after the game loop is finished.

    # PLACE SHUTDOWN CODE HERE

    # Close the engine, closing the window and exiting the program. Must
    # be done last.
    pygame.quit()

# End def GameShutdown()




# --------------------- Main Program -------------------------------------------

def main():

    # Initialise Game, send screen and window size.
    init()

    # Run the Game, contains a loop.
    gameMain()

    # If the game loop has finished, shut down game.
    shutdown()

# End def main()

# If program is being run, not imported, start program by running main.
if __name__ == "__main__":
    main()
