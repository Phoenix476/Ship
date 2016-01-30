# -*- coding: utf-8 -*-
# Прежде чем переходить к следующему шагу, выполните 4 задания (Задания в коде в виде TODO)
import os

import pygame


def load_image(name, alpha_cannel):
    fullname = os.path.join('Images', name)  # Указываем путь к папке с картинками

    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


def move(event, x, y):
    print(event.key)
    # print("mod = ",event.mod)
    if event.key == 276:
        x -= 10
    if event.key == 273:
        y -= 10
    if event.key == 274:
        y += 10
    if event.key == 275:
        x += 10
    # TODO(complete): Задание-3 Дописать функцию, для движения объекта во все 4 стороны
    return x, y


pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна
x = 50
y = 50
ind = 0
color = [(0, 0, 0), (48, 213, 200), (100, 0, 0)]

screen = pygame.display.get_surface()  # определяем поверхность для рисования
# TODO(complete): Задание-2 Загрузить и отобразить на сцене ещё несколько произвольных картинок
image = load_image('skeleton.png', 1)  # загружаем картинку. Вторым аргументом указываем (есть/нет) альфа-канал
image_race_car = load_image('racecar.png', 1)
if image:
    done = False
else:
    done = True

while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            # TODO(complete): Задание-1 Дописать закрытие окна по нажатию клавиши Esc |
            # "K_ESCAPE" - константа клавиши Esc
            done = True
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_c:
                if ind >= len(color) - 1:
                    ind = -1
                ind += 1
            coords = move(e, x, y)
            x = coords[0]
            y = coords[1]

        if e.type == pygame.KEYUP:  # Событие "Клавиша отпущена"
            print('Key Up')
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            print('Mouse Down')
            # TODO: Задание-4 При нажатии кнопки "c" реализуйте изменение цвета фона по кругу
            # (бирюзовый, розовый, черный, бирюзовый ...)
    screen.fill(color[ind])
    screen.blit(image, (x, y))  # отрисовываем содержимое поверхности image на поверхность screen
    screen.blit(image_race_car, (340, 300))
    pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности