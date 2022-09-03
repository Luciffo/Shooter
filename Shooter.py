from random import randint

import pygame
pygame.font.init()
window = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
FPS = 60
killed: int = 0
game = True


class Picture(pygame.sprite.Sprite):
    def __init__(self, x, y, height, weight, img, speed):
        super(Picture, self).__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (height, weight))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Picture):
    def check_press(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed

    def attack(self):
        bullet = Bullet(rocket.rect.centerx, rocket.rect.top, 20, 50, "bullet.png", 10)
        bullets.add(bullet)
        # bullet.draw()
        # bullet.go()


class Bullet(Picture):
    def update(self):
        self.rect.y -= 13


class UFO(Picture):
    def update(self):
        self.rect.y += randint(1, 7)
        if self.rect.y > 500:
            self.rect.y = -100
            self.rect.x = randint(0, 600)


bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

for _ in range(7):
    enemies.add(UFO(randint(0 , 600), -100, 100, 50, 'alien.png', 10))

rocket = Player(300, 400, 50, 70, 'rocket.jpg', 10)
bullet = Bullet(rocket.rect.centerx, rocket.rect.top, 20, 50, "bullet.png", 10)
background = pygame.transform.scale(pygame.image.load("galaxy.jpeg"), (700, 500))


font = pygame.font.Font(None, 30)

win = font.render(
    'Перемога!', True, (0, 255, 0)
)

lost = font.render(
    'Поразка...', True, (255, 0, 0)
)

count_d = font.render(
    'Ворогів знищено: 0', True, (255, 255, 255)
)

count_l = font.render(
    'Ворогів пропущено: 0', True, (255, 255, 255)
)

Finish = False

game = True
killed = 0
failed = 0
while game:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)




    if not Finish:

        window.blit(background, (0, 0))
        count_d = font.render('Ворогів знищено:' + str(killed), True, (255, 255, 255))
        count_l = font.render('Ворогів пропущено:' + str(failed), True, (255, 255, 255))
        window.blit(count_d, (50, 50))
        window.blit(count_l, (450, 50))
        rocket.draw()
        rocket.update()
        s_collide = pygame.sprite.spritecollide(rocket, enemies, False)
        s_list = pygame.sprite.groupcollide(enemies, bullets, False, True)
        for name in s_list.keys():
            name.rect.y = -100
            name.rect.x = randint(0,600)
            killed += 1
        if len(s_collide) >= 1:
            Finish = True
        if killed == 50:
            Finish = True
        bullets.draw(window)
        bullets.update()
        enemies.update()
        enemies.draw(window)
        for i in events:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    rocket.attack()