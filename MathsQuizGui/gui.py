import guizero

app = guizero.App(title="Maths Quiz", bg="beige", width=800, height=600)

def clearScreen():
    for widgets in app.children.copy():
        widgets.destroy()

def clearBox(box):
    for widgets in box.children.copy():
        widgets.destroy()