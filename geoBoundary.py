import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point Coordinates: ({self.x},{self.y})"

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Center: {self.center}\nRadius: {self.radius}"

class Rectangle:
    def __init__(self, bottom_left, width, height):
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def __str__(self):
        return f"Width: {self.width}\nHeight: {self.height}\nBottom-Left Point: {self.bottom_left}"
    
    def corners(self):
        bl = self.bottom_left
        br = Point(bl.x + self.width, bl.y)
        tl = Point(bl.x, bl.y + self.height)
        tr = Point(bl.x + self.width, bl.y + self.height)
        return [bl, br, tl, tr]

def distance(p1: Point, p2: Point):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def point_in_circle(circle: Circle, point: Point):
    #Return True if point lies inside or on the boundary of the circle.
    return (distance(circle.center, point) <= circle.radius)

def rect_in_circle(circle: Circle, rect: Rectangle):
    #Return True if all corners of the rectangle lie inside or on the boundary of the circle.
    return all(point_in_circle(circle, corner) for corner in rect.corners())

def rect_circle_overlap(circle: Circle, rect: Rectangle, partial_overlap=False):
    corners = rect.corners()
    
    # Check if any corner is inside the circle
    if any(point_in_circle(circle, corner) for corner in corners):
        return True
    
    if not partial_overlap:
        return False
    
    # 1. Check if circle center is inside rectangle
    c = circle.center
    r = rect
    if (r.bottom_left.x <= c.x <= r.bottom_left.x + r.width and r.bottom_left.y <= c.y <= r.bottom_left.y + r.height):
        return True
    
    # 2. Check distance from circle center to each edge of rectangle
    closest_x = min(max(c.x, r.bottom_left.x), r.bottom_left.x + r.width)
    closest_y = min(max(c.y, r.bottom_left.y), r.bottom_left.y + r.height)
    closest_point = Point(closest_x, closest_y)
    
    # If distance from circle center to closest point <= radius, they overlap
    if distance(c, closest_point) <= circle.radius:
        return True
    return False

# Instantiate Circle with center at (150, 100) and radius 75
center_point = Point(150, 100)
circle = Circle(center_point, 75)
print("Circle Coordinates:")
print(circle)

    # Define a rectangle inside the circle
rect1 = Rectangle(Point(140, 90), 10, 10)
print("\nRect1 Position: ")
print(rect1)
print(f"rect1 inside circle? [{rect_in_circle(circle, rect1)}]")
    
    # Define a rectangle partially overlapping
rect2 = Rectangle(Point(210, 100), 20, 20)
print("\nRect2 Position: ")
print(rect2)
print(f"rect2 corner in circle? [{rect_circle_overlap(circle, rect2)}]")
print(f"rect2 partial overlap? [{rect_circle_overlap(circle, rect2, partial_overlap=True)}]")

    # Define a rectangle completely outside
rect3 = Rectangle(Point(230, 200), 10, 10)
print("\nRect3 Position: ")
print(rect3)
print(f"rect3 corner in circle? [{rect_circle_overlap(circle, rect3)}]")
print(f"rect3 partial overlap? [{rect_circle_overlap(circle, rect3, partial_overlap=True)}]")
