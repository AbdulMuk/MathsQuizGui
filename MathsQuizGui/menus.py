import basic
import multFact
import algebra
import gui
import guizero

def arithmeticMenu():
    gui.clearScreen()
    buttonW = 16
    buttonTextSize = 12
    eButtonBg = "lightblue"
    mButtonBg = "goldenrod"
    hButtonBg = "lightgreen"
    buttonGap = 2

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Arithmetic Menu", size=22, color="red")
    guizero.Text(gui.app, height=1)

    boxCat = guizero.Box(gui.app, layout="grid", width="fill", height=30)
    guizero.Text(boxCat, grid=[0,0], width=17)
    guizero.Text(boxCat, text="Easy 0 to 10", grid=[1,0], size=13, color="blue")
    guizero.Text(boxCat, grid=[2,0], width=8)
    guizero.Text(boxCat, text="Medium 0 to 100", grid=[3,0], size=13, color="brown")
    guizero.Text(boxCat, grid=[4,0], width=7)
    guizero.Text(boxCat, text="Hard -100 to 100", grid=[5,0], size=13, color="green")

    box = guizero.Box(gui.app)

    box1 = guizero.Box(box, layout="grid")
    aeButton = guizero.PushButton(box1, command=basic.arithmetic, args=[0, 10, "+"], text="Addition", grid=[0,0], width=buttonW)
    aeButton.bg = eButtonBg
    aeButton.text_size = buttonTextSize
    guizero.Text(box1, grid=[1,0], width=buttonGap)
    amButton = guizero.PushButton(box1, command=basic.arithmetic, args=[0, 100, "+"], text="Addition", grid=[2,0], width=buttonW)
    amButton.bg = mButtonBg
    amButton.text_size = buttonTextSize
    guizero.Text(box1, grid=[3,0], width=buttonGap)
    ahButton = guizero.PushButton(box1, command=basic.arithmetic, args=[-100, 100, "+"], text="Addition", grid=[4,0], width=buttonW)
    ahButton.bg = hButtonBg
    ahButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box2 = guizero.Box(box, layout="grid")
    seButton = guizero.PushButton(box2, command=basic.arithmetic, args=[0, 10, "-"], text="Subtraction", grid=[0,0], width=buttonW)
    seButton.bg = eButtonBg
    seButton.text_size = buttonTextSize
    guizero.Text(box2, grid=[1,0], width=buttonGap)
    smButton = guizero.PushButton(box2, command=basic.arithmetic, args=[0, 100, "-"], text="Subtraction", grid=[2,0], width=buttonW)
    smButton.bg = mButtonBg
    smButton.text_size = buttonTextSize
    guizero.Text(box2, grid=[3,0], width=buttonGap)
    shButton = guizero.PushButton(box2, command=basic.arithmetic, args=[-100, 100, "-"], text="Subtraction", grid=[4,0], width=buttonW)
    shButton.bg = hButtonBg
    shButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box3 = guizero.Box(box, layout="grid")
    meButton = guizero.PushButton(box3, command=basic.arithmetic, args=[0, 10, "x"], text="Multiplication", grid=[0,0], width=buttonW)
    meButton.bg = eButtonBg
    meButton.text_size = buttonTextSize
    guizero.Text(box3, grid=[1,0], width=buttonGap)
    mmButton = guizero.PushButton(box3, command=basic.arithmetic, args=[0, 100, "x"], text="Multiplication", grid=[2,0], width=buttonW)
    mmButton.bg = mButtonBg
    mmButton.text_size = buttonTextSize
    guizero.Text(box3, grid=[3,0], width=buttonGap)
    mhButton = guizero.PushButton(box3, command=basic.arithmetic, args=[-100, 100, "x"], text="Multiplication", grid=[4,0], width=buttonW)
    mhButton.bg = hButtonBg
    mhButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box4 = guizero.Box(box, layout="grid")
    deButton = guizero.PushButton(box4, command=basic.arithmetic, args=[0, 10, "÷"], text="Division", grid=[0,0], width=buttonW)
    deButton.bg = eButtonBg
    deButton.text_size = buttonTextSize
    guizero.Text(box4, grid=[1,0], width=buttonGap)
    dmButton = guizero.PushButton(box4, command=basic.arithmetic, args=[1, 100, "÷"], text="Division", grid=[2,0], width=buttonW)
    dmButton.bg = mButtonBg
    dmButton.text_size = buttonTextSize
    guizero.Text(box4, grid=[3,0], width=buttonGap)
    dhButton = guizero.PushButton(box4, command=basic.arithmetic, args=[-100, 100, "÷"], text="Division", grid=[4,0], width=buttonW)
    dhButton.bg = hButtonBg
    dhButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box5 = guizero.Box(box, layout="grid")
    mixeButton = guizero.PushButton(box5, command=basic.arithmetic, args=[0, 10, "mix"], text="Mix", grid=[0,0], width=buttonW)
    mixeButton.bg = eButtonBg
    mixeButton.text_size = buttonTextSize
    guizero.Text(box5, grid=[1,0], width=buttonGap)
    mixmButton = guizero.PushButton(box5, command=basic.arithmetic, args=[0, 100, "mix"], text="Mix", grid=[2,0], width=buttonW)
    mixmButton.bg = mButtonBg
    mixmButton.text_size = buttonTextSize
    guizero.Text(box5, grid=[3,0], width=buttonGap)
    mixhButton = guizero.PushButton(box5, command=basic.arithmetic, args=[-100, 100, "mix"], text="Mix", grid=[4,0], width=buttonW)
    mixhButton.bg = hButtonBg
    mixhButton.text_size = buttonTextSize

    guizero.Text(gui.app, height=1)

    mainMenuButton = guizero.PushButton(gui.app, command=mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def numbersMenu():
    gui.clearScreen()
    buttonW = 20
    buttonTextSize = 14
    buttonBg = "lightblue"
    buttonGap = 2

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Numbers Menu", size=22, color="red")
    guizero.Text(gui.app, height=3)

    mButton = guizero.PushButton(gui.app, command=multFact.mfQuestions, args=["multiples"], text="Multiples", width=buttonW)
    mButton.bg = buttonBg
    mButton.text_size = buttonTextSize

    guizero.Text(gui.app, height=1)

    fButton = guizero.PushButton(gui.app, command=multFact.mfQuestions, args=["factors"], text="Factors", width=buttonW)
    fButton.bg = buttonBg
    fButton.text_size = buttonTextSize

    guizero.Text(gui.app, height=2)

    mainMenuButton = guizero.PushButton(gui.app, command=mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def algebraMenu():
    gui.clearScreen()
    buttonW = 20
    buttonTextSize = 14
    lButtonBg = "lightblue"
    qButtonBg = "lightgreen"
    buttonGap = 2

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Algebra Menu", size=22, color="red")
    guizero.Text(gui.app, height=3)

    boxCat = guizero.Box(gui.app, layout="grid", width="fill")
    guizero.Text(boxCat, grid=[0,0], width=21)
    guizero.Text(boxCat, text="Linear", grid=[1,0], size=18, color="blue")
    guizero.Text(boxCat, grid=[2,0], width=12)
    guizero.Text(boxCat, text="Quadratic", grid=[3,0], size=18, color="brown")
    guizero.Text(boxCat, grid=[0,1], width=11)
    guizero.Text(boxCat, text="(Single brackets)", grid=[1,1], size=14, color="blue")
    guizero.Text(boxCat, grid=[2,1], width=8)
    guizero.Text(boxCat, text="(Double brackets)", grid=[3,1], size=14, color="brown")

    guizero.Text(gui.app, height=1)

    box = guizero.Box(gui.app)

    box1 = guizero.Box(box, layout="grid")
    ctlButton = guizero.PushButton(box1, command=algebra.algebra, args=["c", "s"], text="Collecting terms", grid=[0,0], width=buttonW)
    ctlButton.bg = lButtonBg
    ctlButton.text_size = buttonTextSize
    guizero.Text(box1, grid=[1,0], width=buttonGap)
    ctqButton = guizero.PushButton(box1, command=algebra.algebra, args=["c", "q"], text="Collecting terms", grid=[2,0], width=buttonW)
    ctqButton.bg = qButtonBg
    ctqButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box2 = guizero.Box(box, layout="grid")
    eblButton = guizero.PushButton(box2, command=algebra.algebra, args=["e", "s"], text="Expanding brackets", grid=[0,0], width=buttonW)
    eblButton.bg = lButtonBg
    eblButton.text_size = buttonTextSize
    guizero.Text(box2, grid=[1,0], width=buttonGap)
    ebqButton = guizero.PushButton(box2, command=algebra.algebra, args=["e", "q"], text="Expanding brackets", grid=[2,0], width=buttonW)
    ebqButton.bg = qButtonBg
    ebqButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box3 = guizero.Box(box, layout="grid")
    flButton = guizero.PushButton(box3, command=algebra.algebra, args=["f", "s"], text="Factorising", grid=[0,0], width=buttonW)
    flButton.bg = lButtonBg
    flButton.text_size = buttonTextSize
    guizero.Text(box3, grid=[1,0], width=buttonGap)
    fqButton = guizero.PushButton(box3, command=algebra.algebra, args=["f", "q"], text="Factorising", grid=[2,0], width=buttonW)
    fqButton.bg = qButtonBg
    fqButton.text_size = buttonTextSize

    guizero.Text(gui.app, height=2)

    mainMenuButton = guizero.PushButton(gui.app, command=mainMenu, text="Main Menu", width=buttonW)
    mainMenuButton.bg = "cadetblue"
    mainMenuButton.text_size = buttonTextSize

def mainMenu():
    gui.clearScreen()
    buttonW = 20
    buttonTextSize = 14
    qButtonBg = "lightblue"
    iButtonBg = "lightgreen"
    buttonGap = 2

    guizero.Text(gui.app, height=1)
    guizero.Text(gui.app, text="Main Menu", size=22, color="red")
    guizero.Text(gui.app, height=3)

    boxCat = guizero.Box(gui.app, layout="grid", width="fill")
    guizero.Text(boxCat, grid=[0,0], width=23)
    guizero.Text(boxCat, text="Questions", grid=[1,0], size=18, color="blue")
    guizero.Text(boxCat, grid=[2,0], width=15)
    guizero.Text(boxCat, text="Information", grid=[3,0], size=18, color="brown")

    guizero.Text(gui.app, height=1)

    box = guizero.Box(gui.app)

    box1 = guizero.Box(box, layout="grid")
    gqButton = guizero.PushButton(box1, command=basic.generalQuiz, text="General quiz", grid=[0,0], width=buttonW)
    gqButton.bg = qButtonBg
    gqButton.text_size = buttonTextSize
    guizero.Text(box1, grid=[1,0], width=buttonGap)
    mtButton = guizero.PushButton(box1, command=multFact.mulTable, text="Multiplication table", grid=[2,0], width=buttonW)
    mtButton.bg = iButtonBg
    mtButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box2 = guizero.Box(box, layout="grid")
    aoButton = guizero.PushButton(box2, command=arithmeticMenu, text="Arithmetic operations", grid=[0,0], width=buttonW)
    aoButton.bg = qButtonBg
    aoButton.text_size = buttonTextSize
    guizero.Text(box2, grid=[1,0], width=buttonGap)
    mnButton = guizero.PushButton(box2, command=multFact.mfInfo, args=["multiples"], text="Multiples of numbers", grid=[2,0], width=buttonW)
    mnButton.bg = iButtonBg
    mnButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box3 = guizero.Box(box, layout="grid")
    nButton = guizero.PushButton(box3, command=numbersMenu, text="Numbers", grid=[0,0], width=buttonW)
    nButton.bg = qButtonBg
    nButton.text_size = buttonTextSize
    guizero.Text(box3, grid=[1,0], width=buttonGap)
    fnButton = guizero.PushButton(box3, command=multFact.mfInfo, args=["factors"], text="Factors of numbers", grid=[2,0], width=buttonW)
    fnButton.bg = iButtonBg
    fnButton.text_size = buttonTextSize

    guizero.Text(box, height=1)

    box4 = guizero.Box(box, align="left")
    aButton = guizero.PushButton(box4, command=algebraMenu, text="Algebra", width=buttonW)
    aButton.bg = qButtonBg
    aButton.text_size = buttonTextSize
    aButton.align = "left"