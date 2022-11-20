
import random
# The SecretWord class allows you to randomly choose the word that the player must guess, this is done from a list where all the words that will be part of the game are stored


class Secretword():

    def __init__(self):
        self.word = ""

    def wordList(self):

        list = [
            "director",
            "cartoon",
            "library",
            "magazine",
            "rainbow",
            "umbrella",
            "window",
            "family",
            "camera",
            "diamond",
            "handsome",
            "awesome",
            "healthy",
            "humorous"
        ]

        word = random.choice(list)
        self.word = word
        return word

    def wordDisplay(self, word):
        display = []
        for letter in range(len(word)):
            display += "_"
        return display
