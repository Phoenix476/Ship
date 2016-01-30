import pygame
import sys
from Classes.Vector import Vector


FPS = 40
NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
COMEBACK = 3
SPEED_DOWN = 4
SPEED_UP = 5


class SpaceShip:
    def __init__(self, position):
        self.default_position = Vector(position)  # Стандартная позиция (центр экрана_
        self.position = Vector(position)        # Вектор позиции объекта
        self.speed = Vector((3, 0))     # Вектор скорости
        self.speed_rotate = 10      # Угол поворота вектора скорости
        self.image = pygame.Surface((30, 50))     # Поверхность, где будет отрисовываться объект
        self.state = NORMAL
        self.draw()

    def update(self):
        # Функция обновляет позицию объекта на экране
        # # Заставляет пролетать объект сквозь границы окна
        if self.position.as_point()[0] > 801:
            self.position = Vector((0, self.position.as_point()[1]))
        if self.position.as_point()[1] > 601:
            self.position = Vector((self.position.as_point()[0], 0))
        if self.position.as_point()[1] < -1:
            self.position = Vector((self.position.as_point()[0], 599))
        if self.position.as_point()[0] < -1:
            self.position = Vector((799, self.position.as_point()[1]))
        # # Поворот объекта
        if self.state == TURN_LEFT:
            self.speed.rotate(-self.speed_rotate)
        if self.state == TURN_RIGHT:
            self.speed.rotate(self.speed_rotate)
        # # Ускорение и замедление объкта
        if self.state == SPEED_DOWN:
            self.speed = self.speed - self.speed.normalize()
        if self.state == SPEED_UP:
            self.speed = self.speed + self.speed.normalize()
        # # Возвращение объекта в центр экрана
        if self.state == COMEBACK:
            self.position = self.default_position

        self.position += self.speed

    def events(self, event):
        # События
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
            if event.key == pygame.K_SPACE:
                self.state = COMEBACK
            if event.key == pygame.K_DOWN:
                self.state = SPEED_DOWN
            if event.key == pygame.K_UP:
                self.state = SPEED_UP
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def draw(self):
        # Отрисовывает корабль на поверхности
        pygame.draw.lines(self.image, (255, 255, 255), False, [(2, 2), (12, 10), (26, 13),
                                                               (12, 17), (2, 24), (2, 16),
                                                               (7, 13), (2, 10), (2, 2)])

    def render(self, screen):
        # Вывод изображения на экран
        origin_rect = self.image.get_rect()
        rotate_image = pygame.transform.rotate(self.image, self.speed.angle)
        rotate_rect = rotate_image.get_rect()
        rotate_rect.center = origin_rect.center
        rotate_rect.move_ip(self.position.as_point())
        screen.blit(rotate_image, rotate_rect)
        screen.blit(rotate_image, rotate_rect)
        # pygame.draw.line(screen, (0, 255, 0), self.position.as_point(), (self.position + self.speed*5).as_point())


pygame.init()
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
space_ship = SpaceShip((400, 300))
clock = pygame.time.Clock()
while True:
    for e in pygame.event.get():
        space_ship.events(e)
        if e.type == pygame.QUIT:
            sys.exit()
    clock.tick(FPS)
    space_ship.update()
    screen.fill((0, 0, 0))
    space_ship.render(screen)
    pygame.display.flip()
