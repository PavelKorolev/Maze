import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, x_offset, y_offset, img):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.start = (x, y)
        self.stop = (x + x_offset, y + y_offset)
        self.direction_x = 1
        self.direction_y = 1

    def update(self):
        if self.rect.x >= self.stop[0]:
            self.rect.x = self.stop[0]
            self.direction_x = -1

        if self.rect.x <= self.start[0]:
            self.rect.x = self.start[0]
            self.direction_x = 1

        if self.rect.y >= self.stop[1]:
            self.rect.y = self.stop[1]
            self.direction_y = -1

        if self.rect.y <= self.start[1]:
            self.rect.y = self.start[1]
            self.direction_y = 1

        self.rect.x += self.direction_x * self.speed_x
        self.rect.y += self.direction_y * self.speed_y


def main():
    pass


if __name__ == "__main__":
    main()
