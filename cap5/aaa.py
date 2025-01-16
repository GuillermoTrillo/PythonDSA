numberList = []

def MainMenu(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Escolha seu tipo de operação")
    print("+")
    print("-")
    print("x")
    print("/")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    operation = input("Escreva o simbolo: ")
    GetOperation(operation)
    
def GetOperation(operation):
    if operation == "+":
        GetNumbers()
        Addition()
    elif operation == "-":
        GetNumbers()
        Subtraction()
    elif operation == "x":
        GetNumbers()
        Multiplication()
    elif operation == "/":
        GetNumbers()
        Division()
    else:
        MainMenu()
        
        
def GetNumbers():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Quantos numeros diferentes você vai querer tratar?")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    numberQuantity = int(input("Escreva a quantidade: "))
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    i = 0
    for i in range(numberQuantity):
        numberList.append(int(input("Escreva a quantidade da posição "+str(i+1)+": ")))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def Addition():
    totalNumber = 0
    i = 0
    for i in numberList:
        totalNumber += i
    ShowResult(totalNumber)

def Subtraction():
    totalNumber = 0
    i = 0
    for i in numberList:
        totalNumber = totalNumber - i
    ShowResult(totalNumber)
        
def Multiplication():
    totalNumber = 0
    i = 0
    for i in numberList:
        totalNumber = totalNumber * i
    ShowResult(totalNumber)
    
def Division():
    totalNumber = 0
    i = 0
    for i in numberList:
        totalNumber = totalNumber / i
    ShowResult(totalNumber)
    
def ShowResult(totalNumber):
    print("The total was ", totalNumber, "\n")
    EndOfEverything()
    
def EndOfEverything():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Quer fazer de novo? Não terminaria o processo.")
    print("S")
    print("N")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    answer = input("Escreva o simbolo: ")
    
    if answer == "S":
        MainMenu()
    elif answer == "N":
        return
    else:
        numberList.clear
        EndOfEverything()
    
MainMenu()