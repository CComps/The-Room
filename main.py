import pygame
import sys


class Player(object):
    def __init__(self):
        self.image = pygame.image.load("images/player.png")
        self.position = [640, 400]  # World coordinates
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

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, surf, camera_pos):
        # Draw the player at its position relative to the camera
        draw_pos = [self.position[0] - camera_pos[0], self.position[1] - camera_pos[1]]
        surf.blit(self.image, draw_pos)


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
        pygame.display.set_caption("The Room")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.camera_pos = [0, 0]  # Camera's position in the world

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

            # Update the camera position to center on the player
            self.camera_pos[0] = self.player.position[0] - self.screen.get_width() // 2
            self.camera_pos[1] = self.player.position[1] - self.screen.get_height() // 2

            self.screen.fill([255, 255, 255])
            self.player.draw(self.screen, self.camera_pos)
            pygame.display.update()

        pygame.quit()
        sys.exit()


g = Game()
g.run()
