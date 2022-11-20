#Lucca

class Display():
    # display changes the word for a blanks _ _ _ _, everytime the user guess right,
    # the blank is switched to the letter

    def display(self, guess, word, displayword ):
        
        # loop trough every letter of the word, when there is a match, 
        # the '_____' change to '____a_', for example
        # and return the value to director, to be displayed in the terminal
        
        for position in range(len(word)):
            letter = word[position]

            if letter == guess:
                displayword[position] = guess
        return displayword