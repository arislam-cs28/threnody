###############################################################################################################################
# ALL IMPORT DECLARATIONS
###############################################################################################################################

import storyline as st          # importing the main storyline and initializing it
import var_storage as vts       # importing all of the main variables and initializing them

###############################################################################################################################
# MAIN FILE FUNCTIONS
###############################################################################################################################

# Declaring system requirements onto terminal before executing actual game
def system(): # Function Complete
    print()
    print("####################################")
    print("System requirements before playing:")
    print("""
    - A terminal that runs python3
    - A modern, ANSI-compatible console that can render ANSI-codes for a more immersive experience
    - A compatible Windows, MacOS, or Linux operating system """)
    print()


# Declaring trigger warning agreement before playing actual game
def trigger_warnings(): # Function Complete
    print("####################################")
    print("This Python text-based game contains gore, mentions of death, and other disturbing content.")
    print("Your mental health matters. Please pause to consider if you would like to play or not.")
    print("Type \"yes\" (exactly as it is written, excluding quotation marks) to assure that you would like to proceed.")
    print("If not, you will be redirected to exit the game.")
    confirmation_to_play = input("Type here: ").strip().lower()

    if confirmation_to_play == "yes":
        main_menu()
    else:
        print()
        print("You have exited the game.")
        print("Thank you for considering \033[3mThrenody\033[0m.")
        exit()


# Giving the player a synopsis of the game, the tags for the game, and a full list of trigger warnings
def game_overview():
    print("""
    """)


# Giving the player a full list of how to play, and valid inputs
def play_guides():
    print("Welcome to the \033[3mThrenody\033[0m playing guide.")


# Giving the player info on how to contact me [at the time of writing this, the developer is arislam-cs28 on GitHub and blueheart.elf on everything else]
def contact():
    print("email")


# Giving the player a full overview of the things they may do on the main menu
def main_menu(): # Function Complete
    print()
    print("""####################################
Welcome to the main menu of \033[3mThrenody\033[0m, a text-based game where you make choices to navigate the waters of grief, violence, and an exploration of the human psyche.

Options:
    - To see the full game synopsis tags, type: 1
    - To get instructions on how to play, type: 2
    - To begin playing, type: 3
    - To contact the original developer with bug notices, questions, or just thoughts on the game, type: 4""")
    action = int(input("What would you like to do? "))

    if action == 1:
        game_overview()

    elif action == 2:
        play_guides()

    elif action == 3:
        vts.player_name = input("What is your name? ")
        print(f"Nice to meet you, {vts.player_name}.")
        print("Your experience begins \033[3mnow.\033[0m")

        st.beginning()


    elif action == 4:
        contact()

    else:
        print("Invalid input. Please try again.")
        main_menu()


###############################################################################################################################
# RUNNING THE GAME ITSELF
###############################################################################################################################

def main(): # Function Complete
    system()
    trigger_warnings()


main()