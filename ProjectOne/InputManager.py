import Text as Text

class InputManager:
    
    text = Text.Text()
    
    def StartGame(self):
        InputManager.text.startMenu()
        operation = input("Escreva o simbolo: ")
        if operation == "1":
                InputManager.ChooseDifficulty()
        elif operation == "0":
            return
        else:
            InputManager.StartGame()
            
    
    def ChooseDifficulty(self):
        InputManager.text.difficulty()
        
        operation = input("Escreva o simbolo: ")
        if operation == "1":
                InputManager.ChooseDifficulty()
        elif operation == "2":
            return
        elif operation == "3":
            return
        elif operation == "0":
            InputManager.StartGame()
            return
        else:
            InputManager.StartGame()