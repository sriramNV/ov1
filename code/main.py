from settings import *
from level import Level
from pytmx.util_pygame import load_pygame


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("project-ov1")

        self.tmx_maps = {0: load_pygame("../data/levels/omni.tmx")}
        print(self.tmx_maps)

        self.current_stage = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
