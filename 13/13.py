from win10toast import ToastNotifier
import subprocess
import webbrowser
import time
import random
import threading
toaster=ToastNotifier()

message=[
    "poruka1",
    "poruka2",
    "poruka3"
]

def msg():

    while True:
        toaster.show_toast("Title",random.choice(message), duration=2)
        time.sleep(3)


thread=threading.Thread(target=msg)
thread.start()
subprocess.Popen("C:/WINDOWS/system32/notepad.exe")
webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe").open("https://google.com")
