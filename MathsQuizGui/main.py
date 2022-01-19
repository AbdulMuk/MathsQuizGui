import menus
import gui
import guizero

guizero.Text(gui.app, height=1)

box = guizero.Box(gui.app, width="fill")
box.bg = "red4"
guizero.Text(box, height=1)
guizero.Text(box, text="Maths Quiz", size=28, color="white")
guizero.Text(box, height=1)

guizero.Text(gui.app, height=8)

mainMenuButton = guizero.PushButton(gui.app, command=menus.mainMenu, text="Main Menu")
mainMenuButton.bg = "cadetblue"
mainMenuButton.text_size = 16

guizero.Text(gui.app, height=10)

guizero.Text(gui.app, text="Created by: Abdul Mukit. © 2022", size=16, color="darkgreen")

gui.app.display()