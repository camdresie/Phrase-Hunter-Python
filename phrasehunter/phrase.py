# Create your Phrase class logic here.


class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def check_guess(self, guess):
        if guess in self.phrase:
            print("Sweet! You got a letter!\n")
            return True
        else:
            print("Oops! That one isn't in the phrase!\n")
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
