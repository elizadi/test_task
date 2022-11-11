import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from math import ceil, sqrt, sin, cos, radians
import random
import matplotlib.colors as colors



# class Generating():
#     def __init__(self, h, w) -> None:
#         self

def __init__(self, Height = 480, Width = 640, rectMin = 150, rectMax = 250):
    self.Height = Height
    self.Width = Width
    self.rectMin = rectMin
    self.rectMax = rectMax 


def random_color():
    r = np.random.random()
    b = np.random.random()
    g = np.random.random()    
    color = (r, g, b)
    return color

fig, ax = plt.subplots()

ax.set_facecolor(random_color())

h = random.randint(150, 250)
w = random.randint(150, 250)
half_diagonal = ceil(sqrt(h**2 + w**2))#+5   #если результат извлечения корня не является целым числом, то округляет в сторону большего числа
rot = random.randint(0, 89)
rot_degree = radians(rot)

point0 = [random.randint(w, 640 - half_diagonal), random.randint(0, 480 - half_diagonal)]
point1 = [round(point0[0] + w * cos(rot_degree)), round(point0[1] + w * sin(rot_degree))]
point3 = [round(point0[0] - h * sin(rot_degree)), round(point0[1] + h * cos(rot_degree))]
point2 = [point3[0] - point0[0] + point1[0], point3[1] - point0[1] + point1[1]]
points = [point0, point1, point2, point3]

transp_points = np.transpose(points)
xmin = min(transp_points[0])
ymax = max(transp_points[1])
xmax = max(transp_points[0])
ymin = min(transp_points[1])
lim_rect_w = xmax - xmin
lim_rect_h = ymax - ymin


rect = Rectangle((point0[0], point0[1]), w, h, angle = rot, fc = random_color())
ax.add_patch(rect) 

lim_rect = Rectangle((xmin, ymin), lim_rect_w, lim_rect_h, angle = 0, ec = random_color(), fill = None)
ax.add_patch(lim_rect)



print("Описывающий прямоугольник:")
print("x = {0}, y = {1}, w = {2}, h = {3}".format(xmin, ymax, lim_rect_w, lim_rect_h))
# print('(415, 211), 164, 190, 57')
print("Координаты углов:")
for i, point in enumerate(points):
    print("x{0} = {1}, y{0} = {2}".format(i+1, point[0], point[1]))
    
print('h = {0}, w = {1}, rot = {2}'.format(h, w, rot))


print()
print(transp_points)
print()

plt.xlim([0, 640])
plt.ylim([0, 480])

plt.show()