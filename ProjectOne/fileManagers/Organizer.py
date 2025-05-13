import os
import csv

class Organizer:
    
    cwd = os.getcwd()
    
    def accessFile(self):
            with open(Organizer.cwd+"/ProjectOne/fileManagers/WordFiles/"+self.typeOfOrganizer+"Words.cvs", newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            print(data)