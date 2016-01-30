import math
import sys

import pygame

from Classes.Tire import Tire


class Point:
    """
    Вспомогательный Класс для удобной работы с точками
    """

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def len(self, point_B):
        return math.sqrt((point_B.x - self.x) ** 2 + (point_B.y - self.y) ** 2)

    def as_tuple(self):
        return self.x, self.y


def points_on_line(point_A, point_B, step):
    """
    Делим отрезок AB на равные отрезки длиной step.
    Возвращает список промежуточных точек(их координат), между point_A и point_B.
    Включая первую точку, последняя точка в списке отсутствует.
    Если нужна и последняя точка, раскомментируйте строку.
    """
    point_A = Point(point_A)
    point_B = Point(point_B)
    if point_B.len(Point((0, 0))) < point_A.len(Point((0, 0))):
        point_A, point_B = point_B, point_A
    try:
        alpha = math.atan((point_B.y - point_A.y) / (point_B.x - point_A.x))
    except ZeroDivisionError:
        alpha = math.radians(90)
    l_AB = point_A.len(point_B)
    print(alpha)
    steps = 0
    points = [point_A.as_tuple()]
    k = 1
    while steps < l_AB - step:
        steps += step
        x = k * steps * math.cos(alpha) + point_A.x
        y = k * steps * math.sin(alpha) + point_A.y
        if point_B.len(Point((x, y))) > l_AB:  # fixme: костыль!
            k = -1
            x = k * steps * math.cos(alpha) + point_A.x
            y = k * steps * math.sin(alpha) + point_A.y
        points.append((x, y))
    # points.append(point_B.as_tuple())
    return points


def get_track(event):
    """
    Добавляет в список render_list объекты "шины".
    Объекты располагаются между координатами двух кликов мыши, на расстоянии len_step друг от друга
    """
    global new_track, render_list
    len_step = 40
    if new_track:
        new_track.append(event.pos)
        points = points_on_line(new_track[0], new_track[1], len_step)
        for point in points:
            render_list.append(Tire(point))
        new_track = []
    else:
        new_track.append(event.pos)


FPS = 40
screen = pygame.display.set_mode((800, 600))
render_list = []  # Список объеков, которые нужно отрисовывать на экране
new_track = []

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        # for obj in self.render_list:
        #    obj.event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            get_track(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    for render_obj in render_list:
        render_obj.render(screen)
        # render_obj.update()
    clock.tick(FPS)
    pygame.display.flip()