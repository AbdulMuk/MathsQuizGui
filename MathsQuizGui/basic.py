import tools
import random
import menus
import gui
import guizero

def generalQuiz():
    # question and answer pairs as a list, index 0 is the question and index 1 the answer
    generalQs = [
        ["How many degrees are there in a straight line", "180"],
        ["How many degrees are there in a right angle", "90"],
        ["How many degrees are there in a complete circle", "360"],
        ["What is the sum of the angles inside a triangle", "180"],
        ["What is the sum of the angles inside a square", "360"],
        ["What is the sum of the angles inside a pentagon", "540"],
        ["What is the sum of the exterior angles of any polygon", "360"],
        ["How many centimeters are there in a meter", "100"],
        ["How many millimeters are there in a meter", "1,000"],
        ["How many millimeters are there in a centimeter", "10"],
        ["How many meters are there in a kilometer", "1,000"],
        ["How many milligrams are there in a gram", "1,000"],
        ["How many milligrams are there in a kilogram", "1,000,000"],
        ["How many micrograms are there in a gram", "1,000,000"],
        ["How many centilitres are there in a litre", "100"],
        ["How many millilitres are there in a centilitre", "10"],
        ["How many inches are there in a foot", "12"],
        ["How many feet are there in a yard", "3"],
        ["What is the longest side in a right angle triangle called", "hypotenuse"],
        ["What is the side next to the angle in a right angle triangle called", "adjacent"],
        ["What is the side opposite the angle in a right angle triangle called", "opposite"],
        ["What is a regular triangle called (all sides the same, all angles the same)", "equilateral triangle"],
        ["What is a triangle with 2 sides and 2 angles the same called", "isosceles triangle"],
        ["What is a quadrilateral with 2 pairs of parallel sides called", "parallelogram"],
        ["What is a regular quadrilateral called (all sides the same, all angles the same)", "square"],
        ["How many sides does a triangle have", "3"],
        ["How many sides does a quadrilateral have", "4"],
        ["How many sides does a pentagon have", "5"],
        ["How many sides does a hexagon have", "6"],
        ["What do you call a shape with 10 sides", "decagon"],
        ["What do you call a shape with 8 sides", "octagon"],
        ["What do you call the distance around a shape", "perimeter"],
        ["What do you call the distance around a cirlce", "circumference"],
        ["What is the line from the center of a cirlce to the edge called", "radius"],
        ["What is the line from one side of a cirlce to the other side passing through the centre called", "diameter"],
        ["Speed = distance divided by what", "time"],
        ["Circumference = 2 times pi times what", "radius"]
    ]
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="General Quiz", size=22, color="red")
    guizero.Text(gui.app, height=2)

    guizero.Text(gui.app, text="Instructions: Type the answers without any units. Commas and spaces will be ignored.")
    guizero.Text(gui.app, height=1)
    box = guizero.Box(gui.app)
    qNum = 1
    correct = 0

    def nextQ():
        gui.clearBox(box)
        nonlocal qNum, correct
        nextQButton.text = "Next question"
        question = random.choice(generalQs)

        qBox = guizero.Box(box)
        guizero.Text(qBox, text=f"{qNum}) ", align="left")
        guizero.Text(qBox, text=f"{question[0]}?", align="left")
        guizero.Text(box, height=1)
        ansGet = guizero.TextBox(box, width=20)
        ansGet.text_size = 12
        ansGet.bg = "white"
        guizero.Text(box, height=1)

        def checkAnswer():
            nonlocal correct
            checkAnsButton.visible = False
            userAns = ansGet.value
            msg = f"Incorrect! The correct answer is: {question[1]}"
            msg, correct = tools.checkAns(question[1], userAns, msg, correct)
            guizero.Text(box, height=1)
            guizero.Text(box, text=msg)
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

    mainMenuButton = guizero.PushButton(gui.app, command=menus.mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def arithmetic(a, b, operator):
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12
    
    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Arithmetic", size=22, color="red")
    guizero.Text(gui.app, height=2)

    box = guizero.Box(gui.app)
    qNum = 1
    correct = 0

    def generateQA():
        num1 = random.randint(a, b)
        num2 = random.randint(a, b)
        op = operator # don't want to reassign operator, for mix to work

        if operator == "mix": op = random.choice(["+", "-", "x", "÷"])

        if op == "÷":
            num1 = tools.remove0(num1, a, b)
            num2 = tools.remove0(num2, a, b)
            num3 = num1 * num2 # num3 and num4 are introduced to avoid decimal division results
            num4 = num2
            ans = num1
        else:
            num3 = num1
            num4 = num2
            if op == "+":
                ans = num3 + num4
            elif op == "-":
                ans = num3 - num4
            elif op == "x":
                ans = num3 * num4

        return [num3, num4, op, str(ans)]

    def nextQ():
        gui.clearBox(box)
        nonlocal qNum, correct
        nextQButton.text = "Next question"
        num3, num4, op, ans = generateQA()

        qBox = guizero.Box(box)
        guizero.Text(qBox, text=f"{qNum}) ", align="left")
        guizero.Text(qBox, text=f"{num3} {op} {num4} =", align="left")
        guizero.Text(box, height=1)
        ansGet = guizero.TextBox(box)
        ansGet.text_size = 12
        ansGet.bg = "white"
        guizero.Text(box, height=1)

        def checkAnswer():
            nonlocal correct
            checkAnsButton.visible = False
            userAns = ansGet.value
            msg = f"Incorrect! {num3} {op} {num4} = {ans}"
            msg, correct = tools.checkAns(ans, userAns, msg, correct)
            guizero.Text(box, height=1)
            guizero.Text(box, text=msg)
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
    aMenuButton = guizero.PushButton(backBox, command=menus.arithmeticMenu, text="Arithmetic Menu", grid=[0,0], width=buttonW)
    aMenuButton.bg = "lightblue"
    aMenuButton.text_size = buttonTextSize
    guizero.Text(backBox, grid=[1,0], width=5)
    mainMenuButton = guizero.PushButton(backBox, command=menus.mainMenu, text="Main Menu", grid=[2,0], width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize
