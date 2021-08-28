from phrasehunter.game import Game

playing = True


def play_again():
    while True:
        user_response = input("\nWould you like to play again? Enter y or n: ").lower()
        if user_response == 'y':
            print("Sweet! Give it another go!")
            return True
        elif user_response == 'n':
            print("Thanks for playing! See you next time!")
            return False
        else:
            print("Please enter y or n only!")


if __name__ == '__main__':
    while playing:
        game = Game()
        game.start()
        playing = play_again()

