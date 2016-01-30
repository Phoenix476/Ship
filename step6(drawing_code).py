# -*- coding: utf-8 -*-
# Рисуем на экране кодом. Документация тут: http://www.pygame.org/docs/ref/draw.html
import sys
import pygame


def draw(surf):
    """
    Рисуем на поверхности с помощью методов/функция pyGame
    """
    pygame.draw.circle(surf, (200, 0, 0), (20, 20), 10)  # Рисуем круг(цвет, координаты центра, радиус).
    # Обратите внимание! Мы рисуем на переданной поверхности surf, относительно её левого верхнего угла

    # Рисуем синие линии. Последним аргументом передаем список пар координат точек
    pygame.draw.lines(surf, (0, 0, 200), False, [(150, 200), (150, 150), (200, 100), (250, 150)])

    # Рисуем зеленую дугу. Подробнее об аргументах смотрите в документации pyGame
    pygame.draw.arc(surf, (0, 250, 0), (40, 40, 130, 50), 0, 3, 2)


# глобальные переменные (Global Variables)
FPS = 40
BACKGROUND_COLOR = (120, 50, 120)  # Цвет фона
RES_X, RES_Y = 400, 400  # размеры окна приложения

pygame.init()  # инициализация
display = pygame.display.set_mode((RES_X, RES_Y))  # создание окна
screen = pygame.display.get_surface()  # получаем поверхность для рисования

# drawing_surf = pygame.Surface((200, 200))  # Создаем пустую поверхность (на ней и будем рисовать)
drawing_surf = pygame.Surface((200,200), pygame.SRCALPHA) #Так можно создать поверхность с прозрачным фоном

draw(drawing_surf)
clock = pygame.time.Clock()  # Создаем таймер для контроля фпс

while True:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:
            sys.exit()  # Закрытие окна программы

    dt = clock.tick(FPS)  # Устанавливаем FPS
    screen.fill(BACKGROUND_COLOR)  # Очищаем экран
    screen.blit(drawing_surf, (0, 0))
    pygame.display.flip()  # отображаем на мониторе все, что нарисовали на экране

"""
Полный список всех фигур, которые можно рисовать(скопировано из документации):
pygame.draw.rect	—	draw a rectangle shape
pygame.draw.polygon	—	draw a shape with any number of sides
pygame.draw.circle	—	draw a circle around a point
pygame.draw.ellipse	—	draw a round shape inside a rectangle
pygame.draw.arc	—	    draw a partial section of an ellipse
pygame.draw.line	—	draw a straight line segment
pygame.draw.lines	—	draw multiple contiguous line segments
pygame.draw.aaline	—	draw fine antialiased lines
pygame.draw.aalines	—	draw a connected sequence of antialiased lines
"""