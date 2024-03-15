
import pygame 
import random
import time 

COLOR = (255, 100, 98) 
SURFACE_COLOR = (167, 255, 100) 
WIDTH = 500
HEIGHT = 500
class Particle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = size
        self.color = color
        self.lifetime = 3  

       
        self.vel_x = random.randint(-3, 3)
        self.vel_y = random.randint(-3, 3)
        def update(self):
        
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.kill() 

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 


    def moveRight(self, pixels):
        self.rect.x += pixels
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
    def moveBack(self,speed):
        self.rect.y -= speed * speed/10


class Weapon(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y, velocity):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity

    def update(self):
        self.rect.y -= self.velocity

pygame.init() 
  
RED = (255, 0, 0) 
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Test Game") 
  
all_sprites_list = pygame.sprite.Group() 
particle_sprites_list = pygame.sprite.Group() 

object_ = Sprite(RED, 20, 30) 
object_.rect.x = 200
object_.rect.y = 300

def spawn_enemies():
    global all_sprites_list
    for _ in range(5):
        enemy = Sprite(BLUE, 20, 30)
        enemy.rect.x = random.randint(0, WIDTH - 30)
        enemy.rect.y = random.randint(-100, -50)
        all_sprites_list.add(enemy)

spawn_enemies()

enemie_WIDTH = 30
enemie_HEIGHT = 20

enemie2_WIDTH = 30
enemie2_HEIGHT = 20

enemie3_WIDTH = 30
enemie3_HEIGHT = 20

enemie4_WIDTH = 30
enemie4_HEIGHT = 20

enemie5_WIDTH = 30
enemie5_HEIGHT = 20


enemie_ = Sprite(BLUE, enemie_HEIGHT, enemie_WIDTH)
enemie_.rect.x = 0
enemie_.rect.y = 0



enemie2_ = Sprite(BLUE, enemie2_HEIGHT, enemie2_WIDTH)
enemie2_.rect.x = 300
enemie2_.rect.y = 0

enemie3_ = Sprite(BLUE, enemie3_HEIGHT, enemie3_WIDTH)
enemie3_.rect.x = 400
enemie3_.rect.y = 0

enemie4_ = Sprite(BLUE, enemie4_HEIGHT, enemie4_WIDTH)
enemie4_.rect.x = 200
enemie4_.rect.y = 0

enemie5_ = Sprite(BLUE, enemie4_HEIGHT, enemie4_WIDTH)
enemie5_.rect.x = 500
enemie5_.rect.y = 0

all_sprites_list.add(object_) 
all_sprites_list.add(enemie_)
all_sprites_list.add(enemie2_)
all_sprites_list.add(enemie3_)
all_sprites_list.add(enemie4_)
all_sprites_list.add(enemie5_)

fonts = pygame.font.SysFont('freesansbold.ttf', 32)
score = 0
Score_text = fonts.render('Score: ' + str(score),  True, (0,0,0))
Score_Text_rect = Score_text.get_rect()
Score_Text_rect.center = ((245,20))

end = fonts.render(' You lose Womp womp', True, (255,255,255))
end_rect = end.get_rect()
end_rect.center  = ((245,100))

win = fonts.render(' You Win yay!', True, (255,255,255))
win_rect = win.get_rect()
win_rect.center = end_rect.center  = ((245,100))

exit = True
clock = pygame.time.Clock() 


weapons_list = pygame.sprite.Group()
WEAPON_COLOR = (255, 255, 255)
weapon_width = 5
weapon_height = 10
weapon_velocity = 10


while exit: 

    
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
            elif event.key == pygame.K_w:
               
                weapon = Weapon(WEAPON_COLOR, weapon_height, weapon_width, object_.rect.centerx, object_.rect.y, weapon_velocity)
                weapons_list.add(weapon)
                
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        object_.moveRight(10)
    if keys[pygame.K_DOWN]:
        object_.moveForward(10)
    if keys[pygame.K_UP]:
        object_.moveBack(10)
    
    weapons_list.update()
    for weapon in weapons_list.copy():
        if weapon.rect.y < 0:
            weapons_list.remove(weapon)
        else:
            
            enemies_hit = pygame.sprite.spritecollide(weapon, all_sprites_list, False)
            for enemy in enemies_hit:
                if enemy != object_:  
                     for _ in range(1):  
                        particle = Particle((255, 255, 0), enemy.rect.x, enemy.rect.y, 5)
                        particle_sprites_list.add(particle)
                        all_sprites_list.remove(enemy)
                        weapons_list.remove(weapon)
                        print("Enemy hit!")  
                        score += 1
                        Score_text = fonts.render('Score: ' + str(score),  True, (0,0,0))
                        spawn_enemies()
    
    particle_sprites_list.update()
    
    if score == 5:
        screen.fill(BLACK) 
        screen.blit(win,win_rect)
        all_sprites_list.remove(object_)
        pygame.display.flip() 
        time.sleep(3)
        break
    if enemie2_.rect.colliderect(object_.rect):
         screen.fill(BLACK) 
         screen.blit(end,end_rect)
         all_sprites_list.remove(object_)
         pygame.display.flip() 
         time.sleep(3)
         break
   
    
    if enemie3_.rect.colliderect(object_.rect):
        screen.fill(BLACK) 
        screen.blit(end,end_rect)
        all_sprites_list.remove(object_)
        pygame.display.flip() 
        time.sleep(3)
        break
    
    
    if enemie4_.rect.colliderect(object_.rect):
        screen.fill(BLACK) 
        screen.blit(end,end_rect)
        all_sprites_list.remove(object_)
        pygame.display.flip() 
        time.sleep(3)
        break
   
    
    if enemie5_.rect.colliderect(object_.rect):
        screen.fill(BLACK) 
        screen.blit(end,end_rect)
        all_sprites_list.remove(object_)
        pygame.display.flip() 
        time.sleep(3)
        break
    
    if enemie_.rect.colliderect(object_.rect):
        screen.fill(BLACK) 
        screen.blit(end,end_rect)
        all_sprites_list.remove(object_)
        pygame.display.flip() 
        time.sleep(3)
        break
    
   
    

        
        
  

    object_.rect.colliderect(enemie_.rect)
    object_.rect.colliderect(enemie2_.rect)
    object_.rect.colliderect(enemie3_.rect)
    object_.rect.colliderect(enemie4_.rect)
    object_.rect.colliderect(enemie5_.rect)
    
   
            

    if enemie_.rect.y >= 510 : 
        enemie_.rect.x = random.randint(0,WIDTH - enemie_WIDTH)
        enemie_.rect.y = -5

    if enemie2_.rect.y >= 510 : 
        enemie2_.rect.x = random.randint(0,WIDTH - enemie2_WIDTH)
        enemie2_.rect.y = -5

    if enemie3_.rect.y >= 510 : 
        enemie3_.rect.x = random.randint(0,WIDTH - enemie3_WIDTH)
        enemie3_.rect.y = -5

    if enemie4_.rect.y >= 510 : 
        enemie4_.rect.x = random.randint(0,WIDTH - enemie4_WIDTH)
        enemie4_.rect.y = -5

    if enemie5_.rect.y >= 510 : 
        enemie5_.rect.x = random.randint(0,WIDTH - enemie5_WIDTH)
        enemie5_.rect.y = -5

    enemie_.moveForward(5)
    enemie2_.moveForward(5)
    enemie3_.moveForward(5)
    enemie4_.moveForward(5)
    enemie5_.moveForward(5)

    if object_.rect.x < -10 : object_.rect.x = 500
    if object_.rect.x >= 510 : object_.rect.x = -5
    if object_.rect.y < -10 : object_.rect.y = 500
    if object_.rect.y >= 510 : object_.rect.y = -5

  
    all_sprites_list.update() 
    screen.fill(SURFACE_COLOR) 
    all_sprites_list.draw(screen) 
    weapons_list.draw(screen)
    particle_sprites_list.draw(screen)
    screen.blit(Score_text,Score_Text_rect)

    pygame.display.flip() 
    clock.tick(60) 
  

pygame.quit