#!/usr/bin/python
# -*- coding: <Unicode> -*-

import pygame
import time, math, random


class Heroplane:
    """
    define hero(player) class
    hero class method should include init, bonding windows and keyboard respond
    """

    def __init__(self, screen_temp):
        # init hero starting position
        self.x = 200
        self.y = 600
        self.speed = 8
        # bonding windows
        self.screen = screen_temp
        # load airplane pic
        self.image = pygame.image.load('./images/me.png')
        # define bullet list
        self.bullet_list = []

    def display(self):
        """
        draw plane (draw bullet first to make it under the plane)
        """
        # draw bullet one by one
        for b in self.bullet_list:
            display(b)
            if b.move():
                self.bullet_list.remove(b)
        # draw plane
        display(self)

    def move_left(self):
        # move left
        if self.x >= 20:
            self.x -= self.speed

    def move_right(self):
        # move right
        if self.x <= 380:
            self.x += self.speed

    def move_up(self):
        # move up
        if self.y >= 20:
            self.y -= self.speed

    def move_down(self):
        # move down
        if self.y <= 580:
            self.y += self.speed

    def fire(self):
        # define fire
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Bullet:
    """
    define bullet
    """

    def __init__(self, screen_temp, x, y):
        """ init player's bullet"""
        # init bullet position
        self.x = x + 45
        self.y = y
        self.speed = 10
        # bond windows
        self.screen = screen_temp
        # load bullet pic
        self.image = pygame.image.load('./images/pd.png')

    def move(self):
        """move bullets"""
        self.y -= self.speed
        if self.y <= 20:
            return True


class EnemyPlane:
    """
    define enemy
    """

    def __init__(self, screen_temp):
        """ init enemy """
        # randomly init enemy starting position
        self.x = random.choice(range(408))
        self.y = -75
        # enemy HP
        self.HP = 10
        # bonding window
        self.screen = screen_temp
        # load enemy pic
        self.image = pygame.image.load('./images/e' + str(random.choice(range(0, 3))) + '.png')
        # define enemy bullet list
        self.bullet_list = []

    def move(self, hero):
        """move enemy"""
        self.y += 4
        # traversal all bullets and test for collsion
        for b in hero.bullet_list:
            if b.x > self.x + 6 and b.x < self.x + 98 and b.y > self.y + 16 and b.y < self.y + 64:
                self.HP -= 1
                hero.bullet_list.remove(b)
                if self.HP <= 0:
                    return True


class EnemyBullet:
    """
    define enemy bullet class
    """

    def __init__(self, screen_temp, x, y, hero):
        """define enemy bullet"""
        # init enemy bullet starting position
        self.x = x + 53
        self.y = y + 74
        self.speed = 0.5
        # init follow angles
        self.angx = hero.x + 53 - self.x
        self.angy = hero.y + 38 - self.y
        # bond windows obj
        self.screen = screen_temp
        # load bullet image
        self.image = pygame.image.load('./images/epd.png')

    def move(self, hero):
        """bullets chase heroes """
        self.x += self.angx * self.speed / math.sqrt(self.angx ** 2 + self.angy ** 2)
        self.y += self.angy * self.speed / math.sqrt(self.angx ** 2 + self.angy ** 2)
        # bullet out of bound --> 1
        if self.y <= -20 or self.y >= 700 or self.x <= -20 or self.x >= 512:
            return 1 
        # bullet hits --> 2
        elif self.x > hero.x and self.x < hero.x + 106 and self.y + 30 > hero.y + 15 and self.y + 30 < hero.y + 42:
            return 2


def key_control(hero):
    """keyboard responds"""
    # execute quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit()")
            exit()
            pygame.quit()
    # get keyboard events
    pressed_keys = pygame.key.get_pressed()
    # respond keyboard events
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        hero.move_left()
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        hero.move_right()

    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        hero.move_up()
    elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        hero.move_down()

    # find keyboard event of "space", or can't operate in the same time
    if pressed_keys[pygame.K_SPACE]:
        hero.fire()


def display(obj):
    """ drawing function(bon obj to windows)"""
    obj.screen.blit(obj.image, (obj.x, obj.y))


def main():
    # init
    pygame.init()

    # load sounds
    crash_sound = pygame.mixer.Sound("sounds/crash.wav")
    pygame.mixer.music.load("sounds/demon.wav")

    # create the game windows
    screen = pygame.display.set_mode((512, 700), 0, 0)
    pygame.display.set_caption('2D_Airplane')

    # create game background
    back = random.choice(['0', '1'])
    background = pygame.image.load("./images/bg" + str(back) + ".jpg")

    # create hero
    hero = Heroplane(screen)

    # fresh the image constantly
    m = -836

    # list for storing enemy
    enemy_list = []

    # list for storing enemy bullets
    enemybullet_list = []

    # die set as false
    die = False

            
    pygame.mixer.music.play(-1)

    while True:
        # draw images (pointer is outside of the window. Half of the image is outside )
        screen.blit(background, (0, m))
        m += 2
        if m >= -68:
            m = - 836

        # respond to keyboard
        key_control(hero)

        # draw exploding effect based on the plane HP
        if die:
            pygame.mixer.music.stop()
            screen.blit(pygame.image.load('./images/gameover.png'), (131, 175))
            screen.blit(pygame.image.load('./images/restart.png'), (100, 450))
            screen.blit(pygame.image.load('./images/quit.png'), (345, 443))
            # detect mouse event
            pressed_array = pygame.mouse.get_pressed()
            for i in range(len(pressed_array)):
                if pressed_array[i]:
                    if i == 0:
                        pos = pygame.mouse.get_pos()
                        if 100 <= pos[0] <= 204 and 450 <= pos[1] <= 477:
                            # reset game
                            die = 0
                            hero.x = 200
                            hero.y = 600
                            enemy_list.clear()
                            enemybullet_list.clear()
                            hero.bullet_list.clear()
                            pygame.mixer.music.play(-1)
                        elif 345 <= pos[0] <= 412 and 443 <= pos[1] <= 481:
                            exit()
                            pygame.quit()
        else:
            hero.display()

        if not die:
            # draw enemy planes
            if random.choice(range(50)) == 14:
                Enemy = EnemyPlane(screen)
                enemy_list.append(Enemy)
            # traverse the enemy plane list
            for e in enemy_list:
                display(e)
                # enemy planes randomly shoot bullets
                if e.y >= 150:
                    if random.choice(range(50)) == 14:
                        enemybullet_list.append(EnemyBullet(screen, e.x, e.y, hero))
                # detect if the enemy planes are alive
                if e.move(hero):
                    for i in range(0, 4):
                        for j in range(10):
                            screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (e.x, e.y))
                    enemy_list.remove(e)
                if e.y >= 700:
                    enemy_list.remove(e)
                # detect collision
                if (hero.x < e.x < hero.x + 160 and hero.y + 15 < e.y + 30 < hero.y + 42) or (
                        hero.x < e.x + 104 < hero.x + 106 and hero.y + 15 < e.y + 30 < hero.y + 42) or (
                        hero.x < e.x < hero.x + 106 and hero.y + 15 < e.y + 62 < hero.y + 42) or (
                        hero.x < e.x + 104 < hero.x + 106 and hero.y + 15 < e.y + 62 < hero.y + 42):
                    pygame.mixer.Sound.play(crash_sound)    
                    for i in range(0, 4):
                        for j in range(10):
                            screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (e.x, e.y))
                            screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (hero.x, hero.y))
                    enemy_list.remove(e)
                    die = 1
                # draw enemy bullets
                for eb in enemybullet_list:
                    display(eb)
                    if eb.move(hero) == 1:
                        enemybullet_list.remove(eb)
                    elif eb.move(hero) == 2:
                        pygame.mixer.Sound.play(crash_sound)
                        # 10 frames, 4 random bomb image options 
                        for i in range(0, 4):
                            for j in range(10):
                                screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (hero.x, hero.y))
                        enemybullet_list.remove(eb)
                        die = 1
        # refresh display
        pygame.display.update()

        # 0.03s for every refresh to save CPU resource
        time.sleep(0.03)


# main
if __name__ == "__main__":
    main()

