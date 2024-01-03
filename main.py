import twoplayer
import ai_computer

def main_game():
    while True:    
        game_mode = input("\nSelect a mode:\n\t (a) 2-player\n\t (b) versus computer\nType either a or b: ")
        if game_mode == "a":
            mode = twoplayer
            print("\nTic-Tac-Toe 2-player mode:")
            mode.game_play()
            restart(mode)
        elif game_mode == "b":
            mode = ai_computer
            print("\nTic-Tac-Toe vs. computer mode")
            mode.game_play()
            restart(mode)
        else:
            print("Invalid input. Please type either 'a' for 2-player or 'b' for versus computer: ")

def restart(mode):
    while True:
        restart = input("\nWould you like to:\n\t (a) Play another game\n\t (b) Change game mode\n\t (c) Quit\nType either a, b, or c:  ")
        if restart == "a":
            mode.restart()
            mode.game_play()
        elif restart == "b":
            mode.restart()
            main_game()
        elif restart == "c":
            print("\nThank you for playing :)\n")
            quit()
        else: 
            print("\nInvalid Input. Please choose either a, b, or c. \n")


main_game()