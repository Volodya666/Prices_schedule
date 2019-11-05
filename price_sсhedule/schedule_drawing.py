import turtle
from file_writing import all_prices, all_names, all_colors

a = turtle.Turtle()  # a = arrow
a.speed(0)
a.ht()
a.up()
a.goto(-681, -343)
a.down()
a.goto(-681, 351)
a.goto(-681, -343)
a.goto(700, -343)
a.goto(-681, -343)

def Chart(col):
    a.color(col)
    for i in range(len(all_prices)):
        a.goto(-681+(i+1)*30, int(all_prices[i]) + -342)
        a.dot(4)
        a.up()
        a.fd(4)
        a.write(str(all_prices[i]))
        a.bk(4)
        a.down()
    for name in all_names:
        print(col + "--" + name)
    a.up()
    a.goto(-681, -343)
    a.down()
    turtle.done()


for col in all_colors:
    Chart(col)