import Text as Text

class InputManager:
    
    text = Text.Text()
    
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
                InputManager.EasyMode(self)
        elif operation == "2":
            InputManager.MediumMode(self)
            return
        elif operation == "3":
            InputManager.HardMode(self)
            return
        elif operation == "0":
            InputManager.StartGame(self)
            return
        else:
            InputManager.ChooseDifficulty(self)
            
    def EasyMode(self):
        print("this is easy mode")
        
    def MediumMode(self):
        print("this is Medium mode")
        
    def HardMode(self):
        print("this is Hard mode")
        