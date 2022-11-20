
class Parachute():

    def parachute(self, check):

        parachute1 = """
         _____    
        /_____\\
        \     /   
         \   /
           O
          /|\\
          / \ 

        ˄ ˄ ˄ ˄  
        """
        parachute2 = """
         
        /_____\\
        \     /   
         \   /
           O
          /|\\
          / \ 

        ˄ ˄ ˄ ˄ 
        """
        parachute3 = """ 

        \     /   
         \   /
           O
          /|\\
          / \ 

        ˄ ˄ ˄ ˄ 
        """
        parachute4 = """
    
        \   /
          O
         /|\\
         / \ 

       ˄ ˄ ˄ ˄ 
        """
        parachute5 = """
        
         O
        /|\\
        / \ 
        
      ˄ ˄ ˄ ˄ 
        """

        parachute6 = """

         X
        /|\\
        / \ 
        
      ˄ ˄ ˄ ˄ 
        """
        if check == 1:
            return parachute1 
        elif check == 2:
            return parachute2
        elif check == 3:
            return parachute3
        elif check == 4:
            return parachute4
        elif check == 5:
            return parachute5
        else:
            return parachute6