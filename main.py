import pygame
import random
import os
# this is for initializing 
pygame.init()
pygame.display.set_caption("No Man Space")
running = True
WIDTH = 1600
HIEGHT= 900
FPS = 240
#color
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
Life=3 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HIEGHT))
background_img = pygame.image.load(os.path.join("images", "background.png")).convert()
bullet_img = pygame.image.load(os.path.join("images", "bullet.png")).convert()
player_img = pygame.image.load(os.path.join("images", "player.jpg")).convert()
rock_img = pygame.image.load(os.path.join("images", "rock.png")).convert()
#this is for player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25.5
        #pygame.draw.circle(self.image , RED, self.rect.center, self.radius)
        self.rect.center =(WIDTH/2,HIEGHT/2)
        self.speedx = 5

    #this is for control

    def update(self):
        key_pressed= pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x +=self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -=self.speedx
        if key_pressed[pygame.K_w]:
            self.rect.y -=self.speedx
        if key_pressed[pygame.K_s]:
            self.rect.y +=self.speedx
        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.top < 0 :
            self.rect.top = 0
        if self.rect.bottom > HIEGHT :
            self.rect.bottom = HIEGHT
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
#this is rock
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        swh = random.randrange(30,70)
        self.image = pygame.transform.scale(rock_img,(swh,swh))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        #pygame.draw.circle(self.image , RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.rect.center =(self.rect.x,self.rect.y)
        self.speedy = random.randrange(1,10)


    def update(self):
       self.rect.y += self.speedy
       if self.rect.top > HIEGHT or self.rect.left > WIDTH or self.rect.left <0 :
        self.rect.x = random.randrange(0,WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,10)   
#this is for bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img,(40,60))
        self.image.set_colorkey(BLACK)      
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x 
        self.speedy = -10
    def update(self):
       self.rect.y += self.speedy
       if self.rect.bottom < 0:
            self.kill()
all_sprites = pygame.sprite.Group()
player = Player()
rock = Rock()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player)
for i in range (8):
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)
# this is for running
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets ,True,True)
    for hit in hits:
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)
    hits = pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle)
    if hits:
        running=False
    #display
    screen.fill(BLACK)
    screen.blit(background_img, (0,0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()