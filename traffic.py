import pyautogui as pg
import time
import random
print("position", pg.position())
print("size", pg.size())

x, y = pg.size()


def percentToPixelX(a):
    return x*a/100


def percentToPixelY(a):
    return y*a/100


def waitedscroll(a, b, scrollGap):
    for s in range(a, random.randrange(a+1, b)):
        pg.scroll(scrollGap)
        time.sleep(random.uniform(0.1, 1))


def buzziness():
    pg.move(random.randrange(5, 10), 0, random.uniform(0.1, 0.3))
    pg.move(0, random.randrange(5, 10), random.uniform(0.1, 0.3))
    pg.move(0, -random.randrange(5, 10), random.uniform(0.1, 0.3))
    pg.move(-random.randrange(5, 10), 0, random.uniform(0.1, 0.3))


def openQuitTor():
    pg.hotkey("ctrl", "q")
    openTor()


def openTor():
    pg.hotkey("ctrl", "alt", "d")
    pg.moveTo(1530, 1050)
    pg.click()
    time.sleep(6)


blogsList = ["https://www.wealthandtech.com/2022/12/start-your-journey-to-becoming-data.html",
             "https://www.wealthandtech.com/2022/12/become-web-developer-in-7-easy-steps.html",
             "https://www.wealthandtech.com/2022/12/boost-your-mood-instantly-with-these.html",
             "https://www.wealthandtech.com/2022/12/free-instagram-followers.html",
             "https://www.wealthandtech.com/2022/12/unlock-your-true-potential-defining.html",
             "https://www.wealthandtech.com/2022/12/achieve-dense-hair-with-ordinary-hair.html",
             "https://www.wealthandtech.com/2022/12/unlock-secret-to-skyrocketing-your.html",
             "https://www.wealthandtech.com/2022/12/the-best-baldness-cure-to-tackle-your.html",
             "https://www.wealthandtech.com/2022/12/how-to-stay-away-from-girls.html",
             "https://www.wealthandtech.com/2022/12/discover-power-of-self-care-guide-to.html",
             "https://www.wealthandtech.com/2022/12/conquering-loneliness-discover-how-to.html",
             "https://www.wealthandtech.com/2022/12/digital-detox-how-to-kick-your.html",
             "https://www.wealthandtech.com/2022/12/xc.html"]

count = 0
while True:
    if count == 0:
        openTor()
    elif count % 10:
        openQuitTor()

    count += 1

    pg.hotkey("win", "up")
    pg.moveTo(percentToPixelX(96.35), percentToPixelY(9.25), 2)
    pg.click()

    pg.moveTo(percentToPixelX(83.85), percentToPixelY(57.40), 2)
    pg.click()
    time.sleep(2)

    pg.moveTo(percentToPixelX(26.04), percentToPixelY(9.25), 2)
    pg.click()
    pg.typewrite(blogsList[random.randrange(0, len(blogsList))])
    pg.typewrite(["enter"])
    time.sleep(random.randrange(5, 10))
    pg.moveTo(random.randrange(percentToPixelX(10), percentToPixelX(90)),
              random.randrange(
        percentToPixelY(20), percentToPixelY(90)), random.uniform(0.25, 0.75))
    conditions = [time.sleep(random.randrange(5, 10)),
                  buzziness(),
                  pg.moveTo(random.randrange(percentToPixelX(10), percentToPixelX(90)),
                            random.randrange(
                      percentToPixelY(20), percentToPixelY(90)), random.uniform(0.25, 0.75)), pg.moveTo(random.randrange(percentToPixelX(10), percentToPixelX(90)),
                                                                                                        random.randrange(
                          percentToPixelY(20), percentToPixelY(90)), random.uniform(0.25, 0.75)),
                  waitedscroll(10, 40, -1), buzziness(),
                  time.sleep(random.uniform(1, 10)),
                  waitedscroll(5, 10, 1),
                  buzziness(),
                  time.sleep(random.uniform(1, 10)),
                  buzziness(),
                  time.sleep(random.uniform(1, 10)),
                  waitedscroll(10, 30, -1),
                  waitedscroll(5, 10, 1),
                  buzziness(),
                  ]
    random.shuffle(conditions)
    print(conditions)
    for i in conditions:
        i

    pg.moveTo(percentToPixelX(93.75), percentToPixelY(
        9.25), random.uniform(0.25, 2))
    pg.click()

    print("done loop", count)
    time.sleep(random.randrange(60, 80))
