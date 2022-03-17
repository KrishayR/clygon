import math


class InvalidInt(Exception):
    pass

class TooLessVars(Exception):
    pass

class UnidentifiableName(Exception):
    pass

def inv_sum_of_interior_angles(sum_interior_angle):
    self.sum_interior_angle = sum_interior_angle
    return (self.sum_interior_angle/180) + 2

def inv_interior_angles(interior_angle):
    self.interior_angle = interior_angle
    return (360/(180-self.interior_angle))

def area_form():
    return "The formula for area is πr^2"

def part_area_form():
    return "The formula for full circle area is πr^2. To find part of a circle, do central_angle/360 * the full circle area"

def perimeter_form():
    return "The formula for Perimeter is 2πr"

def finder_form():
    return "The formula is: Arc Length = (Central angle * π * Radius)/180  "

class Polygon:
    "Main class for polygon which includes common methods, other classes will inherit from here"

    def __init__(self, sides):
        self.sides = sides
        self.possible_sides = {3:"Triangle", 4:"Quadrilateral", 5:"Pentagon", 6:"Hexagon", 7:"Heptagon", 8:"Octagon", 9:"Nonagon", 10:"Decagon", 11:"Hendecagon", 12:"Dodecagon"}


    def name(self):
        try:
            return self.possible_sides[int(self.sides)]
        except KeyError:
            if int(self.sides) < 3:
                return f"Invalid shape: A polygon cannot have only {self.sides} side{'' if self.sides == 1 else 's'}."
            else:
                return f"{self.sides}-gon"
        except (ValueError, TypeError, ZeroDivisionError):
            raise InvalidInt("You have not provided a valid integer for the number of sides\n")
            


    def sum_of_interior_angles(self, exp=False):
        try:
            if exp == False:
                return (180 * (int(self.sides) - 2))
            else:
                print("The formula for the sum of interior angles is: 180(n-2) where n is the number of sides")
                print(f"180({int(self.sides)} - 2)")
                print(f"180({int(self.sides) - 2})")
                return (180 * (int(self.sides) - 2))
            
        except (ValueError, TypeError, ZeroDivisionError):
            raise InvalidInt("You have not provided a valid integer for the number of sides\n")

    def interior_angles(self, exp=False):
        try:
            if exp == False:
                return ((180 * (int(self.sides)))/ (int(self.sides)))
            else:
                print("The formula for each individual interior angle is: 180(n-2)/n where n is the number of sides")
                print(f"180({int(self.sides)} - 2)/{int(self.sides)}")
                print(f"180({int(self.sides) - 2})/{int(self.sides)}")
                print(f"{180 * (int(self.sides)-2)}/{int(self.sides)} ")
                return ((180 * (int(self.sides)-2))/ (int(self.sides)))
        
        except (ValueError, TypeError, ZeroDivisionError):
            raise InvalidInt("You have not provided a valid integer for the number of sides\n")

    def inv_sum_of_interior_angles(self, sum_interior_angle):
        self.sum_interior_angle = sum_interior_angle
        return (self.sum_interior_angle/180) + 2

    def inv_interior_angles(self, interior_angle):
        self.interior_angle = interior_angle
        return (360/(180-self.interior_angle))

    def central_angles(self, exp=False):
        try:
            if exp == False:
                return 360/int(self.sides)
            else:
                print("The sum of all central angles is 360 degrees, so we can derive the following formula:")
                print("The formula for each central angle is: 360/n where n is the number of sides")
                print(f"360/{int(self.sides)}")
                return 360/int(self.sides)
        
        except (ValueError, TypeError, ZeroDivisionError):
            raise InvalidInt("You have not provided a valid integer for the number of sides\n")
        
    def exterior_angles(self, exp=False):
        try:
            if exp == False:
                return 360/int(self.sides)
            else:
                print("The sum of all exterior angles is 360 degrees, so we can derive the following formula:")
                print("The formula for each exterior angle is: 360/n where n is the number of sides")
                print(f"360/{int(self.sides)}")
                return 360/int(self.sides)
        
        except (ValueError, TypeError, ZeroDivisionError):
            raise InvalidInt("You have not provided a valid integer for the number of sides\n")

    def perimeter(self, base):
        self.base = base
        return base * self.sides 

    def area(self, **kwargs):
        """Enter the arguments in this format -> base=?, apothem=?, radius=?, where ? corresponds to an integer number. Omit any arguments that you are not given."""
        self.given = kwargs
        if "base" in self.given.keys():
            base = self.given.get("base")
            apothem = (base/2)/math.tan(math.radians(self.central_angles()/2))
            return ((apothem * (base/2))/2) * (2*self.sides)
        elif "apothem" in self.given.keys():
            apothem = self.given.get("apothem")
            base = math.tan(math.radians(self.central_angles()/2)) * apothem
            return ((apothem * base)/2) * (2*self.sides)
        elif "radius" in self.given.keys():
            radius = self.given.get("radius")
            apothem = math.cos(math.radians(self.central_angles()/2)) * radius
            base = math.sin(math.radians(self.central_angles()/2)) * radius
            return ((apothem * base)/2) * (2*self.sides)

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius**2) * math.pi

    def part_area(self, radius, central_angle):
        self.central_angle = central_angle
        return (self.central_angle/360) * ((self.radius**2) * math.pi)
        

    def perimeter(self):
        return (2 * self.radius) * math.pi
            
    def finder(self, **kwargs):
        """Enter the arguments in this format -> arc_length=?, central_angle=?, radius=?, where ? corresponds to an integer number. (Central angle in degrees) Omit any arguments that you are not given."""
        self.given = kwargs
        # print(self.given)
        
        if len(self.given) < 2:
            raise TooLessVars("Cannot figure out the answer using the data you have provided, please enter at least 2 variables")

        for i in self.given.keys():
            if i not in ["arc_length", "central_angle", "radius"]:
                raise UnidentifiableName("Each argument entered must be called 'arc_length', 'central_angle', or 'radius'")

        if self.given.keys() >= {"arc_length", "central_angle"}:
            return (self.given.get("arc_length") * 180)/(self.given.get("central_angle") * math.pi)
        
        elif self.given.keys() >= {"arc_length", "radius"}:
            return (self.given.get("arc_length") * 180)/(self.given.get("radius") * math.pi)

        elif self.given.keys() >= {"radius", "central_angle"}:
            return (self.given.get("central_angle") * math.pi * self.given.get("radius"))/180




    

