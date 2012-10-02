import robot

UP = robot.Direction.UP
DOWN = robot.Direction.DOWN
LEFT = robot.Direction.LEFT
RIGHT = robot.Direction.RIGHT

trail = []

def turnLeft():
    bot.turnLeft()

def turnRight():
    bot.turnRight()

def move(dist):
    trail.append((getX(), getY()))

    if bot.direction == UP:
        for y in range(getY(), getY() + dist):
            trail.append((getX(), y))
    elif bot.direction == DOWN:
        for y in reversed(range(getY() - dist, getY())):
            trail.append((getX(), y))
    elif bot.direction == LEFT:
        for x in reversed(range(getX() - dist, getX())):
            trail.append((x, getY()))
    if bot.direction == RIGHT:
        for x in range(getX(), getX() + dist):
            trail.append((x, getY()))

    bot.move(dist)
    bot.checkBounds((-9, -9, 9, 9))

def getX():
    x, y = bot.getPos()
    return x

def getY():
    x, y = bot.getPos()
    return y

def getDir():
    return bot.direction

def getDirS():
    if bot.direction == UP:
        return "Up"
    elif bot.direction == DOWN:
        return "Down"
    elif bot.direction == LEFT:
        return "Left"
    elif bot.direction == RIGHT:
        return "Right"

def inTrail(point):
    for i in trail:
        if i == point: 
            return True
    return False

def printMap():
    print 'Current Robot Facing: ' + getDirS()
    print '=' * 21
    for i in reversed(range(-9,10)):
        s = '|'
        for j in range(-9,10):
            if (getY() == i) and (getX() == j):
                s += 'X'
            elif inTrail((j, i)): 
                s += '.'
            else:
                s += ' '
        s += '|'
        print s
    print '=' * 21

bot = robot.Robot()
print "BotWrapper Initialized!"
