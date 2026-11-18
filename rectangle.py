class Rectangle:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return f"(p={self.p}, q={self.q})"

    def get_width(self):
        return self.q.x - self.p.x

    def get_height(self):
        return self.q.y - self.p.y

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def area(self):
        return self.get_width() * self.get_height()

    def contains(self, pt):
        if self.p.x <= pt.x:
            if pt.x <= self.q.x:
                if self.p.y <= pt.y:
                    if pt.y <= self.q.y:
                        return True
        return False