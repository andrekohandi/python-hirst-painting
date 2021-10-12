# # to get the list of color from image.jpg (hirst painting)
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst_painting/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as t
import random

t.colormode(255)
boss = t.Turtle()
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 
77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

boss.speed("fast")
boss.penup()
boss.hideturtle()
boss.setheading(225)
boss.forward(300)
boss.setheading(0)

num_of_dots = 100

for dot in range(1, num_of_dots + 1): 
    boss.dot(20, random.choice(color_list))
    boss.forward(50)

    if dot % 10 == 0:
        boss.setheading(90)
        boss.forward(50)
        boss.setheading(180)
        boss.forward(500)
        boss.setheading(0)


screen = t.Screen()
screen.exitonclick()