import os
import csv

class Organizer:
    cwd = os.getcwd()
    typeOfOrganizer = ""
    def accessFile(self):
            with open(Organizer.cwd+"/ProjectOne/fileManagers/WordFiles/"+Organizer.typeOfOrganizer+"Words.cvs", newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            print(data)