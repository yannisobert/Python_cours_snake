class Snake:
    def __init__(self):
        self.block = 10
        self.x_positive = self.block
        self.x_negative = -self.block
        self.y_negative = -self.block
        self.y_positive = self.block

    def moveLeft(self):
        return self.x_negative

    def moveRight(self):
        return self.x_positive

    def moveUp(self):
        return self.y_negative

    def moveDown(self):
        return self.y_positive
