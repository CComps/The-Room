import pygame
import os


class Player(object):
    def __init__(self):
        self.image = pygame.image.load("images/player.png")
        self.center = [640, 400]
        self.velocity = [0, 0]
        self.max_speed = 10
        self.acceleration = 0.1
        self.deceleration = 0.3

    def move(self, move_x, move_y):
        if move_x != 0:
            self.velocity[0] += move_x * self.acceleration
            if self.velocity[0] > self.max_speed:
                self.velocity[0] = self.max_speed
            elif self.velocity[0] < -self.max_speed:
                self.velocity[0] = -self.max_speed
        else:
            if self.velocity[0] > 0:
                self.velocity[0] -= self.deceleration
                if self.velocity[0] < 0:
                    self.velocity[0] = 0
            elif self.velocity[0] < 0:
                self.velocity[0] += self.deceleration
                if self.velocity[0] > 0:
                    self.velocity[0] = 0

        if move_y != 0:
            self.velocity[1] += move_y * self.acceleration
            if self.velocity[1] > self.max_speed:
                self.velocity[1] = self.max_speed
            elif self.velocity[1] < -self.max_speed:
                self.velocity[1] = -self.max_speed
        else:
            if self.velocity[1] > 0:
                self.velocity[1] -= self.deceleration
                if self.velocity[1] < 0:
                    self.velocity[1] = 0
            elif self.velocity[1] < 0:
                self.velocity[1] += self.deceleration
                if self.velocity[1] > 0:
                    self.velocity[1] = 0

        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def draw(self, surf):
        surf.blit(self.image, self.center)


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
        pygame.display.set_caption("The Room")
        self.clock = pygame.time.Clock()
        self.player = Player()

    def run(self):
        running = 1
        while running:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE
                    )

            keys = pygame.key.get_pressed()
            move_x = keys[pygame.K_d] - keys[pygame.K_a]
            move_y = keys[pygame.K_s] - keys[pygame.K_w]
            self.player.move(move_x, move_y)

            self.screen.fill([255, 255, 255])
            self.player.draw(self.screen)
            pygame.display.update()


g = Game()
g.run()
