import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from math import ceil, sqrt, sin, cos, radians
import random




class Generation:
#     def __init__(self, h, w) -> None:
#         self

    def __init__(self, Height, Width, rectMin, rectMax):
        self.Height = Height
        self.Width = Width
        self.rectMin = rectMin
        self.rectMax = rectMax 


    def random_color(self):
        r = np.random.random()
        b = np.random.random()
        g = np.random.random()    
        color = (r, g, b)
        return color

    def rect(self):
        h = random.randint(self.rectMin, self.rectMax)
        w = random.randint(self.rectMin, self.rectMax)
        half_diagonal = ceil(sqrt(h**2 + w**2))#+5   #если результат извлечения корня не является целым числом, то округляет в сторону большего числа
        rot = random.randint(0, 89)
        rot_degree = radians(rot)

        point0 = [random.randint(w, self.Width - half_diagonal), random.randint(0, self.Height - half_diagonal)]
        point1 = [round(point0[0] + w * cos(rot_degree)), round(point0[1] + w * sin(rot_degree))]
        point3 = [round(point0[0] - h * sin(rot_degree)), round(point0[1] + h * cos(rot_degree))]
        point2 = [point3[0] - point0[0] + point1[0], point3[1] - point0[1] + point1[1]]
        points = [point0, point1, point2, point3]

        return points, w, h, rot

    def rect_lim(self, points):    
        transp_points = np.transpose(points)
        xmin = min(transp_points[0])
        ymax = max(transp_points[1])
        xmax = max(transp_points[0])
        ymin = min(transp_points[1])
        lim_rect_w = xmax - xmin
        lim_rect_h = ymax - ymin

        return xmin, ymin, lim_rect_w, lim_rect_h, ymax

    # return points, w, h, rot, xmin, ymin, lim_rect_w, lim_rect_h

Height, Width, rectMin, rectMax = 480, 640, 150, 250

gen = Generation(Height, Width, rectMin, rectMax)
fig, ax = plt.subplots()
ax.set_facecolor(gen.random_color())


points, w, h, rot = gen.rect()

xmin, ymin, lim_rect_w, lim_rect_h, ymax = gen.rect_lim(points)

rect = Rectangle((points[0][0], points[0][1]), w, h, angle = rot, fc = gen.random_color())
ax.add_patch(rect) 

lim_rect = Rectangle((xmin, ymin), lim_rect_w, lim_rect_h, angle = 0, fill = None, ec = gen.random_color())
ax.add_patch(lim_rect)

# ax.annotate('(x1, y1)', (points[0][0], points[0][1] - 20))
# ax.annotate('(x2, y2)', (points[1][0], points[1][1]))
# ax.annotate('(x3, y3)', (points[2][0], points[2][1] + 5))
# ax.annotate('(x4, y4)', (points[3][0], points[3][1] + 25))

# print('Описывающий прямоугольник:')
# print('x = {0}, y = {1}, w = {2}, h = {3}'.format(xmin, ymax, lim_rect_w, lim_rect_h))
# print('Координаты углов:')
# for i, point in enumerate(points):
#     print('x{0} = {1}, y{0} = {2}'.format(i+1, point[0], point[1]))
#     # ax.annotate('(x{0}, y{0})'.format(i+1), (point[0], point[1] + 5))

# print('h = {0}, w = {1}, rot = {2}'.format(h, w, rot))


plt.xlim([0, 640])
plt.ylim([0, 480])
plt.savefig('1.png', format='png', dpi='figure')#, format = 'png')
plt.show()


for i in range(1000):
    ax.set_facecolor(gen.random_color())
    
    points, w, h, rot = gen.rect()

    xmin, ymin, lim_rect_w, lim_rect_h, ymax = gen.rect_lim(points)

    rect = Rectangle((points[0][0], points[0][1]), w, h, angle = rot, fc = gen.random_color())
    ax.add_patch(rect) 

    lim_rect = Rectangle((xmin, ymin), lim_rect_w, lim_rect_h, angle = 0, fill = None, ec = gen.random_color())
    ax.add_patch(lim_rect)

    plt.savefig(str(i) + '.png', format='png', dpi='figure', pad_inches=-1.0, bbox_inches=None)
    i += 1
    plt.clf()