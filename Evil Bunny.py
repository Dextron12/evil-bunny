import pygame

#App cosntants
width, height = 1024, 648
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

class Game:
    running = True

    def __init__(self):
        self.running = True

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    width, height = event.w, event.h
            window.fill((135, 206, 235))

            pygame.display.flip()

program = Game()
program.main()


