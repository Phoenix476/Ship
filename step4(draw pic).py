# -*- coding: utf-8 -*-
import os
import pygame


def load_image(name, alpha_cannel):
    fullname = os.path.join('Images', name)  # Указываем путь к папке с картинками

    try:
        image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    except pygame.error:  # Если картинки нет на месте
        print("Cannot load image:", name)
        return 0
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image = load_image('skeleton.png', 1)  # загружаем картинку. Вторым аргументом указываем (есть/нет) альфа-канал
print(type(image))

if image:
    done = False
else:
    done = True

while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            done = True
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
            # тут можно вызвать функцию, которая обработает это событие
        if e.type == pygame.KEYUP:  # Событие "Клавиша отпущена"
            print('Key Up')
            # тут можно вызвать функцию, которая обработает это событие
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            print('Mouse Down')
            # тут можно вызвать функцию, которая обработает это событие
    screen.blit(image, (50, 50))  # отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности