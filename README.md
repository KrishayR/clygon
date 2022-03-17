# clygon

Clygon is a library built to calculate everything from circles to polygons. You can calculate the interior angles of a polygon, or the area of any n-gon, and even the arc length, radius, or central angle of a circle.

To install the package, run `pip install clygon==0.0.5` in your terminal or cmd prompt.

How can I use it?

1. Import the library:
 ```
 from clygon.shapes import Polygon, Circle
 ```
2. Instantiate the class:
```
eleven = Polygon(sides=11)
```
3. Perform your calculations/attributes:
```
print("The shape is called:", eleven.name())
print("The sum of the interior angles is:", eleven.sum_of_interior_angles())
print(eleven.sum_of_interior_angles(exp=True))
print("\n\n The interior angles are", eleven.interior_angles())
print(eleven.interior_angles(exp=True))
```
4. Run the code!

Example usage for polygons:
```
from clygon.shapes import Polygon

eleven = Polygon(sides=11)
print("The shape is called:", eleven.name())
print("The sum of the interior angles is:", eleven.sum_of_interior_angles())
print(eleven.sum_of_interior_angles(exp=True))
print("\n\n The interior angles are", eleven.interior_angles())
print(eleven.interior_angles(exp=True))

fourtytwo = Polygon(sides=42)
print(fourtytwo.name())
print("if apothem=5, area =",fourtytwo.area(apothem=5))
print("if base=5, area =",fourtytwo.area(base=5))
print("if base=5, perimeter =",fourtytwo.perimeter(base=5))
print("ext. angles=",fourtytwo.exterior_angles())



```
Output:
```
The shape is called: Hendecagon
The sum of the interior angles is: 1620
The formula for the sum of interior angles is: 180(n-2) where n is the number of sides
180(11 - 2)
180(9)
1620


 The interior angles are 180.0
The formula for each individual interior angle is: 180(n-2)/n where n is the number of sides
180(11 - 2)/11
180(9)/11
1620/11 
147.27272727272728
42-gon
if apothem=5, area = 78.68662202004133
if base=5, area = 3502.819067894399
if base=5, perimeter = 210
ext. angles= 8.571428571428571
```

Example usage for circles:

```
from clygon.shapes import Circle, finder_form

circle = Circle(radius=8)
print("Area:", circle.area())
print("The area of some of the circle is:", circle.part_area(radius=8, central_angle=40))
print("The perimeter is:", circle.perimeter())
print("If the arc length is 50, the central angle is: ", circle.finder(arc_length=50, radius=8))
print("The formula to solve for the central angle is: ", finder_form())
```

Output:
```
Area: 201.06192982974676
The area of some of the circle is: 22.340214425527417
The perimeter is: 50.26548245743669
If the arc length is 50, the central angle is:  358.09862195676453
The formula to solve for the central angle is:  The formula is: Arc Length = (Central angle * π * Radius)/180  
```
