
import tkinter as tk
from tkinter import *
import math


def fresh():
    answer.delete(1.0, END)


class calculation:
    # =================================CircleMethod

    def circleMethod():
        global radius
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of radius:")
        value.grid(row=0, column=0)
        radius = Entry(valueFrame1)
        radius.grid(row=0, column=1, pady=5, padx=5, ipadx=5)
        valueFrame1.pack(pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.C_area)
        result.grid(row=0, column=2)
        circle.config(state=DISABLED)

    # ===================================SquareMethod

    def squareMethod():
        global side
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side:")
        value.grid(row=0, column=0)
        side = Entry(valueFrame1)
        side.grid(row=0, column=1, pady=5, padx=5, ipadx=5)
        valueFrame1.pack(pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.S_area)
        result.grid(row=0, column=2)
        square.config(state=DISABLED)

    # =====================================RectangleMethod
    def rectangleMethod():
        global length, breadth
        valueFrame = Frame(root)
        value = Label(valueFrame, text="Length:")
        value.grid(row=0, column=0)
        length = Entry(valueFrame)
        length.grid(row=0, column=1, pady=5)

        value = Label(valueFrame, text="Breadth:")
        value.grid(row=0, column=2)
        breadth = Entry(valueFrame)
        breadth.grid(row=0, column=3, pady=5)

        result = Button(valueFrame, text="Get Answer!", bg="green", command=calculation.R_area)
        result.grid(row=0, column=4)
        valueFrame.pack(pady=5, padx=5, ipadx=5)
        rectangle.config(state=DISABLED)

    # ======================================TriangleMethod
    def triangleMethod():
        global side1, side2, side3
        valueFrame = Frame(root)
        value = Label(valueFrame, text="side1:")
        value.grid(row=0, column=0)
        side1 = Entry(valueFrame)
        side1.grid(row=0, column=1)
        value = Label(valueFrame, text="side2:")
        value.grid(row=0, column=2)
        side2 = Entry(valueFrame)
        side2.grid(row=0, column=3)
        value = Label(valueFrame, text="side3:")
        value.grid(row=0, column=4)
        side3 = Entry(valueFrame)
        side3.grid(row=0, column=5)
        result = Button(valueFrame, text="Get Answer!", bg="green", command=calculation.T_area)
        result.grid(row=0, column=10)
        valueFrame.pack(pady=5, padx=5, ipadx=5)
        triangle.config(state=DISABLED)

    # ====================================HexagonMethod
    def hexagonMethod():
        global side_a
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side_a:")
        value.grid(row=0, column=0)
        side_a = Entry(valueFrame1)
        side_a.grid(row=0, column=1, pady=5, padx=5, ipadx=5)
        valueFrame1.pack(pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.H_area)
        result.grid(row=0, column=3)
        hexagon.config(state=DISABLED)

    # =====================================OctagonMethod

    def octagonMethod():
        global side_b
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side_b:")
        value.grid(row=0, column=0)
        side_b = Entry(valueFrame1)
        side_b.grid(row=0, column=1, pady=5, padx=5, ipadx=5)
        valueFrame1.pack(pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.O_area)
        result.grid(row=0, column=3)
        octagon.config(state=DISABLED)

    # =====================================CubeMethod
    def cubeMethod():
        global side_cube
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side:")
        value.grid(row=0, column=0)
        side_cube = Entry(valueFrame1)
        side_cube.grid(row=0, column=1, pady=5, padx=5, ipadx=5)
        valueFrame1.pack(pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.Cube_area)
        result.grid(row=0, column=2)
        cube.config(state=DISABLED)

    # =================================CuboidMethod
    def CuboidMethod():
        global l_cub, b_cub, h_cub
        valueFrame = Frame(root)
        value = Label(valueFrame, text="l:")
        value.grid(row=0, column=0)
        l_cub = Entry(valueFrame)
        l_cub.grid(row=0, column=1)
        value = Label(valueFrame, text="b:")
        value.grid(row=0, column=2)
        b_cub = Entry(valueFrame)
        b_cub.grid(row=0, column=3)
        value = Label(valueFrame, text="h:")
        value.grid(row=0, column=4)
        h_cub = Entry(valueFrame)
        h_cub.grid(row=0, column=5)
        result = Button(valueFrame, text="Get Answer!", bg="green", command=calculation.Cuboid_area)
        result.grid(row=0, column=10)
        valueFrame.pack(pady=5, padx=5, ipadx=5)
        Cuboid.config(state=DISABLED)
        # ==================================SphereMethod

    def sphereMethod():
        global sphere_g
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of radius:")
        value.grid(row=0, column=0)
        sphere_g = Entry(valueFrame1)
        sphere_g.grid(row=0, column=1, pady=10, padx=10, ipadx=10)
        valueFrame1.pack(pady=10, padx=10, ipadx=10)
        result = Button(valueFrame1, text="Get Answer!", bg="green", command=calculation.Sphere_area)
        result.grid(row=0, column=2)
        sphere.config(state=DISABLED)

    # ==================================Area of triangle

    def T_area():
        s1 = side1.get()
        s2 = side2.get()
        s3 = side3.get()
        s = 1 / 2 * (float(s1) + float(s2) + float(s3))
        areaOfTriangle = math.sqrt(s * (s - float(s1)) * (s - float(s2)) * (s - float(s3)))
        answer.delete(1.0, END)
        answer.insert(INSERT, "S =1/2(a+b+c)\n=>")
        answer.insert(INSERT, s)
        answer.insert(INSERT, "area of triangle =\n=>""sqrt(s(s-a)(s-b)(s-c)\n=>")
        answer.insert(INSERT, areaOfTriangle)
        answer.insert(INSERT, " Ans.")

    # ======================================Area of Rectangle
    def R_area():
        l = length.get()
        b = breadth.get()

        areaOfRectangle = float(l) * float(b)
        answer.delete(1.0, END)
        answer.insert(INSERT, "Area of rectangle=\n=> length X breadth\n=>")
        answer.insert(INSERT, l)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfRectangle)
        answer.insert(INSERT, " Ans. ")

    # ======================================Area of Circle

    def C_area():
        pi = 3.14
        r = radius.get()
        answer.delete(1.0, END)
        areaOfCircle = pi * float(r) * float(r)
        answer.insert(INSERT, "Area of Circle=Pi*r*r\n=>22/7*r*r\n3.14 X ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfCircle)
        answer.insert(INSERT, " Ans. ")

    # ======================================Area of Square
    def S_area():
        s = side.get()
        answer.delete(1.0, END)
        areaOfSquare = float(s) * float(s)
        answer.insert(INSERT, "Area of Square=s*s\n=>s*s\n")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfSquare)
        answer.insert(INSERT, " Ans. ")

    # =====================================Area of Hexagon
    def H_area():
        a = side_a.get()
        answer.delete(1.0, END)
        areaOfHexagon = 2.6 * float(a) * float(a)
        answer.insert(INSERT, "Area of Hexagon=2.6*a*a\n=>2.6*a*a\n")
        answer.insert(INSERT, "2.6 X ")
        answer.insert(INSERT, a)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, a)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfHexagon)
        answer.insert(INSERT, " Ans. ")

    # ======================================Area of Octagon
    def O_area():
        b = side_b.get()
        answer.delete(1.0, END)
        areaOfOctagon = 4.82 * float(b) * float(b)
        answer.insert(INSERT, "Area of Octagon=4.82*b*b\n=>4.82*b*b\n")
        answer.insert(INSERT, "4.82 X ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfOctagon)
        answer.insert(INSERT, " Ans. ")

    # ======================================Area of Cube
    def Cube_area():
        s = side_cube.get()
        answer.delete(1.0, END)
        areaOfCube = 6 * float(s) * float(s)
        answer.insert(INSERT, "Area of Cube=6*s*s\n=>6*s*s\n")
        answer.insert(INSERT, '6')
        answer.insert(INSERT, ' X ')
        answer.insert(INSERT, s)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfCube)
        answer.insert(INSERT, " Ans. ")

    # =====================================Area of cuboid
    def Cuboid_area():
        l = l_cub.get()
        b = b_cub.get()
        h = h_cub.get()
        areaOfCuboid = 2 * (float(l) * float(b) + float(b) * float(h) + float(h) * float(l))
        answer.delete(1.0, END)
        answer.insert(INSERT, "2")
        answer.insert(INSERT, " X( ")
        answer.insert(INSERT, l)
        answer.insert(INSERT, b)
        answer.insert(INSERT, " + ")
        answer.insert(INSERT, h)
        answer.insert(INSERT, b)
        answer.insert(INSERT, " + ")
        answer.insert(INSERT, l)
        answer.insert(INSERT, h)
        answer.insert(INSERT, " ) ")
        answer.insert(INSERT, "area of Cuboid =\n=>""2*(l*b+b*h+h*l)")
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfCuboid)
        answer.insert(INSERT, " Ans.")

    # ============================================Area of sphere
    def Sphere_area():
        pi = 3.14
        g = sphere_g.get()
        answer.delete(1.0, END)
        areaOfSphere = 4 * pi * float(g) * float(g)
        answer.insert(INSERT, "Area of Sphere=4*Pi*g*g\n=>4*22/7*g*g\n3.14 X ")
        answer.insert(INSERT, g)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, g)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfSphere)
        answer.insert(INSERT, " Ans. ")


root = tk.Tk()
root.title("Area App")

frame1 = Frame(root)
title = Label(frame1, text="Calculate Area of different Shapes", font=("arial", 20, "bold"), fg="oliveDrab")
title.grid(row=0, column=0)
choice = Label(frame1, text="Which shape do you want?", font=("arial", 15, "bold italic"), fg="SlateBlue2")
choice.grid(row=1, column=0)
refresh = Button(frame1, text="Clear All", bg="red", fg="black", command=fresh)
refresh.grid(row=1, column=2)
frame1.pack(side=TOP, pady=10, padx=5, ipadx=5)

frame2 = Frame(root)
circle = Button(frame2, font=("calibri", 15), text="Circle", bg="LightCoral", relief=RAISED,
                command=calculation.circleMethod)
circle.grid(row=0, column=0)
square = Button(frame2, font=("calibri", 15), text="Square", bg="tan", relief=RAISED, command=calculation.squareMethod)
square.grid(row=0, column=1)
triangle = Button(frame2, font=("calibri", 15), text="Triangle", relief=RAISED, bg="LightCoral",
                  command=calculation.triangleMethod)
triangle.grid(row=0, column=2)
rectangle = Button(frame2, font=("calibri", 15), text="Rectangle", relief=RAISED, bg="tan",
                   command=calculation.rectangleMethod)
rectangle.grid(row=0, column=3)
hexagon = Button(frame2, font=("calibri", 15), text="Hexagon", bg="LightCoral", relief=RAISED,
                 command=calculation.hexagonMethod)
hexagon.grid(row=0, column=4)
octagon = Button(frame2, font=("calibri", 15), text="Octagon", relief=RAISED, bg="tan",
                 command=calculation.octagonMethod)
octagon.grid(row=0, column=5)
cube = Button(frame2, font=("calibri", 15), text="Cube", bg="LightCoral", relief=RAISED, command=calculation.cubeMethod)
cube.grid(row=1, column=0)
Cuboid = Button(frame2, font=("calibri", 15), text="Cuboid", bg="tan", relief=RAISED, command=calculation.CuboidMethod)
Cuboid.grid(row=1, column=1)
sphere = Button(frame2, font=("calibri", 15), text="Sphere", bg="LightCoral", relief=RAISED,
                command=calculation.sphereMethod)
sphere.grid(row=1, column=2)
frame2.pack(side=TOP)

frame3 = Frame(root, bg="beige")
answer = Text(frame3, height=10, relief=SUNKEN, wrap=WORD)
answer.grid(padx=5, ipadx=5, pady=5, ipady=5)
frame3.pack(side=BOTTOM)

mainloop()

