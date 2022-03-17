# clygon

Clygon is a library built to calculate everything from circles to polygons. You can calculate the interior angles of a polygon, or the area of any n-gon, and even the arc length, radius, or central angle of a circle.

To install the package, run `pip install clygon` in your terminal or cmd prompt.

How can I use it?

1. Import the library - `import clygon`
2. Instantiate the class:
```
eleven = clygon.Polygon(sides=11)
```
3. Perform your calculations/attributes:
```
print("The shape is called:", eleven.name())
print("The sum of the interior angles is:", eleven.sum_of_interior_angles())
print(eleven.sum_of_interior_angles(exp=True))
print("\n\n The interior angles are", eleven.interior_angles())
print(eleven.interior_angles(exp=True))
```
5. Run the code!

Example usage:
```
import clygon

eleven = clygon.Polygon(sides=11)
print("The shape is called:", eleven.name())
print("The sum of the interior angles is:", eleven.sum_of_interior_angles())
print(eleven.sum_of_interior_angles(exp=True))
print("\n\n The interior angles are", eleven.interior_angles())
print(eleven.interior_angles(exp=True))

fourtytwo = clygon.Polygon(sides=42)
print(fourtytwo.name())
print("if apothem=5, area =",fourtytwo.area(apothem=5))
print("if base=5, area =",fourtytwo.area(base=5))
print("if base=5, perimeter =",fourtytwo.perimeter(base=5))
print("ext. angles=",fourtytwo.exterior_angles())

```
Output:
```
