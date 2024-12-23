class Circle:
    def __init__(self, R):
        self.R = R
    def get_radius(self):
        return self.R
    def set_radius(self, R):
        self.R = R

circle = Circle(4)
print(circle.get_radius())
circle.set_radius(45)
print(circle.get_radius())