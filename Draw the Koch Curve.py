import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
           koch_curve(t, length/3, level-1)
           t.left(angle)

def main():
    # Set up the turtle and screen
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)

    # Get the level number from the user
    level = int(input("Enter the level number: "))

    # Set the initial length of the curve
    length = 300

    # Move the turtle to the starting position
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the Koch Curve
    koch_curve(t, length, level)

    # Hide the turtle and hold the screen open
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()
