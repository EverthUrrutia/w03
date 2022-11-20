
from game.gameover import Gameover
from game.parachute import Parachute
from game.playerguess import Playerguess
from game.secretword import Secretword
from game.check import Check
from game.display import Display

class Director():

    def __init__(self):
        self.word = ""
        self.displayword = []
        self.parachute = ""
        self.game = True

    def start_game(self):
        
        word = Secretword().wordList()
        self.word = word

        self.displayword = Secretword().wordDisplay(word)
            
        i = 1
        print(Parachute().parachute(i))

        while self.game:
            print(self.displayword)

            guess = Playerguess().get_input()
            check = Check().check(guess, self.word, self.displayword)
            
            if check:
                self.displayword  = Display().display(guess, self.word, self.displayword)  
                print(Parachute().parachute(i))

            else:
                i += 1
                print(Parachute().parachute(i))

            game = Gameover().gameover(self.displayword ,i)
            
            if game or game == False:
                print(self.displayword)
                break
