class Direction:
    RIGHT = 0
    UP = 1
    DOWN = 2
    LEFT = 3

class Robot:
    def __init__(self):
        print "Robot Initialized"
        self.posX = 0
        self.posY = 0
        self.direction = Direction.UP

    def move(self, dist):
        if self.direction == Direction.UP:
            self.posY += dist
        elif self.direction == Direction.DOWN:
            self.posY -= dist
        elif self.direction == Direction.LEFT:
            self.posX -= dist
        elif self.direction == Direction.RIGHT:
            self.posX += dist

    def turnRight(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN

    def turnLeft(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP

    def getPos(self):
        return self.posX, self.posY
