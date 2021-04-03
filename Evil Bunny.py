import pygame, os
from datetime import datetime

pygame.init()

#App cosntants
window = pygame.display.set_mode((1024, 648), pygame.RESIZABLE)
base_dir = os.getcwd()
mapPos = [256, 0]

def text(x, y, fg, font, size, msg, surface):
    font = pygame.font.SysFont(font, size)
    text = font.render(msg, True, fg)
    textRect = text.get_rect()
    textRect.center = (x,y)
    surface.blit(text, textRect)

class Inventory:
    
    def __init__(self):
        self.scroll = 0
        self.inventory = [] #0-8
        self.bar = pygame.Surface((288, 32), pygame.SRCALPHA, 32)

    def draw(self):
        self.bar.fill((49,49,49,150))
        for i in range(9):
            pygame.draw.rect(self.bar, (128,128,128), (i*32,0,32,32), 2)
        pygame.draw.rect(self.bar, (0, 0, 55), (self.scroll*32,0,32,32), 2)
        window.blit(self.bar, ((program.width/2)-144, program.height-42))

        #logic
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            self.scroll = 0
        if key[pygame.K_2]:
            self.scroll = 1
        if key[pygame.K_3]:
            self.scroll = 2
        if key[pygame.K_4]:
            self.scroll = 3
        if key[pygame.K_5]:
            self.scroll = 4
        if key[pygame.K_6]:
            self.scroll = 5
        if key[pygame.K_7]:
            self.scroll = 6
        if key[pygame.K_8]:
            self.scroll = 7
        if key[pygame.K_9]:
            self.scroll = 8

class Phone:

    def __init__(self):
        self.sprite = pygame.image.load(base_dir + "\\Resources\\Objects\\phone.png")
        self.open = False
        self.bg = pygame.Surface((68, 136))
        self.rawTime = datetime.now()

        #Load Apps
        self.msgIco = pygame.image.load(base_dir + "\\Resources\\Objects\\Apps\\message.png")
        self.emailIco = pygame.image.load(base_dir + "\\Resources\\Objects\\Apps\\email.png")
        self.phoneIco = pygame.image.load(base_dir + "\\Resources\\Objects\\Apps\\phone.png")
        self.radioIco = pygame.image.load(base_dir + "\\Resources\\Objects\\Apps\\radio.png")


    def draw(self):
        mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if self.open == False:
            self.bg.fill((0,0,0))
            if int(self.rawTime.hour) // 12 <= 0 or self.rawTime.hour == 12:
                text(34,18, (255,255,255), "Tahoma", 16, str(self.rawTime.hour) + ":" + str(self.rawTime.minute), self.bg)
            else:
                text(34,18, (255,255,255), "Tahoma", 16, str(self.rawTime.hour//12) + ":" + str(self.rawTime.minute), self.bg)
            window.blit(self.bg, ((program.width/2)+156, program.height-38))
            window.blit(self.sprite, ((program.width/2)+155, program.height-42))

            if (program.width/2)+226 > mouse[0] > (program.width/2)+156 and (program.height-38)+140 > mouse[1] > program.height-38:
                if click[0] == 1:
                    self.open = True
        if self.open == True:
            self.bg.fill((105,105,105))
            pygame.draw.rect(self.bg, (49,49,49), (0,116, 104, 42))
            self.bg.blit(self.phoneIco, (5, 118))
            self.bg.blit(self.msgIco, (26, 118))
            self.bg.blit(self.emailIco, (43, 118))
            self.bg.blit(self.radioIco, (5, 5))
            window.blit(pygame.transform.scale(self.bg, (105, 227)), (program.width-122, program.height-242))
            window.blit(pygame.transform.scale(self.sprite, (120,240)), (program.width-130, program.height-250))

            if (program.width-130)+120 > mouse[0] > program.width-130 and program.height-10 > mouse[1] > program.height-240:
                if click[0] == 1:
                    self.open = False
     
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
        self.hunger = 12
        self.halfHunger = False



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

        


    def update(self, mapPos):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            mapPos[1] += 32 * self.speed
            self.compass = 0
            self.walking = True
        elif key[pygame.K_s]:
            mapPos[1] -= 32 * self.speed
            self.compass = 180
            self.walking = True
        elif key[pygame.K_a]:
            mapPos[0] += 32 * self.speed
            self.compass = 270
            self.walking = True
        elif key[pygame.K_d]:
            mapPos[0] -= 32 * self.speed
            self.compass = 90
            self.walking = True
        else:
            self.walking = False

        """
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
            if round(self.pos[0]) - mapPos[0] > 600:
                mapPos[0] + 4
        elif key[pygame.K_a]:
            self.compass = 270
            self.pos[0] -= 32 * self.speed
            self.walking = True
        else:
            self.walking = False
            self.direction = 1


        print((round(self.pos[0]) - mapPos[0])//32)"""

    

class Game:
    running = True
    

    def __init__(self):
        self.width, self.height = 1024, 648
        self.running = True
        pygame.display.set_caption("Evil Bunny")
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 315)
        pygame.time.set_timer(pygame.USEREVENT+1, 20000)

        Grass = pygame.image.load("Resources\\Tiles\\Grass.png")
        Water = pygame.image.load("Resources\\Tiles\\Water.png")
        Dirt = pygame.image.load("Resources\\Tiles\\Dirt.png")
        Sand = pygame.image.load("Resources\\Tiles\\Sand.png")

        self.health = pygame.image.load("Resources\\Objects\\health.png")
        self.halfHealth = pygame.image.load("Resources\\Objects\\healthHalf.png")

        self.map = pygame.Surface((32*60, 32*40))
        for x in range(0,60):
            for y in range(0, 40):
                self.map.blit(Grass, (x*32,y*32))

    def main(self):

        player = Player((self.width//2), (self.height//2))
        phone = Phone()
        inventory = Inventory()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    program.width, program.height = event.w, event.h
                if player.walking == True:
                    if event.type == pygame.USEREVENT:
                        if player.direction == 0:
                            player.direction = 1
                        elif player.direction == 1:
                            player.direction = 2
                        elif player.direction == 2:
                            player.direction = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if inventory.scroll < 8:
                            inventory.scroll += 1
                        else:
                            inventory.scroll = 0
                    if event.button == 5:
                        if inventory.scroll > 0:
                            inventory.scroll -= 1
                        else:
                            inventory.scroll = 8
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if phone.open == True:
                            phone.open = False
                if event.type == pygame.USEREVENT+1:
                    if player.halfHunger == False:
                        player.hunger -= 1
                        player.halfHunger = True
                    elif player.halfHunger == True:
                        player.halfHunger = False

                    if player.hunger <= 4:
                        player.speed = 0.04
                    if player.hunger <= 2:
                        player.speed = player.speed = 0.02
                    if player.hunger == 0:
                        print("You dead")
            window.fill((135, 206, 235))

            window.blit(self.map, mapPos)

            player.draw()
            phone.draw()
            inventory.draw()

            #((program.width/2)-144, program.height-42))

            for i in range(player.hunger):
                window.blit(self.health, (((self.width//2)-144)+i*24, self.height-60))
            if player.halfHunger == True:
                window.blit(self.halfHealth, (((self.width//2)-144)+(i+1)*24, self.height-60))


            pygame.display.flip()
            player.update(mapPos)
            self.clock.tick(60)

program = Game()
program.main()


