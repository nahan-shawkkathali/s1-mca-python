
import area_module   
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))
rect_area = area_module.area_rectangle(length, width)
circle_area = area_module.area_circle(radius)
print("\nAreas Calculated:")
print(f"Area of Rectangle = {rect_area}")
print(f"Area of Circle = {circle_area:.2f}")
