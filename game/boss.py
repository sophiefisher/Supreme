#boss.py

import mob, pyglet, util, random, viewport
from pyglet.window import key

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

boss=pyglet.resource.image('enemy4.png')
util.center_image(boss)


class Boss(mob.Mob):

    def __init__(self,x,y,*args,**kwargs):
        super(Boss,self).__init__(boss,x=x,y=y,*args,**kwargs)
        #self.image=image
        self.visible=False
        self.affected_by_gravity=True
        #self.antigravity=True
        self.scale=.48
        self.spd=600
        self.is_enemy=True
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        self.acc=self.height*.5
        self.boss_health=40

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

        
        super(Boss,self).update(dx,dy,dt)

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
        if other.is_beam and self.boss_health>1:
            self.scale-=.0093
            self.boss_health-=1
            other.dead=True
        elif other.is_beam and self.boss_health==1:
            other.dead=True
            self.dead=True
                    
                
