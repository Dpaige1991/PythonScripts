import pystray
import PIL.Image

image = PIL.Image.open("PythonImg.png")

def on_clicked(icon, item):
    if str(item) == "Say Hello":
        print("Hello World")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "Subitem 1":
        print("Sub 1")
    else:
        print("Not implemented yet!")

icon = pystray.Icon("Python", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Subitem 1", on_clicked),
        pystray.MenuItem("Subitem 2", on_clicked)
    ))
))

icon.run()