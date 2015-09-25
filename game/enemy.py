#enemy.py

import mob, pyglet, util, random, viewport
from pyglet.window import key

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

enemy_image1=pyglet.resource.image('enemy1.png')
util.center_image(enemy_image1)

enemy_image2=pyglet.resource.image('enemy2.png')
util.center_image(enemy_image2)
'''
enemy_image3=pyglet.resource.image('enemy3.png')
util.center_image(enemy_image3)

enemy_image4=pyglet.resource.image('enemy4.png')
util.center_image(enemy_image4)

enemy_image1=enemy_images.texture.get_region(0,0,151.25,225)
util.center_image(enemy_image1)

enemy_image2=enemy_images.texture.get_region(151.25,302.5,25,225)
util.center_image(enemy_image2)

enemy_image3=enemy_images.texture.get_region(302.5,0,453.75,225)
util.center_image(enemy_image3)

enemy_image4=enemy_images.texture.get_region(453.75,0,605,225)
util.center_image(enemy_image4)'''

class Enemy(mob.Mob):

    def __init__(self,image,x,y,*args,**kwargs):
        super(Enemy,self).__init__(enemy_image1,*args,**kwargs)
        self.image=image
        self.affected_by_gravity=True
        #self.antigravity=True
        self.scale=0.113
        self.spd=200
        self.x=x
        self.y=y
        self.is_enemy=True
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        self.acc=self.height*14.0
        
        self.vel_x=random.random()*self.spd
        if random.randint(0,1):self.vel_x*=-1
        self.vel_y=random.random()*self.spd
        if random.randint(0,1):self.vel_y*=-1

        pyglet.clock.schedule_interval(self.change_velocity,3)
   
    def update(self,dt):

        dx=self.vel_x*dt
        dy=self.vel_y*dt
        
        if not self.supported:
            self.vel_y-=self.acc*dt
            dy=self.vel_y*dt

        
        super(Enemy,self).update(dx,dy,dt)

    def change_velocity(self,dt):

        self.vel_x=random.random()*self.spd
        if random.randint(0,1):self.vel_x*=-1
        self.vel_y=random.random()*self.spd
        if random.randint(0,1):self.vel_y*=-1

    def check_bounds(self):
 
        min_x=self.width//2
        max_x=viewport.window.width-(self.width//2)
        min_y=self.height//2
        max_y=viewport.window.height-(self.height//2)

        if self.x<=min_x or \
           self.x>=max_x: self.vel_x*=-1
        if self.y<=min_y or \
           self.y>=max_y: self.vel_y*=-1

    def handle_collision_with(self,other):
        if other.is_beam:
            other.dead=True
            self.dead=True


   
