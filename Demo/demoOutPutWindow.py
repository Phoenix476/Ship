# -*- coding: utf-8 -*-
# Демонстрация использования окна для вывода значений свойств объектов

import sys

import pygame

from Classes.OutPutWindow import OutPutWindow
from Classes.Units import BlueMan


# глобальные переменные (Global Variables)
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # Цвет фона
RES_X, RES_Y = 400, 400  # размеры окна приложения

pygame.init()  # инициализация
display = pygame.display.set_mode((RES_X, RES_Y))  # создание окна
screen = pygame.display.get_surface()  # получаем поверхность для рисования

trace = OutPutWindow(coords=(10, 10), font_color=(0, 0, 250), font_size=22)  # Создаем окно
first_unit = BlueMan(50, 50)

# Например, я хочу отслеживать свойства x,y и speed объекта first_unit
trace.add_attr(first_unit, "x")
trace.add_attr(first_unit, "y")
trace.add_attr(first_unit, "speed")

clock = pygame.time.Clock()  # Создаем таймер для контроля фпс

while True:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:
            sys.exit()  # Закрытие окна программы
        if e.type == pygame.KEYDOWN or e.type == pygame.KEYUP:
            first_unit.handle_event(e)  # Передаем события объекту, для обработки

    dt = clock.tick(FPS)  # Устанавливаем FPS
    screen.fill(BACKGROUND_COLOR)  # Очищаем экран
    first_unit.update(dt)  # Обновляем состояние объекта
    first_unit.render(screen)  # Отрисовываем объект на экране
    trace.render(screen)  # Не забываем отрисовать наше Окно
    pygame.display.flip()  # отображаем на мониторе все, что нарисовали на экране
