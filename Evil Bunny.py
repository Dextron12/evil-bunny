import pygame, os

#App cosntants
width, height = 1024, 648
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
base_dir = os.getcwd()

class Player:

    def __init__(self, x, y):
        self.sprite = pygame.image.load(base_dir + "\\Resources\\Sprites\\bunny.png")

        self.nBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\northBunny.png")
        self.neBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\neBunny.png")
        self.sBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\southBunny.png")
        self.seBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\seBunny.png")
        self.eBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\eastBunny.png")
        self.wBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\westBunny.png")
        self.swBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\swBunny.png")
        self.nwBunny = pygame.image.load(base_dir + "\\Resources\\Sprites\\nwBunny.png")

        self.pos = [x, y]
        self.direction = 1 #0: walk anim, 1: still anim, 2: waml2 anim
        self.walking = False
        self.compass = 0
        self.speed = 0.08

    def draw(self):
        if self.compass == 0:
            window.blit(self.nBunny, self.pos, (self.direction*32, 0, 32, 32))
        if self.compass == 90:
            window.blit(self.eBunny, self.pos, (self.direction*32, 0, 32, 32))
        if self.compass == 180:
            window.blit(self.sBunny, self.pos, (self.direction*32, 0, 32, 32))
        if self.compass == 270:
            window.blit(self.wBunny, self.pos, (self.direction*32, 0, 32, 32))

        if self.compass == 45: #NE
            window.blit(self.neBunny, self.pos, (self.direction*30, self.direction*32, 32, 32))
        if self.compass == 135: #SE
            window.blit(self.seBunny, self.pos, (self.direction*29, self.direction*32, 32, 32))
        if self.compass == 225: #SW
            window.blit(self.swBunny, self.pos, (self.direction*30.6, self.direction*32, 32, 32))
        if self.compass == 315: # NW
            window.blit(self.nwBunny, self.pos, (self.direction*30, self.direction*32, 32, 32))

        


    def update(self):
        key = pygame.key.get_pressed()

        #North
        if key[pygame.K_w]:
            if key[pygame.K_d]: #NE
                self.compass = 45
                self.pos[0] += 32 * self.speed
                self.pos[1] -= 32 * self.speed
            elif key[pygame.K_a]: #NW
                self.compass = 315
                self.pos[0] -= 32 * self.speed
                self.pos[1] -= 32* self.speed
            else:
                self.compass = 0
                self.pos[1] -= 32 * self.speed
            self.walking = True
        
        elif key[pygame.K_s]:
            if key[pygame.K_a]:
                self.compass = 225 #SW
                self.pos[0] -= 32 * self.speed
                self.pos[1] += 32 * self.speed
            elif key[pygame.K_d]:
                self.compass = 135 #SE
                self.pos[0] += 32 * self.speed
                self.pos[1] += 32 * self.speed
            else:
                self.compass = 180
                self.pos[1] += 32 * self.speed
            self.walking = True

        elif key[pygame.K_d]:
            self.compass = 90
            self.pos[0] += 32 * self.speed
            self.walking = True
        elif key[pygame.K_a]:
            self.compass = 270
            self.pos[0] -= 32 * self.speed
            self.walking = True
        else:
            self.walking = False
            self.direction = 1
    

class Game:
    running = True

    def __init__(self):
        self.running = True
        pygame.display.set_caption("Evil Bunny")
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 315)

        Grass = pygame.image.load("Resources\\Tiles\\Grass.png")
        Water = pygame.image.load("Resources\\Tiles\\Water.png")
        Dirt = pygame.image.load("Resources\\Tiles\\Dirt.png")
        Sand = pygame.image.load("Resources\\Tiles\\Sand.png")

        self.map = pygame.Surface((32*60, 32*40))
        for x in range(0,60):
            for y in range(0, 40):
                self.map.blit(Grass, (x*32,y*32))

    def main(self):
        mapPos = (0,0)

        player = Player(32,64)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    width, height = event.w, event.h
                if player.walking == True:
                    if event.type == pygame.USEREVENT:
                        if player.direction == 0:
                            player.direction = 1
                        elif player.direction == 1:
                            player.direction = 2
                        elif player.direction == 2:
                            player.direction = 0
            window.fill((135, 206, 235))

            window.blit(self.map, mapPos)

            player.draw()

            pygame.display.flip()
            player.update()
            self.clock.tick(60)

program = Game()
program.main()


