import pygame, math

width,height = 800,600
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)

pygame.init()

class Textures:
    Grass = pygame.image.load("Resources\\Tiles\\Grass.png")
    Water = pygame.image.load("Resources\\Tiles\\Water.png")
    Dirt = pygame.image.load("Resources\\Tiles\\Dirt.png")
    Sand = pygame.image.load("Resources\\Tiles\\Sand.png")
    Texture_Tags = {"1" : Grass, "2" : Water, "3": Dirt, "4": Sand}
    Blocked_Tags = ["2"] # 0 being no defined tile
    Blocked = []
    def Blocked_At(pos):
        if list(pos) in Textures.Blocked:
            return True
        else:
            return False

class GUI:

     def Text(self,msg, x, y,w,h, colour, font, size,surf=screen):
        font = pygame.font.SysFont(font, size)
        textSurf = font.render(msg, True, colour)
        textRect = textSurf.get_rect()
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        surf.blit(textSurf, (textRect))
        
     def Button(self,msg, x, y, w, h, colour, ic, ac, font, size, args=None, event=None):
         mouse = pygame.mouse.get_pos()
         click = pygame.mouse.get_pressed()
         if x+w > mouse[0] > x and y+h > mouse[1] > y:
             pygame.draw.rect(screen, ac, (x,y,w,h))
             if click[0] == 1 and event != None:
                 if args != None:
                     event(args)
                 else:
                     event()
         else:
             pygame.draw.rect(screen, ic, (x,y,w,h))
         self.Text(self,msg,x,y,w,h,colour,font,size)
     def Switch(self,x,y,w,h,SwitchName,SwitchList,SwitchSize,DisabledColour,bg=(255,255,255)):
        mouse = pygame.mouse.get_pos()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if SwitchList.get(SwitchName) == False:
                        SwitchList[SwitchName] = True
                    else:
                        SwitchList[SwitchName] = False
        pygame.draw.rect(screen, bg, (x,y,w,h))
        if SwitchList.get(SwitchName) == False:
            pygame.draw.rect(screen, DisabledColour, (x+5,y+5,SwitchSize,h-10))
        return SwitchList

class Editor:

    def Load_Map(self,file):
        with open(file + ".map", "r") as mapfile:
            map_data = mapfile.read()

        map_data = map_data.split("-")

        map_size = map_data[len(map_data) - 1]
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0],map_size[1] = int(map_size[0]) * 32, int(map_size[1]) * 32
        tiles = []
        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))
        for tile in tiles:
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)
            tiles[tiles.index(tile)] = [pos[0] * 32, pos[1] * 32, tile[1]]

        tile_data = tiles
        return tile_data

    def Save_Map(self,file,tile_data):
        map_data = ""
        max_x,max_y = 0,0
        for t in tile_data:
            if t[0] >  max_x:
                max_x = t[0]
            if t[1] > max_y:
                max_y = t[1]
        for tile in tile_data:
            map_data = map_data + str(int(tile[0] / 32)) + "," + str(int(tile[1] / 32)) + ":" + tile[2] + "-"
        map_data = map_data + str(int(max_x / 32)) + "," + str(int(max_y / 32))
        with open(file + ".map", "w") as mapfile:
            mapfile.write(map_data)

        
    def Main(self,screen, width, height):
        map_height, map_width = 4,4
        camera_x, camera_y = 0,0
        selector = pygame.Surface((32, 32), pygame.HWSURFACE|pygame.SRCALPHA)
        selector.fill((0,0,255,100))
        pygame.display.set_caption("Fallen Planets Editor")
        tile_data = []
        text = []
        pygame.mouse.set_pos(0,0)
        filename = "Earth"
    ##        while True: # USED FOR USER MAP DIMENSIONS
    ##            for event in pygame.event.get():
    ##                if event.type == pygame.QUIT:
    ##                    pygame.quit()
    ##                    quit()
    ##                if event.type == pygame.KEYDOWN:
    ##                    if event.key == pygame.K_0:
    ##                        text.append("0")
    ##                    if event.key == pygame.K_1:
    ##                        text.append("1")
    ##                    if event.key == pygame.K_2:
    ##                        text.append("2")
    ##                    if event.key == pygame.K_3:
    ##                        text.append("3")
    ##                    wtext = text.join("")
    ##                    print(wtext)
    ##                if event.type == pygame.VIDEORESIZE:
    ##                    screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
    ##            screen.fill((0,0,255))
    ##            pygame.draw.rect(screen, (255,255,255), (200, 100, size[0]- 400, size[1] - 200))
    ##            pygame.draw.rect(screen, (0,0,0), (285,150,size[0] - 500, 50), 2)
    ##            GUI.Text(GUI,"Width", size[0] - 600, 160,100,30, (0,0,0), 'Arial', 30)
    ##            pygame.display.flip()
        map_width = input("Map Width: ")
        map_height = input("Map Height: ")
        dt = input("Default Tile: ")
        filename = input("Map Name: ")
        mouse_x, mouse_y = 0,0
        if dt == "":
            dt = "1"
            for x in range(0, int(map_width)*32, 32):
                for y in range(0, int(map_height)*32, 32):
                    tile_data.append([x,y,dt])
        brush = "1"
        while True:
            click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_x = math.floor(mouse_pos[0] / 32) * 32
                    mouse_y = math.floor(mouse_pos[1] / 32) * 32
##                if event.type == pygame.MOUSEBUTTONDOWN:
##                    tile = [mouse_x - camera_x, mouse_y - camera_y, brush] # keep this as a list
##
##                    found = False
##                    for t in tile_data:
##                        if t[0] == tile[0] and t[1] == tile[1]:
##                            found = True
##                            break
##                    if not found:
##                        if not brush == "r":
##                            tile_data.append(tile)
##                    else:
##                        if brush == "r":
##                            for t in tile_data:
##                                if t[0] == tile[0] and t[1] == tile[1]:
##                                    tile_data.remove(t)
            if click[0] == 1:
                tile = [mouse_x - camera_x, mouse_y - camera_y, brush]
                print(mouse_x, camera_x)
                found = False
                for t in tile_data:
                    if t[0] == tile[0] and t[1] == tile[1]:
                       found = True
                       break
                if not found:
                    if not brush == "r":
                        tile_data.append(tile)
                else:
                    if brush == "r":
                        for t in tile_data:
                            if t[0] == tile[0] and t[1] == tile[1]:
                                tile_data.remove(t)
            if brush == "r":
                selector.fill((255,0,0,100)) # fills red if removing tile
            else:
                selector.fill((65,105,225,100)) # fills selector brush roal blue
            key = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            if key[pygame.K_w] or key[pygame.K_UP]:
                camera_y += 32
            elif key[pygame.K_s] or key[pygame.K_DOWN]:
                camera_y -= 32
            elif key[pygame.K_a] or key[pygame.K_LEFT]:
                camera_x += 32
            elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                camera_x -= 32

            if key[pygame.K_r]:
                brush = "r"
            if key[pygame.K_F1]:
                self.Save_Map(self,filename,tile_data)
            if key[pygame.K_F2]:
                  tile_data = self.Load_Map(self,filename)
            if key[pygame.K_F3]:
                brush = input("Brush Tag: ")
            if key[pygame.K_ESCAPE]:
                break
            screen.fill((0,0,255))
            for tile in tile_data:
                screen.blit(Textures.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
            screen.blit(selector, (mouse_x, mouse_y))
            GUI.Text(GUI,"F1 = Save Map", 15,0,80,20, (0,255,0), "Arial", 20)
            GUI.Text(GUI,"F2 = Load Map", 15,30,80,20, (0,255,0), "Arial", 20)
            GUI.Text(GUI,"F3 = Change Brush", 15,60,100,20, (0,255,0), "Arial", 20)
            pygame.display.flip()

Editor.Main(Editor,screen,width,height)
