###############################################################################################################################
# ALL IMPORT DECLARATIONS
###############################################################################################################################

import storyline as st          # importing the main storyline and initializing it
import var_storage as vts       # importing all of the main variables and initializing them

###############################################################################################################################
# MAIN FILE FUNCTIONS
###############################################################################################################################

# Declaring system requirements onto terminal before executing actual game
def system():
    print("System requirements before playing:")
    print("""
    - A terminal that runs python3
    - A moden, ANSI-compatible terminal or console for a better experience
    """)
    print()


# Declaring trigger warning agreement before playing actual game
def trigger_warnings():
    print("This Python text-based game contains gore, mentions of death, and other disturbing content. ")
    print("Please type \"yes\" (exactly as it is written, excluding quotation marks) to assure that you would like to proceed.")
    print("If not, you will be redirected to exit the game.")
    confirmation_to_play = input("Type here: ").strip().lower()

    if confirmation_to_play == "yes":
        play_guides()
        st.beginning()
    else:
        print("You have exited the game.")
        exit()



def play_guides():
    print("Welcome to the \033[3mThrenody\033[0m playing guide.")



def back_to_main():
    print()
    print("""####################################
    We welcome you to play 
    
    """)



###############################################################################################################################
# RUNNING THE GAME ITSELF
###############################################################################################################################

def main():
    system()
    trigger_warnings()
    play_guides()


main()