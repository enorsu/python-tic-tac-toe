import os, time
from pyautogui import alert
screen1 = ["1","2","3",
          "4","5","6",
          "7","8","9",]
def render_screen(s):
    print(s[0], s[1], s[2])
    print(s[3], s[4], s[5])
    print(s[6], s[7], s[8])

def set_pixel(scree , val, setable):
    if setable == "X":
        if scree[val - 1] == "O":
            alert(text="Yritit huijata! Menetit vuoron!")
            return "Yritit huijata! Menetit vuoron!"
        else:
             scree[val - 1] = setable
    else:
        if scree[val - 1] == "X":
            alert(text="Yritit huijata! Menetit vuoron!")
            return "Yritit huijata! Menetit vuoron!"
        else:
             scree[val - 1] = setable
   


#for i in range(9):
#    for x in range(9):
#        time.sleep(0.1)
#        os.system("clear")
#        set_pixel(screen1, i + 1, x + 1)
#        
#        render_screen(screen1)
os.system("clear")
while True:
    os.system("clear")
    render_screen(screen1)
    xinput = int(input("Player X:"))
    set_pixel(screen1, xinput, "X")
    os.system("clear")
    render_screen(screen1)
    oinput = int(input("Player O:"))
    set_pixel(screen1, oinput, "O")

