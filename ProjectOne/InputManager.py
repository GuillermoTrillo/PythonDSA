from fileManagers import Organizer as Organizer
import GameDealer as GameDealer
import Text as Text

class InputManager:
    
    text = Text.Text()
    gameDealer = GameDealer.GameDealer()
    
    def StartGame(self):
        InputManager.text.startMenu()
        operation = input("Your input: ")
        if operation == "1":
                InputManager.ChooseDifficulty(self)
        elif operation == "0":
            return
        else:
            InputManager.StartGame(self)
            
            
            
    
    def ChooseDifficulty(self):
        InputManager.text.difficulty()
        
        operation = input("Your input: ")
        if operation == "1":
            InputManager.startMatch(self, "Easy")
        elif operation == "2":
            InputManager.startMatch(self, "Medium")
            return
        elif operation == "3":
            InputManager.startMatch(self, "Hard")
            return
        elif operation == "0":
            InputManager.StartGame(self)
            return
        else:
            InputManager.ChooseDifficulty(self)
            
    def startMatch(self, difficulty):
        organizer = Organizer.Organizer()
        organizer.accessFile(difficulty)
        randomWord = organizer.getRandomWord()
        InputManager.gameDealer.getChances()
    #def 