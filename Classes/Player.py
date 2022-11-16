import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img, award_sound):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.award_sound = award_sound

        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.coins = None
        self.collected_coins = 0

        self.enemies = pygame.sprite.Group()

        self.alive = True

    def update(self):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        coins_hit_list = pygame.sprite.spritecollide(self, self.coins, False)
        for coin in coins_hit_list:
            self.collected_coins += 1
            self.award_sound.play()
            coin.kill()

        if pygame.sprite.spritecollide(self, self.enemies, False):
            self.alive = False


def main():
    pass


if __name__ == "__main__":
    main()