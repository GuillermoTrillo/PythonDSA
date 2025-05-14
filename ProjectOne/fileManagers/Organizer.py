from numpy import random
import os
import csv

class Organizer:
    
    cwd = os.getcwd()
    data = None
    
    def accessFile(self, difficulty):
            with open(Organizer.cwd+"/ProjectOne/fileManagers/WordFiles/"+difficulty+"Words.cvs", newline='') as f:
                reader = csv.reader(f)
                Organizer.data = list(reader)
            
    def getRandomWord(self):
        chosenNumber = random.randint(len(Organizer.data))
        accessedList = Organizer.data[chosenNumber]
        
        chosenNumber = random.randint(len(accessedList))
        return accessedList[chosenNumber]
        