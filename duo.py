import pyautogui
import keyboard
import time

cuento = "https://www.duolingo.com/stories/en-es-the-paper-bag"

you = "you know how"
wait = "wait a minute"
three = (600,370,200,200)
check = (400,400,400,200)


def next():
    while True:
        if pyautogui.pixel(1002,688)[2] == 2:
            pyautogui.click(1002,688)
            time.sleep(0.2)
            break

def write(word):
    pyautogui.write(word)

def click(image,reg = (400,420,600,100),checkbox=False,conf=0.9):
    while True:
        pos = pyautogui.locateOnScreen(image, region=reg, grayscale=True, confidence = conf)
        if pos != None:
            if checkbox:
                x = pos.left-30
                y = pos.top+10
                pyautogui.click(x,y)
            else:
                pyautogui.click(pos)
            time.sleep(0.2)
            break

def clickAll(images):
    for image in images:
        click(image,conf=0.8)

for i in range(4):
    next()
click('ansLate.png',reg = three)
for i in range(3):
    next()
time.sleep(2)
write(you)
for i in range(3):
    next()
clickAll([
    'you.png',
    'wont.png',
    'what.png',
    'just.png'
])
for i in range(6):
    next()
click('trouble.png',reg=check,checkbox=True)
for i in range(4):
    next()
click('jealous.png')
for i in range(3):
    next()
time.sleep(2)
write(wait)
for i in range(12):
    next()
click('bakery.png',reg=check,checkbox=True,conf=0.8)
for i in range(5):
    next()
print("late.png")
click('late.png',reg=(400,350,400,200),checkbox=True,conf=0.7)
for i in range(5):
    next()
click('dessert.png',reg=(400,400,500,200),checkbox=True,conf=0.7)
next()