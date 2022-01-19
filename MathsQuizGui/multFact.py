import tools
import random
import menus
import gui
import guizero

def mfQuestions(cat):
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text=f"{cat.title()}", size=22, color="red")
    guizero.Text(gui.app, height=2)

    guizero.Text(gui.app, text=f"Instructions: Enter all the {cat} seperated by spaces")
    guizero.Text(gui.app, height=1)
    box = guizero.Box(gui.app)
    qNum = 1
    correct = 0

    def nextQ():
        gui.clearBox(box)
        nonlocal qNum, correct
        nextQButton.text = "Next question"

        qBox = guizero.Box(box)
        guizero.Text(qBox, text=f"{qNum}) ", align="left")
        num = random.randint(1, 100)

        if cat == "multiples":
            ans = [str(x) for x in tools.multiples(num, 11)]
            guizero.Text(qBox, text=f"List the first ten multiple of {num}", align="left")
            guizero.Text(box, height=1)
            ansGet = guizero.TextBox(box, width=50)
            ansGet.text_size = 12
            ansGet.bg = "white"
            guizero.Text(box, height=1)
        elif cat == "factors":
            ans = [str(x) for x in tools.factors(num)]
            guizero.Text(qBox, text=f"List all the factors of {num}", align="left")
            guizero.Text(box, height=1)
            ansGet = guizero.TextBox(box, width=50)
            ansGet.text_size = 12
            ansGet.bg = "white"
            guizero.Text(box, height=1)

        def checkAnswer():
            nonlocal correct
            userAns = ansGet.value.split()

            if set(ans) == set(userAns):
                guizero.Text(box, height=1)
                guizero.Text(box, text="Correct, well done!")
                correct += 1
            else:
                guizero.Text(box, height=1)
                ansBox = guizero.Box(box)
                guizero.Text(ansBox, text="Incorrect! The correct answer is:", align="left")
                guizero.Text(ansBox, text=ans, align="left")
            
            guizero.Text(box, text=f"Total correct: {correct}")
        
        checkAnsButton = guizero.PushButton(box, command=checkAnswer, text="Check answer", width=buttonW)
        checkAnsButton.bg = "lightgreen"
        checkAnsButton.text_size = buttonTextSize
        qNum += 1
    
    guizero.Text(gui.app, height=1)
    nextQButton = guizero.PushButton(gui.app, command=nextQ, text="Start", width=buttonW)
    nextQButton.bg = "lawn green"
    nextQButton.text_size = buttonTextSize
    guizero.Text(gui.app, height=2)

    backBox = guizero.Box(gui.app, layout="grid")
    nMenuButton = guizero.PushButton(backBox, command=menus.numbersMenu, text="Numbers Menu",grid=[0,0], width=buttonW)
    nMenuButton.bg = "lightblue"
    nMenuButton.text_size = buttonTextSize
    guizero.Text(backBox, grid=[1,0], width=5)
    mainMenuButton = guizero.PushButton(backBox, command=menus.mainMenu, text="Main Menu",grid=[2,0], width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def mulTable():
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Multiplication Table", size=22, color="red")
    guizero.Text(gui.app, height=2)

    guizero.Picture(gui.app, image="C:/Users/Abdul/Documents/Programming/Python/Projects/MathsQuizGui/timesTable.png")

    guizero.Text(gui.app, height=2)

    mainMenuButton = guizero.PushButton(gui.app, command=menus.mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def mfInfo(cat):
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text=f"{cat.title()} of Numbers", size=22, color="red")
    guizero.Text(gui.app, height=2)

    guizero.Text(gui.app, text=f"Enter a number to show it's {cat}")
    guizero.Text(gui.app, height=1)
    numGet = guizero.TextBox(gui.app, width=6)
    numGet.text_size = 12
    numGet.bg = "white"
    guizero.Text(gui.app, height=1)
    box = guizero.Box(gui.app)

    def show():
        gui.clearBox(box)
        num = numGet.value

        try:
            num = int(num)
        except:
            guizero.Text(box, text="Please enter a whole number")
            return
        
        if num > 99999:
            guizero.Text(box, text="Please enter a lower number")
            return
        elif num < 1 and cat == "factors":
            guizero.Text(box, text="Please enter a whole number greater than zero")
            return

        if cat == "multiples":
            numList = tools.multiples(num, 13)
        else:
            numList = tools.factors(num)

        guizero.Text(box, text=numList, height=3)

    guizero.Text(gui.app, height=1)
    showButton = guizero.PushButton(gui.app, command=show, text=f"Show {cat}", width=buttonW)
    showButton.bg = "lightgreen"
    showButton.text_size = buttonTextSize

    guizero.Text(gui.app, height=2)

    mainMenuButton = guizero.PushButton(gui.app, command=menus.mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize