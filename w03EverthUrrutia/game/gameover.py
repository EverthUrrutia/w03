

class Gameover():
    def gameover(self, playerguess, turn):
        if '_' not in playerguess:
            print("CONGRATULATION YOU WIN")
            return True
        elif turn == 6:
            print("GAME OVER")
            return False
    
