# -*- coding: utf-8 -*-
import pygame

pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна

done = False
while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            done = True
