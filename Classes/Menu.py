import pygame


class Menu:
    def __init__(self, options):
        self.options = options

    def render(self, surface, current_font, active_option):
        """
        options:
        (x, y)
        (option_offset_x, option_offset_y)
        name
        color
        active_color
        number
        """
        for i in self.options:
            if active_option == i[5]:
                color_to_render = i[4]
            else:
                color_to_render = i[3]
            surface.blit(current_font.render(i[2], 1, color_to_render), (i[0], i[1]))
            pygame.draw.rect(surface, color_to_render, pygame.Rect(i[0][0], i[0][1], i[1][0], i[1][1]), 5)

    def start(self, menu, screen, MENU_BACKGROUND):
        cycle_done = True
        menu_font = pygame.font.SysFont("Arial", 90, True)
        option = 0
        while cycle_done:
            menu.fill(MENU_BACKGROUND)

            mp = pygame.mouse.get_pos()
            for i in self.options:
                if mp[0] in range(i[0][0], i[0][0] + i[1][0]) and mp[1] in range(i[0][1], i[0][1] + i[1][1]):
                    option = i[5]
            self.render(menu, menu_font, option)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        pygame.quit()
                    if e.key == pygame.K_UP:
                        if option > 0:
                            option -= 1
                    if e.key == pygame.K_DOWN:
                        if option < len(self.options) - 1:
                            option += 1

                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if option == 0:
                        cycle_done = False
                    if option == 1:
                        pygame.quit()

            screen.blit(menu, (0, 0))
            print(pygame.mouse.get_pos())
            pygame.display.flip()


def main():
    pass


if __name__ == "__main__":
    main()
