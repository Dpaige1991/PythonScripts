import time
from winotify import Notification, audio

toast = Notification(app_id="Windows Notify Script",
                     title="Message",
                     msg="Hello World",
                     duration="long",
                     icon=r"C:\Users\domin\Desktop\PythonImg.png")

toast.add_actions(label="Click Me", launch="https://www.magikid.com")

toast.show()