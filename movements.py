#!/usr/local/bin/python3


#11/8/21 Kyle Tennison

#import mouse
from datetime import datetime
import time

import keyboard
import mouse
#from pynput.keyboard import Key as KeyboardKey, Controller as KeyboardController
#keyboard = KeyboardController()
#walk, run, stopwalk, stepW,stepA,stepS,stepD,jump, lookR10, lookL10, stop, eat, mine10, run, stopmine, place, hit, hotbar

commands = {
    #command    : isVariable
    'walk'      : True,
    'run'       : True,
    'stopwalk'  : False,
    'stepW'     : False,
    'stepA'     : False,
    'stepS'     : False,
    'stepD'     : False,
    'jump'      : False,
    'lookR'     : True,
    'lookL'     : True,
    'stop'      : False,
    'eat'       : False,
    'mine'      : True,
    'stopmine'  : False,
    'place'     : False,
    'hit'       : False,
    'hotbar'    : True
}
"""
class Keyboard:

    def __init__(self):
        self.keyspressed = []

    def release(self, key):
        print(f"Released {key} key")
        try:
            self.keyspressed.remove(key)
        except ValueError:
            pass

    def press(self, key):
        print(f"Pressed {key} key")
        self.keyspressed.append(key)

class Mouse:

    def move(x, y, absolute=False, duration=0):
        print(f"moving mouse x{x} and y{y}")

    class click:
        def right():
            print("right clicked")
        def left():
            print("left clicked")

    class release:
        def right():
            print("right mouse released")
        def left():
            print("left mouse released")



mouse = Mouse()
"""
class Action:

    def __init__(self):
        self.timed = False
        self.timer = int()
        self.start = datetime
        self.action = False

    def reset(self):
        self.timed = False
        self.timer = 0
        self.start = datetime
        self.action = False

walkAction = Action()
runAction = Action()
mineAction = Action()
"""
class Key:
    shift = "shift"
    space = "space"

keyboard = Keyboard()
"""
class Step:

    """
    Step.left() - Step Left - 1 param - Time
    Step.right() - Step Right - 1 param - Time
    Step.forward() - Step Forward - 1 param - Time
    Step.backward() - Step Backward - 1 param - Time
    """

    def __init__(self, length=1):
        self.length = length

    def left(self):
        keyboard.press("a")
        time.sleep(self.length)
        keyboard.release("a")

    def right(self):
        keyboard.press("d")
        time.sleep(self.length)
        keyboard.release("d")

    def forward(self):
        keyboard.press("w")
        time.sleep(self.length)
        keyboard.release("w")

    def backward(self):
        keyboard.press("s")
        time.sleep(self.length)
        keyboard.release("s")

step = Step(0.1)

def process(input):

    try:
        if not commands[input]:
            return [input]
    except KeyError:
        print("command not static", input)


    if 'walk' in input:
        return ['walk', input.split('walk')[1]]
    elif 'run' in input:
        return ['run', input.split('run')[1]]
    elif 'lookR' in input:
        return ['lookR', input.split('lookR')[1]]
    elif 'lookL' in input:
        return ['lookL', input.split('lookL')[1]]
    elif 'lookU' in input:
        return ['lookU', input.split('lookU')[1]]
    elif 'lookD' in input:
        return ['lookD', input.split('lookD')[1]]
    elif 'mine' in input:
        return ['mine', input.split('mine')[1]]
    elif 'hotbar' in input:
        return ['hotbar', input.split('hotbar')[1]]

    else:
        print("error unkown command. command:", input)

def walk(time):
    print("walk start")
    if time == "inf":
        keyboard.press('w')
        walkAction.timed = False
        walkAction.action = True
    elif int(time) < 1:
        return "You can not use negative times"
    else:
        keyboard.press('w')
        walkAction.timed = True
        walkAction.action = True
        walkAction.start = datetime.now()
        walkAction.timer = int(time)

def run(time):
    print("run start")
    if time == "inf":
        keyboard.press('w')
        keyboard.press('shift')
        walkAction.timed = False
        walkAction.action = True
    elif int(time) < 1:
        return "You can not use negative times"
    else:
        keyboard.press('w')
        keyboard.press('shift')
        walkAction.timed = True
        walkAction.action = True
        walkAction.start = datetime.now()
        walkAction.timer = int(time)

def stopwalk():
    print("stopwalk")
    keyboard.release('w')
    keyboard.release('shift')
    walkAction.reset()
    runAction.reset()

def jump():
    print("jump")
    keyboard.press(' ')
    time.sleep(0.1)
    keyboard.release(' ')

def stop():
    print("stop")
    stopwalk()
    stopkeys = ['a', 's', 'd', 'w', 'space', 'shift']
    for key in stopkeys:
        keyboard.release(key)

def eat():
    mouse.press(button='right')
    time.sleep(2)
    mouse.release(button='right')

def place():
    mouse.press(button='right')
    mouse.release(button='right')

def mine(time):
    print("mine start")
    if time == "inf":
        mouse.press(button='left')
        mineAction.timed = False
        mineAction.action = True
    elif int(time) < 1:
        return "You can not use negative times"
    else:
        mouse.press(button='left')
        mineAction.timed = True
        mineAction.action = True
        mineAction.start = datetime.now()
        mineAction.timer = int(time)

def stopmine():
    mouse.release(button='left')
    mineAction.reset()

def hit():
    print("hit")
    mouse.click(button='left')

def hotbar(slot):
    try:
        slot = int(slot)
    except:
        print("hotbar broke lmaoo")
    print(f"hotbar {slot}")
    if slot > 9 or slot < 1:
        return "hotbar is only slot 1 - 9"
    keyboard.press_and_release(str(slot))

class Look():

    def __init__(self, tune=1):
        self.tune = tune

    def right(self, ammount):
        ammount = float(ammount)
        mouse.move(ammount * self.tune, 0, absolute=False, duration=0.5)

        print(f"looking right {ammount} deg")

    def left(self, ammount):
        ammount = float(ammount)
        mouse.move(-ammount * self.tune, 0, absolute=False, duration=0.5)

        print(f"looking left {ammount} deg")

    def up(self, ammount):
        ammount = float(ammount)
        mouse.move(0, -ammount * self.tune, absolute=False, duration=0.5)

        print(f"looking up {ammount} deg")

    def down(self, ammount):
        ammount = float(ammount)
        mouse.move(0, ammount * self.tune, absolute=False, duration=0.5)

        print(f"looking down {ammount} deg")

look = Look(tune=0.2)

def update():

    #walking
    if walkAction.timed and walkAction.action:
        if (datetime.now() - walkAction.start).seconds > walkAction.timer:
            stopwalk()
            return 1

    #running
    if runAction.timed and runAction.action:
        if (datetime.now() - runAction.start).seconds > runAction.timer:
            stopwalk()

    #mining
    if mineAction.timed and mineAction.action:
        if (datetime.now() - mineAction.start).seconds > mineAction.timer:
            stopmine()

if __name__ == '__main__':
    pass


#farted
