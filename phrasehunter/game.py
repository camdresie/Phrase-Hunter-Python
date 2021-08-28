from phrasehunter.phrase import Phrase
import random


class Game:

    def __init__(self):
        # Game Class Attributes
        self.missed = 0
        self.phrases = []
        self.set_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']
        self.playing = True

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number Missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def welcome(self):
        print("\nWelcome to the Phrase Hunter game! In this game, you will be tasked with guessing letters in a "
              "phrase!\nIf you guess a letter correctly, it wil be displayed in the phrase. Be careful though, "
              "you only get 5 guesses!\nHappy hunting!\n")

    def set_phrases(self):
        phrases_text = ['You win some you lose some', 'What goes up must come down', 'I was born this way',
                   'Today is your day', 'Never stop trying']
        for phrase_text in phrases_text:
            self.phrases.append(Phrase(phrase_text))

    def get_random_phrase(self):
        index = random.randint(0, len(self.phrases) - 1)
        return self.phrases[index]

    def get_guess(self):
        while True:
            try:
                guess = input("\nInput a letter to guess: ").lower()
                if guess.isalpha() and not len(guess) > 1:
                    return guess
                else:
                    raise ValueError
            except ValueError:
                print("You must guess a single letter")

    def game_over(self):
        if self.missed == 5:
            print("Uh-oh! Looks like you didn't get the phrase this time!")
        else:
            print("Yes to you! You got the phrase!")
