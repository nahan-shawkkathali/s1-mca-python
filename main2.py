
from graphics import rectangle, circle
from graphics.threeD_graphics import cuboid, sphere

print("Rectangle:")
print("Area =", rectangle.area(10, 5))
print("Perimeter =", rectangle.perimeter(10, 5))

print("\nCircle:")
print("Area =", circle.area(7))
print("Perimeter =", circle.perimeter(7))

print("\nCuboid:")
print("Surface Area =", cuboid.surface_area(2, 3, 4))
print("Perimeter =", cuboid.perimeter(2, 3, 4))

print("\nSphere:")
print("Surface Area =", sphere.surface_area(5))
print("Perimeter =", sphere.perimeter(5))
