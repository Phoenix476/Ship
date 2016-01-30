# -*- coding: utf-8 -*-
# Рассмотрим стандартные принципы работы с объектами, которые отрисовываются графически
import sys
import pygame

from Utilities.loads import load_image

# Состояния объекта удобно задавать в виде констант. Если не понимаете в чем удобство, задавайте по своему!
STOP = 0
MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4


class Basic:
    def __init__(self, pos):
        self.image = load_image('2true_hare.png', alpha_cannel=True)
        self.rect = self.image.get_rect()
        self.pos = [pos[0], pos[1]]  # Позиция/кординаты объекта на экране
        self.speed = 2
        self.status = STOP  # Состояние объекта (меняется при нажатии кнопок на клавиатуре)

    def move(self):
        """
        Передвигаем объект
        """
        if self.status == MOVE_LEFT:
            self.pos[0] -= self.speed
        elif self.status == MOVE_RIGHT:
            self.pos[0] += self.speed

    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.status = MOVE_LEFT
            elif event.key == pygame.K_RIGHT:
                self.status = MOVE_RIGHT
        elif event.type == pygame.KEYUP:
            self.status = STOP

    def update(self):
        """
        Обновляем состояние(местоположение, угол поворота и т.п.) объекта
        Этот метод должен вызываться перед отрисовкой каждого кадра
        Как правило, из данного метода вызываются другие методы, которые изменяют нужное состояние объекта
        """
        if self.status != STOP:  # Если объект не стоит, то вызываем метод .move() чтобы передвинуть объект
            self.move()

    def render(self, screen):
        """
        Отрисовываем объект на поверхность screen
        """
        screen.blit(self.image, self.pos)


# Global Variables
FPS = 40
BACKGROUND_COLOR = (120, 50, 120)  # Цвет фона
RES_X, RES_Y = 400, 400  # размеры окна приложения

pygame.init()
display = pygame.display.set_mode((RES_X, RES_Y))
screen = pygame.display.get_surface()

demo_object = Basic((50, 50))
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        demo_object.event(e)  # Передаем все события объекту
        if e.type == pygame.MOUSEBUTTONDOWN:
            print('mouseX = ', e.pos[0], 'mouseY = ', e.pos[1])

    dt = clock.tick(FPS)
    demo_object.update()  # обновляем состояние объекта
    screen.fill(BACKGROUND_COLOR)
    demo_object.render(screen)  # отрисовываем объект
    pygame.display.flip()
