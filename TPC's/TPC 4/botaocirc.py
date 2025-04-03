from graphics import Point, Circle, Text

class BotaoCircular:

    def __init__(self, win, center, radius, label):
        self.center = center
        self.radius = radius
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.active = False  # Começa desativado
        self.deactivate()

    def clicked(self, p):
        dx = p.getX() - self.center.getX()
        dy = p.getY() - self.center.getY()
        distance = (dx**2 + dy**2) ** 0.5
        return self.active and distance <= self.radius

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
