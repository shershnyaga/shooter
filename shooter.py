from pygame import *
from random import*
scr = display.set_mode((700,500))
background = transform.scale(image.load("galaxy.jpg"),(700,500))
hero = transform.scale(image.load("hero.png"),(200,200))
Enemy = transform.scale(image.load("zlod.png"),(200,200))
Enemy1 = transform.scale(image.load("zlod.png"),(200,200))
Enemy2 = transform.scale(image.load("zlod.png"),(200,200))
Enemy3 = transform.scale(image.load("zlod.png"),(200,200))
mixer.init()
mixer.music.load('space.ogg')
game = True
clock = time.Clock()
FPS = 60

class obiekt(sprite.Sprite):
    def __init__(self,picimage, sx,sy, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(picimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = sx 
        self.rect.y = sy
    def reset(self):
        scr.blit(self.image, (self.rect.x,self.rect.y))
        



n = 0
class igrok(obiekt):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT]:
            self.rect.x += 5
        if keys_pressed[K_UP]:
            self.rect.y -= 5
        if keys_pressed[K_DOWN]:
            self.rect.y += 5
        if keys_pressed[K_SPACE]:
            
            global n
            ammo[n].rect.x = self.rect.x
            ammo[n].rect.y = self.rect.y
            n+= 1
            if n>len(ammo)-1:
                n = 0


GEROI = igrok("hero.png", 100,150, 150)

class Enemy(obiekt):
    def update(self):
            if self.rect.y <500:
                self.rect.y += self.speed
            else:
                self.rect.y =0
                self.rect.x=randint(1,500)
        
E1 = Enemy("zlod.png",50 ,50,3)
E2 = Enemy("zlod.png",50 ,50,3)
E3 = Enemy("zlod.png",50 ,50,3)
E4 = Enemy("zlod.png",50 ,50,3)

class bullet(obiekt):
    def fire(self):
            if self.rect.y >0:
                self.rect.y-= self.speed
            else:
                self.rect.y = -100

b1 = bullet("bullet.png", -50,-50,5)
b2 = bullet("bullet.png", -50,-50,5)
b3 = bullet("bullet.png", -50,-50,5)
b4 = bullet("bullet.png", -50,-50,5)
b5 = bullet("bullet.png", -50,-50,5)

ammo = [b1,b2,b3,b4,b5]

 

font.init()
font1 = font.Font(None,50)
ochki = 0
while game:
    for i in ammo:
        i.reset()
        i.fire()
    scr.blit(background,(0,0))
    txt = "Очки"+str(ochki)
    text = font1.render(txt,1,(255,0,0))
    scr.blit(text,(10,20))
    if sprite.collide_rect(E1,b1):
        E1.rect.y=-50
        E1.rect.x=randint(1,500)

        
        
    kick = mixer.Sound('fire.ogg')
    #scr.fill((50,50,150))
    scr.blit(background,(0,0))
    #scr.blit(hero,(x1,y1))
    GEROI.reset()
    #scr.blit(hero,(x1,y1))
    for e in event.get():
        if e.type ==    QUIT:
            game = False
    
    GEROI.reset()
    GEROI.update()
    E1.reset()
    E1.update()
    E2.reset()
    E2.update()
    E3.reset()
    E3.update()
    E4.reset()
    E4.update()
    b1.reset()
    b1.fire()
    b2.reset()
    b2.fire()
    b3.reset()
    b3.fire()
    b4.reset()
    b4.fire()
    b5.reset()
    b5.fire()

#  if mob.rect.right > player.rect.left and \
# mob.rect.left < player.rect.right and \
# mob.rect.bottom > player.rect.top and \
# mob.rect.top < player.rect.bottom:
#     collide = True
    

    display.update()
    clock.tick(FPS)
    #winscreen = transform.scale(image.load("you won.jpg"))
    display.update()
    clock.tick(FPS)
    #kick.play()
