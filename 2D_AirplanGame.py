# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:33:49 2018

@author: Administrator
"""
import pygame
import time,math,random

class Heroplane:
    '''
    定义玩家飞机类
    英雄类的类方法应包含初始化对象参数、令窗口对象绑定自己、键盘响应（即定义对象接收输入后做的动作）
    '''
    def __init__(self,screen_temp):
        # 初始化飞机出场位置
        self.x = 200
        self.y = 600
        self.speed = 8
        #绑定窗口对象
        self.screen=screen_temp
        #载入飞机图片
        self.image=pygame.image.load('./images/me.png')
        #定义玩家子弹列表
        self.bullet_list = []
        
    def display(self):
        '''
        绘制飞机（先绘制子弹使其在飞机下面）
        '''
        # 逐颗绘制子弹
        for b in self.bullet_list:
            display(b)
            if b.move():
                self.bullet_list.remove(b)
        #绘制飞机
        display(self)
    
    def move_left(self):
        #左移
        if self.x >= 20:
            self.x -= self.speed
    
    def move_right(self):
        #右移
        if self.x <= 380:
            self.x += self.speed
            

    def move_up(self):
            #上移
            if self.y >= 20:
                self.y -= self.speed    

    def move_down(self):
            #下移
            if self.y <= 580:
                self.y += self.speed
                
    def fire(self):
        #定义开火
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
        
class Bullet:
    
    '''
    定义子弹类
    '''
    def __init__(self,screen_temp,x,y):
        ''' 初始化玩家子弹'''
        #初始化子弹出场位置
        self.x = x + 45;
        self.y = y
        self.speed = 10
        #绑定窗口对象
        self.screen = screen_temp
        #载入子弹图片
        self.image = pygame.image.load('./images/pd.png')
    
    def move(self):
        '''移动子弹'''
        self.y -= self.speed
        if self.y <= 20:
            return True
        
class EnemyPlane:
    '''
    定义敌机类
    '''
    def __init__(self,screen_temp):
        '''初始化敌机'''
        #初始化敌机出场位置（随机）
        self.x = random.choice(range(408))
        self.y = -75
        #敌机血量
        self.HP=10
        #绑定窗口对象
        self.screen=screen_temp
        #载入敌机图片
        self.image=pygame.image.load('./images/e'+str(random.choice(range(0,3)))+'.png')
        #定义敌机的子弹列表（用于存放子弹）
        self.bullet_list = []

    def move(self,hero):
        '''移动敌机'''
        self.y += 4
        #遍历所有子弹，并执行碰撞检测
        for b in hero.bullet_list:
            if b.x>self.x+6 and b.x<self.x+98 and b.y>self.y+16 and b.y<self.y+64:
                self.HP-=1
                hero.bullet_list.remove(b)
                if self.HP<=0:
                    return True

class EnemyBullet:
    '''
    定义敌机子弹类
    '''
    def __init__(self,screen_temp,x,y,hero):
        '''初始化敌机子弹'''
        #初始化子弹出场位置
        self.x = x+53
        self.y = y+74
        self.speed=0.5
        #初始化追踪角度
        self.angx=hero.x+53-self.x
        self.angy=hero.y+38-self.y
        #绑定窗口对象
        self.screen=screen_temp
        #载入子弹图片
        self.image=pygame.image.load('./images/epd.png')

    def move(self,hero):
        '''子弹追踪英雄'''
        self.x += self.angx*self.speed/math.sqrt(self.angx**2+self.angy**2)
        self.y += self.angy*self.speed/math.sqrt(self.angx**2+self.angy**2)
        if self.y<=-20 or self.y>=700 or self.x<=-20 or self.x>=512:
            return 1
        elif self.x>hero.x and self.x<hero.x+106 and self.y+30>hero.y+15 and self.y+30<hero.y+42:
            return 2

def key_control(hero):   
    '''键盘响应'''
    #执行退出操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit()")
            exit()
            pygame.quit()
    #获取按键事件
    pressed_keys = pygame.key.get_pressed()
    #判断事件执行类型
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        hero.move_left()
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        hero.move_right()
        
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        hero.move_up()
    elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        hero.move_down()
    
    #此处另外判断空格，否则不能同时操作
    if pressed_keys[pygame.K_SPACE]:
        hero.fire()
        
        
def display(obj):
    '''定义绘制函数（将对象绑定至窗口）'''
    obj.screen.blit(obj.image,(obj.x,obj.y))
    

def main():
    '''主函数程序'''
    #创建游戏主窗口
    screen = pygame.display.set_mode((512,700),0,0)
    pygame.display.set_caption('飞机大战')
    
    #创建游戏背景
    back = random.choice(['0','1'])
    background = pygame.image.load("./images/bg"+str(back)+".jpg")
    
    #创建玩家飞机
    hero = Heroplane(screen)
    
    #无限循环，逐帧刷新画面
    m = -836
    
    #存放敌机的列表
    enemy_list = []
    
    #存放敌机子弹的列表
    enemybullet_list = []
    
    #是否死亡
    die = False
    
    while True:
            #绘制画面（锚点在窗口外，即图片上方一部分在窗口外）
            screen.blit(background,(0,m))
            m += 2
            if m >= -68:
                m =- 836
            
            #执行键盘响应
            key_control(hero)
            
            #根据死亡变量决定绘制飞机或者爆炸效果
            if die:
                screen.blit(pygame.image.load('./images/gameover.png'), (131, 175))
                screen.blit(pygame.image.load('./images/restart.png'), (100, 450))
                screen.blit(pygame.image.load('./images/quit.png'), (345, 443))
                #检测鼠标点击事件
                pressed_array = pygame.mouse.get_pressed()
                for i in range(len(pressed_array)):
                    if pressed_array[i]:
                        if i == 0:
                            pos = pygame.mouse.get_pos()
                            if pos[0]>=100 and pos[0]<=204 and pos[1]>=450 and pos[1]<=477:
                                #重置游戏
                                die=0
                                hero.x=200
                                hero.y=600
                                enemy_list.clear()
                                enemybullet_list.clear()
                                hero.bullet_list.clear()
                            elif pos[0]>=345 and pos[0]<=412 and pos[1]>=443 and pos[1]<=481:
                                exit()
                                pygame.quit()
            else:
                hero.display()
            
            if die == False:
                #绘制敌机
                if random.choice(range(50)) == 14:
                    Enemy=EnemyPlane(screen)
                    enemy_list.append(Enemy)
                #遍历敌机列表并移动
                for e in enemy_list:
                    display(e)
                    #敌机发射子弹，随机发射
                    if e.y >= 150:
                        if random.choice(range(50)) == 14:
                            enemybullet_list.append(EnemyBullet(screen,e.x,e.y,hero))
                    #检测敌机走远或被击落
                    if e.move(hero):
                        for i in range(0,4):
                            for j in range(10):
                                screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (e.x,e.y))
                        enemy_list.remove(e)
                    if e.y >= 700:
                        enemy_list.remove(e)
                    #检测是否与玩家碰撞
                    if(e.x > hero.x and e.x < hero.x + 160 and e.y +30>hero.y+15 and e.y+30<hero.y+42)or (e.x+104>hero.x and e.x+104<hero.x+106 and e.y+30>hero.y+15 and e.y+30<hero.y+42)or (e.x>hero.x and e.x<hero.x+106 and e.y+62>hero.y+15 and e.y+62<hero.y+42)or (e.x+104>hero.x and e.x+104<hero.x+106 and e.y+62>hero.y+15 and e.y+62<hero.y+42):
                        for i in range(0, 4):
                            for j in range(10):
                                screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (e.x, e.y))
                                screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (hero.x, hero.y))
                        enemy_list.remove(e)
                        die=1
                     #绘制敌机子弹
                    for eb in enemybullet_list:
                        display(eb)
                        if eb.move(hero)==1:
                            enemybullet_list.remove(eb)
                        elif eb.move(hero)==2:
                            for i in range(0, 4):
                                for j in range(10):
                                    screen.blit(pygame.image.load('./images/bomb' + str(i) + '.png'), (hero.x, hero.y))
                            enemybullet_list.remove(eb)
                            die = 1
            # 刷新显示（提交上面的所有更改后的绘制）
            pygame.display.update()
            
            # 给刷新定间隔以节约系统资源
            time.sleep(0.03)
            

# 判断当前是否是主程序，并调用
if __name__=="__main__":
    main()
