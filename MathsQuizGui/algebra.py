import tools
import random
import menus
import gui
import guizero

def collectTerms(type, letters):

    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)
    d = random.choice(letters)

    # if any letters are the same, pick again
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = random.choice(letters)
        b = random.choice(letters)
        c = random.choice(letters)
        d = random.choice(letters)

    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)
    num3 = random.randint(-9, 9)
    num4 = random.randint(-9, 9)
    num5 = random.randint(-9, 9)
    num6 = random.randint(-9, 9)
    num7 = random.randint(-9, 9)
    num8 = random.randint(-9, 9)
    # remove 0
    num1 = tools.remove0(num1, -9, 9)
    num2 = tools.remove0(num2, -9, 9)
    num3 = tools.remove0(num3, -9, 9)
    num4 = tools.remove0(num4, -9, 9)
    num5 = tools.remove0(num5, -9, 9)
    num6 = tools.remove0(num6, -9, 9)
    num7 = tools.remove0(num7, -9, 9)
    num8 = tools.remove0(num8, -9, 9)

    # question and answer list stored as a 4 tier list
    # q and a's are stored as lists
    # each q and a is a list of terms
    # each term is a list of coefficient and term
    # will make every permutation of the answer list so users can answer 3a + 5b or 5b + 3a
    # makeListCT function will be used to turn this into meaningful question and answer expressions
    if type == "s":

        q1 = [[num1, a], [num2, b], [num3, a], [num4, b]]
        a1 = [[num1 + num3, a], [num2 + num4, b]]
        l1 = [[i, j] for i in a1 for j in a1 if (i != j)]
        l1.insert(0, q1)

        q2 = [[num1, a], [num2, ""], [num3, b], [num4, b], [num5, a], [num6, ""]]
        a2 = [[num1 + num5, a], [num3 + num4, b], [num2 + num6, ""]]
        l2 = [[i, j, k] for i in a2 for j in a2 for k in a2 if (i != j and i != k and j != k)]
        l2.insert(0, q2)

        q3 = [[num1, a], [num2, b], [num3, a], [num4, b], [num5, a], [num6, b]]
        a3 = [[num1 + num3 + num5, a], [num2 + num4 + num6, b]]
        l3 = [[i, j] for i in a3 for j in a3 if (i != j)]
        l3.insert(0, q3)

        q4 = [[num1, a], [num2, b], [num3, ""], [num4, c], [num5, a], [num6, b], [num7, ""], [num8, c]]
        a4 = [[num1 + num5, a], [num2 + num6, b], [num4 + num8, c], [num3 + num7, ""]]
        l4 = [[i, j, k, l] for i in a4 for j in a4 for k in a4 for l in a4 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l4.insert(0, q4)

        q5 = [[num1, a], [num2, a], [num3, b], [num4, c], [num5, b], [num6, c]]
        a5 = [[num1 + num2, a], [num3 + num5, b], [num4 + num6, c]]
        l5 = [[i, j, k] for i in a5 for j in a5 for k in a5 if (i != j and i != k and j != k)]
        l5.insert(0, q5)

        q6 = [[num1, a], [num2, b], [num3, d], [num4, c], [num5, d], [num6, b], [num7, a], [num8, c]]
        a6 = [[num1 + num7, a], [num2 + num6, b], [num4 + num8, c], [num3 + num5, d]]
        l6 = [[i, j, k, l] for i in a6 for j in a6 for k in a6 for l in a6 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l6.insert(0, q6)

        q7 = [[num1, a], [num2, b], [num3, a], [num4, c], [num5, b], [num6, a], [num7, c], [num8, b]]
        a7 = [[num1 + num3 + num6, a], [num2 + num5 + num8, b], [num4 + num7, c]]
        l7 = [[i, j, k] for i in a7 for j in a7 for k in a7 if (i != j and i != k and j != k)]
        l7.insert(0, q7)

        questions4dList = [l1, l2, l3, l4, l5, l6, l7]

    else:

        q1 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, a]]
        a1 = [[num1 + num3, f"{a}²"], [num2 + num4, a]]
        l1 = [[i, j] for i in a1 for j in a1 if (i != j)]
        l1.insert(0, q1)

        q2 = [[num1, f"{a}²"], [num2, ""], [num3, a], [num4, a], [num5, f"{a}²"], [num6, ""]]
        a2 = [[num1 + num5, f"{a}²"], [num3 + num4, a], [num2 + num6, ""]]
        l2 = [[i, j, k] for i in a2 for j in a2 for k in a2 if (i != j and i != k and j != k)]
        l2.insert(0, q2)

        q3 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, a], [num5, f"{a}²"], [num6, a]]
        a3 = [[num1 + num3 + num5, "a²"], [num2 + num4 + num6, "a"]]
        l3 = [[i, j] for i in a3 for j in a3 if (i != j)]
        l3.insert(0, q3)

        q4 = [[num1, a], [num2, f"{b}²"], [num3, ""], [num4, b], [num5, a], [num6, f"{b}²"], [num7, ""], [num8, b]]
        a4 = [[num2 + num6, f"{b}²"], [num1 + num5, a], [num4 + num8, b], [num3 + num7, ""]]
        l4 = [[i, j, k, l] for i in a4 for j in a4 for k in a4 for l in a4 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l4.insert(0, q4)

        q5 = [[num1, f"{a}²"], [num2, f"{a}²"], [num3, a], [num4, ""], [num5, a], [num6, ""]]
        a5 = [[num1 + num2, f"{a}²"], [num3 + num5, "x"], [num4 + num6, ""]]
        l5 = [[i, j, k] for i in a5 for j in a5 for k in a5 if (i != j and i != k and j != k)]
        l5.insert(0, q5)

        q6 = [[num1, f"{a}²"], [num2, f"{b}²"], [num3, b], [num4, a], [num5, b], [num6, f"{b}²"], [num7, f"{a}²"], [num8, a]]
        a6 = [[num1 + num7, f"{a}²"], [num2 + num6, f"{b}²"], [num4 + num8, a], [num3 + num5, b]]
        l6 = [[i, j, k, l] for i in a6 for j in a6 for k in a6 for l in a6 if (i != j and i != k and i != l and j != k and j != l and k != l)]
        l6.insert(0, q6)

        q7 = [[num1, f"{a}²"], [num2, a], [num3, f"{a}²"], [num4, ""], [num5, a], [num6, f"{a}²"], [num7, ""], [num8, a]]
        a7 = [[num1 + num3 + num6, f"{a}²"], [num2 + num5 + num8, a], [num4 + num7, ""]]
        l7 = [[i, j, k] for i in a7 for j in a7 for k in a7 if (i != j and i != k and j != k)]
        l7.insert(0, q7)

        questions4dList = [l1, l2, l3, l4, l5, l6, l7]

    # choose a random list from questions, index 0 is the question, the rest are answers
    question3dList = random.choice(questions4dList)
    question = tools.makeListCT(question3dList)
    return question

def expBracket(type, letters):

    x = random.choice(letters)
    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)
    num3 = random.randint(-9, 9)
    num4 = random.randint(-9, 9)

    # remove 0
    num1 = tools.remove0(num1, -9, 9)
    num2 = tools.remove0(num2, -9, 9)
    num3 = tools.remove0(num3, -9, 9)
    num4 = tools.remove0(num4, -9, 9)

    # question and answers as a list
    if type == "s":
        questions = [
            [f"{num1}({x} {tools.checkNum(num2)})",
            f"{tools.check1(num1)}{x} {tools.checkNum(num1 * num2)}",
            f"{num1 * num2} {tools.checkBoth(num1)}{x}"],

            [f"{num1}({tools.check1(num2)}{x} {tools.checkNum(num3)})",
            f"{tools.check1(num1 * num2)}{x} {tools.checkNum(num1 * num3)}",
            f"{num1 * num3} {tools.checkBoth(num1 * num2)}{x}"],

            [f"{num1}({num2} + {x})",
            f"{tools.check1(num1)}{x} {tools.checkNum(num1 * num2)}",
            f"{num1 * num2} {tools.checkBoth(num1)}{x}"],

            [f"{num1}({num2} - {x})",
            f"{tools.check1(num1 * -1)}{x} {tools.checkNum(num1 * num2)}",
            f"{num1 * num2} {tools.checkBoth(num1 * -1)}{x}"],

            [f"{num1}({num2} {tools.checkBoth(num3)}{x})",
            f"{tools.check1(num1 * num3)}{x} {tools.checkNum(num1 * num2)}",
            f"{num1 * num2} {tools.checkBoth(num1 * num3)}{x}"],

            [f"{x}({tools.check1(num1)}{x} {tools.checkNum(num2)})",
            f"{tools.check1(num1)}{x}² {tools.checkBoth(num2)}{x}",
            f"{tools.check1(num2)}{x} {tools.checkBoth(num1)}{x}²"],

            [f"{tools.check1(num1)}{x}({tools.check1(num2)}{x} {tools.checkNum(num3)})",
            f"{tools.check1(num1 * num2)}{x}² {tools.checkBoth(num1 * num3)}{x}",
            f"{tools.check1(num1 * num3)}{x} {tools.checkBoth(num1 * num2)}{x}²"]
        ]
    else:
        questions = [
            [f"({x} {tools.checkNum(num1)})({x} {tools.checkNum(num2)})",
            f"{x}² {tools.checkTerm([num1 + num2, f'{x}'])}{tools.checkNum(num1 * num2)}",
            f"{x}² {tools.checkNum(num1 * num2)} {tools.checkTerm([num1 + num2, f'{x}'])}",
            f"{tools.checkTerm([num1 + num2, f'{x}'])}+ {x}² {tools.checkNum(num1 * num2)}",
            f"{tools.checkTerm([num1 + num2, f'{x}'])}{tools.checkNum(num1 * num2)} + {x}²",
            f"{num1 * num2} + {x}² {tools.checkTerm([num1 + num2, f'{x}'])}",
            f"{num1 * num2} {tools.checkTerm([num1 + num2, f'{x}'])}+ {x}²"],

            [f"({num1} + {x})({num2} + {x})",
            f"{x}² {tools.checkTerm([num1 + num2, f'{x}'])}{tools.checkNum(num1 * num2)}",
            f"{x}² {tools.checkNum(num1 * num2)} {tools.checkTerm([num1 + num2, f'{x}'])}",
            f"{tools.checkTerm([num1 + num2, f'{x}'])}+ {x}² {tools.checkNum(num1 * num2)}",
            f"{tools.checkTerm([num1 + num2, f'{x}'])}{tools.checkNum(num1 * num2)} + {x}²",
            f"{num1 * num2} + {x}² {tools.checkTerm([num1 + num2, f'{x}'])}",
            f"{num1 * num2} {tools.checkTerm([num1 + num2, f'{x}'])}+ {x}²"],

            [f"({x} {tools.checkNum(num1)})²",
            f"{x}² {tools.checkBoth(2 * num1)}{x} {tools.checkNum(num1 ** 2)}",
            f"{x}² {tools.checkNum(num1 ** 2)} {tools.checkBoth(2 * num1)}{x}",
            f"{tools.check1(2 * num1)}{x} + {x}² {tools.checkNum(num1 ** 2)}",
            f"{tools.check1(2 * num1)}{x} {tools.checkNum(num1 ** 2)} + {x}²",
            f"{num1 ** 2} + {x}² {tools.checkBoth(2 * num1)}{x}",
            f"{num1 ** 2} {tools.checkBoth(2 * num1)}{x} + {x}²"],

            [f"({tools.check1(num1)}{x} {tools.checkNum(num2)})²",
            f"{tools.check1(num1 ** 2)}{x}² {tools.checkBoth(2 * num1 * num2)}{x} {tools.checkNum(num2 ** 2)}",
            f"{tools.check1(num1 ** 2)}{x}² {tools.checkNum(num2 ** 2)} {tools.checkBoth(2 * num1 * num2)}{x}",
            f"{tools.check1(2 * num1 * num2)}{x} {tools.checkBoth(num1 ** 2)}{x}² {tools.checkNum(num2 ** 2)}",
            f"{tools.check1(2 * num1 * num2)}{x} {tools.checkNum(num2 ** 2)} {tools.checkBoth(num1 ** 2)}{x}²",
            f"{num2 ** 2} {tools.checkBoth(num1 ** 2)}{x}² {tools.checkBoth(2 * num1 * num2)}{x}",
            f"{num2 ** 2} {tools.checkBoth(2 * num1 * num2)}{x} {tools.checkBoth(num1 ** 2)}{x}²"],

            [f"({tools.check1(num1)}{x} {tools.checkNum(num2)})({tools.check1(num3)}{x} {tools.checkNum(num4)})",
            f"{tools.check1(num1 * num3)}{x}² {tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{tools.checkNum(num2 * num4)}",
            f"{tools.check1(num1 * num3)}{x}² {tools.checkNum(num2 * num4)} {tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}",
            f"{tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{tools.checkBoth(num1 * num3)}{x}² {tools.checkNum(num2 * num4)}",
            f"{tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{tools.checkNum(num2 * num4)} {tools.checkBoth(num1 * num3)}{x}²",
            f"{num2 * num4} {tools.checkBoth(num1 * num3)}{x}² {tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}",
            f"{num2 * num4} {tools.checkTerm([num1 * num4 + num2 * num3, f'{x}'])}{tools.checkBoth(num1 * num3)}{x}²"]
        ]
    # choose a random list from questions, index 0 is the question, the rest are answers
    question = random.choice(questions)
    return question

def fctBracket(type, letters):

    x = random.choice(letters)
    num1 = random.randint(-9, 9)
    num2 = random.randint(-9, 9)

    # remove 0
    num2 = tools.remove0(num2, -9, 9)

    # remove 0, 1 and -1
    while num1 == 0 or num1 == 1 or num1 == -1:
        num1 = random.randint(-9, 9)

    # question and answers as a list
    if type == "s":
        questions = [
            [f"{num1}{x} {tools.checkNum(num1 * num2)}",
            f"{num1}({x} {tools.checkNum(num2)})",
            f"{num1}({num2} + {x})",
            f"{num1 * -1}(-{x} {tools.checkNum(num2 * -1)})",
            f"{num1 * -1}({num2 * -1} - {x})"],

            [f"{num1 * 2}{x} {tools.checkNum(num1 * 3)}",
            f"{num1}(2{x} + 3)",
            f"{num1}(3 + 2{x})",
            f"{num1 * -1}(-2{x} - 3)",
            f"{num1 * -1}(-3 - 2{x})"],

            [f"{num1 * 3}{x} {tools.checkNum(num1 * 2)}",
            f"{num1}(3{x} + 2)",
            f"{num1}(2 + 3{x})",
            f"{num1 * -1}(-3{x} - 2)",
            f"{num1 * -1}(-2 - 3{x})"],

            [f"{num1 * 3}{x} {tools.checkNum(num1 * 4)}",
            f"{num1}(3{x} + 4)",
            f"{num1}(4 + 3{x})",
            f"{num1 * -1}(-3{x} - 4)",
            f"{num1 * -1}(-4 - 3{x})"],

            [f"{num1 * 3}{x} {tools.checkNum(num1 * 5)}",
            f"{num1}(3{x} + 5)",
            f"{num1}(5 + 3{x})",
            f"{num1 * -1}(-3{x} - 5)",
            f"{num1 * -1}(-5 - 3{x})"],

            [f"{num1 * num2}{x} {tools.checkNum(num1)}",
            f"{num1}({tools.check1(num2)}{x} + 1)",
            f"{num1}(1 {tools.checkBoth(num2)}{x})",
            f"{num1 * -1}({tools.check1(num2 * -1)}{x} - 1)",
            f"{num1 * -1}(-1 {tools.checkBoth(num2 * -1)}{x})"],

            [f"{num1 * num2}{x} {tools.checkNum(num1 * 2)}",
            f"{num1}({tools.check1(num2)}{x} + 2)",
            f"{num1}(2 {tools.checkBoth(num2)}{x})",
            f"{num1 * -1}({tools.check1(num2 * -1)}{x} - 2)",
            f"{num1 * -1}(-2 {tools.checkBoth(num2 * -1)}{x})"],

            [f"{num1 * num2}{x} {tools.checkNum(num1 * 5)}",
            f"{num1}({tools.check1(num2)}{x} + 5)",
            f"{num1}(5 {tools.checkBoth(num2)}{x})",
            f"{num1 * -1}({tools.check1(num2 * -1)}{x} - 5)",
            f"{num1 * -1}(-5 {tools.checkBoth(num2 * -1)}{x})"],

            [f"{num1}{x}² + {x}",
            f"{x}({num1}{x} + 1)",
            f"{x}(1 {tools.checkNum(num1)}{x})",
            f"-{x}({num1 * -1}{x} - 1)",
            f"-{x}(-1 {tools.checkNum(num1 * -1)}{x})"],

            [f"{num1}{x}² - {x}",
            f"{x}({num1}{x} - 1)",
            f"{x}(-1 {tools.checkNum(num1)}{x})",
            f"-{x}({num1 * -1}{x} + 1)",
            f"-{x}(1 {tools.checkNum(num1 * -1)}{x})"],

            [f"{x}² {tools.checkNum(num1)}{x}",
            f"{x}({x} {tools.checkNum(num1)})",
            f"{x}({num1} + {x})",
            f"-{x}(-{x} {tools.checkNum(num1 * -1)})",
            f"-{x}({num1 * -1} - {x})"],

            [f"{num1}{x}² {tools.checkNum(num1 * num2)}{x}",
            f"{num1}{x}({x} {tools.checkNum(num2)})",
            f"{num1}{x}({num2} + {x})",
            f"{num1 * -1}{x}(-{x} {tools.checkNum(num2 * -1)})",
            f"{num1 * -1}{x}({num2 * -1} - {x})"],
        ]
    else:
        questions = [
            [f"{x}² {tools.checkTerm([num1 + num2, f'{x}'])}{tools.checkNum(num1 * num2)}",
            f"({x} {tools.checkNum(num1)})({x} {tools.checkNum(num2)})",
            f"({num1} + {x})({x} {tools.checkNum(num2)})",
            f"({x} {tools.checkNum(num1)})({num2} + {x})",
            f"({num1} + {x})({num2} + {x})",
            f"({x} {tools.checkNum(num2)})({x} {tools.checkNum(num1)})",
            f"({num2} + {x})({x} {tools.checkNum(num1)})",
            f"({x} {tools.checkNum(num2)})({num1} + {x})",
            f"({num2} + {x})({num1} + {x})"],

            [f"{x}² {tools.checkNum(2 * num1)}{x} {tools.checkNum(num1 ** 2)}",
            f"({x} {tools.checkNum(num1)})²",
            f"({num1} + {x})²",
            f"({x} {tools.checkNum(num1)})({x} {tools.checkNum(num1)})",
            f"({num1} + {x})({x} {tools.checkNum(num1)})",
            f"({x} {tools.checkNum(num1)})({num1} + {x})",
            f"({num1} + {x})({num1} + {x})"]
        ]
    # choose a random list from questions, index 0 is the question, the rest are answers
    question = random.choice(questions)
    return question

def algebra(cat, type):
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Algebra", size=22, color="red")
    guizero.Text(gui.app, height=1)
    
    insBoxCon = guizero.Box(gui.app, width="fill")
    insBox = guizero.Box(insBoxCon, layout="grid", align="right")

    infoBox = guizero.Box(insBox, grid=[0,0], width="fill")
    infoBox1 = guizero.Box(infoBox, layout="grid", width="fill")
    guizero.Text(infoBox1, text="If a coefficient = 1 then only write the variable", grid=[0,0])
    infoBox2 = guizero.Box(infoBox, layout="grid", width="fill")
    guizero.Text(infoBox2, text="To write squared, use ^2 or the ² button", grid=[0,0])
    infoBox3 = guizero.Box(infoBox, layout="grid", width="fill")
    guizero.Text(infoBox3, text="eg. 3x^2 - x + 6", grid=[0,0])
    
    def showIns():
        if infoBox.visible:
            infoBox.visible = False
            insButton.text = "Show instructions"
        else:
            infoBox.visible = True
            insButton.text = "Hide instructions"

    guizero.Text(insBox, grid=[1,0], width=25)
    insButton = guizero.PushButton(insBox, command=showIns, text="Hide instructions", grid=[2,0])
    insButton.bg = "lightgrey"
    insButton.text_size = 9
    guizero.Text(insBox, grid=[3,0], width=2)

    box = guizero.Box(gui.app)
    qNum = 1
    correct = 0
    letters = ["a", "b", "c", "d", "e", "n", "m", "p", "q", "r", "t", "x", "y", "z"]

    def nextQ():
        gui.clearBox(box)
        nonlocal qNum, correct
        nextQButton.text = "Next question"

        if cat == "c":
            question = collectTerms(type, letters)
        elif cat == "e":
            question = expBracket(type, letters)
        else:
            question = fctBracket(type, letters)

        qBox = guizero.Box(box)
        guizero.Text(qBox, text=f"{qNum}) ", align="left")
        guizero.Text(qBox, text=f"{question[0]} =", align="left")
        guizero.Text(box, height=1)

        getAnsBox = guizero.Box(box, layout="grid")
        ansGet = guizero.TextBox(getAnsBox, grid=[0,0], width=30)
        ansGet.text_size = 12
        ansGet.bg = "white"
        guizero.Text(getAnsBox, grid=[1,0], width=2)

        square = lambda: ansGet.append("²")

        squareButton = guizero.PushButton(getAnsBox, command=square, text="²", grid=[2,0], width=5, padx=0, pady=0)
        squareButton.text_size = 12
        squareButton.bg = "yellow"
        guizero.Text(box, height=1)

        def checkAnswer():
            nonlocal correct
            checkAnsButton.visible = False
            userAns = ansGet.value
            msg = f"Incorrect! The correct answer is: {question[1]}"
            
            # format userAns
            userAns = userAns.replace(" ", "")
            userAns = tools.replaceCarr(userAns)
            userAns = userAns.lower()
            userAns = userAns.lstrip("+")

            # check if userAns matches any of the answers
            checkCorrect = False
            question.pop(0) # remove question leaving only answers

            for ans in question:
                ans = ans.replace(" ", "")
                ans = ans.lstrip("+")
                checkCorrect = checkCorrect or userAns == ans

            if checkCorrect:
                guizero.Text(box, height=1)
                guizero.Text(box, text="Correct, well done!")
                correct += 1
            else:
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
    aMenuButton = guizero.PushButton(backBox, command=menus.algebraMenu, text="Algebra Menu", grid=[0,0], width=buttonW)
    aMenuButton.bg = "lightblue"
    aMenuButton.text_size = buttonTextSize
    guizero.Text(backBox, grid=[1,0], width=5)
    mainMenuButton = guizero.PushButton(backBox, command=menus.mainMenu, text="Main Menu", grid=[2,0], width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize
