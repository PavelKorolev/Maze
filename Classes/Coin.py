import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def main():
    pass


if __name__ == "__main__":
    main()
