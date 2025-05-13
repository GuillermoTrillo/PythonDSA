import os

class Text:
    #* Menus
    clear = lambda: os.system('cls')
    
    @staticmethod
    def startMenu():
        Text.clear()
        print("----------------------------")
        print("1. Start Game")
        print("0. Close Game")
        print("----------------------------")
        
    @staticmethod
    
    def difficulty():
        Text.clear()
        print("----------------------------")
        print("1. Easy (3 to 5 letter words)")
        print("2. Medium (6 to 10 letter words)")
        print("3. Hard (7+ letter words)")
        print("0. Go back")
        print("----------------------------")