import mouse;
import keyboard
from datetime import datetime 
from time import sleep
import os



####  KEYBOARD  PART ###
        # while True:
        #     keyboard.wait('space')
        #     print('space was pressed! Waiting on it again...')

        # # or this
        # keyboard.add_hotkey('space', lambda: print('space was pressed!'))
        # keyboard.wait()


def printLine(title):
    print(f'================={title}=======================')

def eventLog(e):
    global eventsArr
    eventsArr.append(e)
    if(len(eventsArr) >= 10):
        eventsArr.pop(0)

def keyboardHandler(event):
    eventLog(event)


def mouseHandler(event):
    if type(event) == mouse._mouse_event.ButtonEvent:
        temp = str(event)
        if(temp.find('?')) < 0:
            parseMouseEvent(event)

def parseMouseEvent(event):
    eventLog(event)
    btn = event.button
    for hook in activeHooks:
        if btn == hook['key']:
            if event.event_type == 'down':
                hook['macroFn']()


# mouse.move(x, y,
#   absolute=False,
#   duration=0,
#   steps_per_second=120.0)


def mvMouse(mh:mouse, x, y, speed):
    mh.move(x,y,False,int(100/speed))

def macroWall():
    global mh;

    eventLog("macroWall")
    # press wallbtn
    # moveDn 2000
    # wait 10 ms
    # moveUp 100
    # wait 50ms
    # press leftMouse
    # wait 50ms
    # mouseMv 1920
    # wait 50ms
    # release leftMouse
    # press ExitBuildMenu



def printLastEvents():
    global eventsArr
    for ev in eventsArr:
        print(str(ev))


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printTime():
    timeNow = datetime.now()
    timeNowStr = timeNow.strftime("%H:%M:%S")
    print(timeNowStr)

def printHooks():
    global activeHooks
    for hook in activeHooks:
        for item in hook:
            print(f'{str(item)}')

def printHndl():
    printLine("PIOTYR HAXIOR")
    printTime()
    printLine("Aktywne macro")
    printHooks()
    printLine("Ostatnie eventy")
    printLastEvents()

FRAMETIME = float(1/30)
eventsArr = []
activeHooks = []

mouse_x1 = {
    'type'  :   'mouse', 
    'key'   :   'x',
    'macroFn' :   macroWall
}
keyboard.add_hotkey('x', macroWall)

arrMacros=[]
arrMacros.append(macroWall)

activeHooks.append(mouse_x1)

if __name__ == "__main__":
    global mh, kbh
    mh = mouse.hook(mouseHandler)
    kbh = keyboard.on_press(keyboardHandler)

    while True:
        printHndl()

        sleep(FRAMETIME)
        cls()

    
    kb.set_normal_term()





    