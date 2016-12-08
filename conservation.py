#! C:\Python34\python.exe
import sys
import pyautogui as pyau
import time
x1=(1226, 843) # arrow
x2=(1282, 718) # energy manager button
x3=(1045, 267) # toggle menu
x4=(1468, 250) # settings
off_loc=(1466, 294) # conserve OFF
on_loc=(1494, 294) # conserve ON
close = (1062, 228)
def toggle_on():
    global x1,x2,x3,x4,on_loc, close
    locations = [x1,x2,x3,x4,on_loc, close]
    for loc in locations:
        pyau.moveTo(x=loc[0], y=loc[1], duration=0.3)
        pyau.click()

def toggle_off():
    global x1,x2,x3,x4,off_loc, close
    locations = [x1,x2,x3,x4,off_loc, close]
    for loc in locations:
        pyau.moveTo(x=loc[0], y=loc[1], duration=0.3)
        pyau.click()

print(sys.argv)
if len(sys.argv) != 2:
    print("Error: Only recognize on and off as keywords")
else:
    # Turn on or off
    #print(sys.argv)
    
    on = sys.argv[1].lower() == 'on'
    off = sys.argv[1].lower() == 'off'
    if on:
        toggle_on()
    elif off:
        toggle_off()
    else:
        print("Error: Only recognize on and off as keywords")
    
    
input("Press Enter to exit")

