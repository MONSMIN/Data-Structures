import turtle


def branch(t, length, width, color):
    if width <= 0 or length <= 0:
        return
    else:
        t.pensize(width)
        t.color(color)
        t.forward(length)
        t.left(45)
        branch(t, length - 15, width - 1, color)
        t.right(90)
        branch(t, length - 15, width - 1, color)
        t.left(45)
        t.back(length)


def main():
    try:
        input_length = int(input("Введіть рівень довжини (наприклад, 120): "))
        input_width = int(input("Введіть рівень товщини (наприклад, 10): "))
    except ValueError:
        print("Будь ласка, введіть числове значення.")
        return

    window = turtle.Screen()
    window.bgcolor("skyblue")
    window.screensize(800, 600)

    t = turtle.Turtle()
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.speed(0)
    t.left(90)

    branch(t, input_length, input_width, "green")

    window.exitonclick()


if __name__ == "__main__":
    main()
