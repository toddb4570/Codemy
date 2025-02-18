import turtle
import os

os.system("clear")

# Create a turtle object
t = turtle.Turtle()

# Create a screen object
# screen = turtle.Screen()

def reset_turtle():
	t.clear()
	t.penup()
	t.home()
	t.pendown()

def draw_square(size):
	for _ in range(4):
		t.forward(size)
		t.left(90)


def draw_circle(radius):	
	t.circle(radius)

def draw_triangle(size):
	for _ in range(3):
		t.forward(size)
		t.left(120)


def draw_shape():
	while True:

		os.system("clear")
		print("\nSelect a shape to draw:")
		print("1. Square")
		print("2. Circle")
		print("3. Triangle")
		print("4. Clear canvas")
		print("5. EXIT")

		choice = input("Enter the number of your choice: ")

		if choice == "1":
			size = int(input("Enter the size of the square: "))
			draw_square(size)
		elif choice == "2":
			size = int(input("Enter the radius of the circle: "))
			draw_circle(size)
		elif choice == "3":
			size = int(input("Enter the size of the triangle: "))
			draw_triangle(size)
		elif choice == "4":
			reset_turtle()
		elif choice == "5":
			turtle.bye()
			break;
		else:
			print("Invalid choice. Try again. (type ,enter to continue)")


draw_shape()

