# -*- coding: utf-8 -*-
# Демонстрация движения анимированного объекта

import pygame, sys
from Classes.Units import BlueMan

# глобальные переменные (Global Variables)
FPS = 400
BACKGROUND_COLOR = (0, 100, 100)  # Цвет фона
RES_X, RES_Y = 400, 400  # размеры окна приложения

pygame.init()  # инициализация
display = pygame.display.set_mode((RES_X, RES_Y))  # создание окна
screen = pygame.display.get_surface()  # получаем поверхность для рисования

first_unit = BlueMan(50, 50)  # Создаем объект
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
    pygame.display.flip()  # отображаем на мониторе все, что нарисовали на экране
