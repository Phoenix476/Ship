# -*- coding: utf-8 -*-
import pygame

pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна

done = False
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

"""
QUIT	     none
ACTIVEEVENT	     gain, state
KEYDOWN	     unicode, key, mod
KEYUP	     key, mod
MOUSEMOTION	     pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT        code
"""
