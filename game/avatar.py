#avatar.py

import mob, pyglet, util,laser_shoot,hud,math,gravity,health
from pyglet.window import key

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

avatar_left_laser=pyglet.resource.image('right_laser_hedgehog.png')
util.center_image(avatar_left_laser)
avatar_right_laser=pyglet.resource.image('left_laser_hedgehog.png')
util.center_image(avatar_right_laser)

right_facing=True

class Avatar(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Avatar,self).__init__(avatar_right_laser,x=0,y=530,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.has_laser=False
        self.scale=.035
        self.affected_by_gravity=True
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        self.spd=200
        self.health=11
        #self.x=0
        #self.y=530
        self.rotation=180
        self.vel_y=0
        self.is_avatar=True
        self.death_timer=0
        #self.dead=False
        self.jump_velocity=-750
        #self.acc=-1*self.height*2
        #self.has_laser=True
        #self.anchor_x=(self.width//2)
        #self.anchor_y=(self.height//2)
        #self.shot_timer=0.1
        #self.reload_timer=self.shot_timer
        
   
    def update(self,dt):

        global right_facing

        self.death_timer-=dt

        dx=0
        dy=0
        
        if self.key_handler[key.RIGHT]:
            dx=self.spd*dt
            if gravity.normal_gravity==False:
                if self.image==avatar_left_laser:
                    self.image=avatar_right_laser
            elif gravity.normal_gravity==True:
                if self.image==avatar_right_laser:
                    self.image=avatar_left_laser
            right_facing=True
            
        if self.key_handler[key.LEFT]:
            dx=-1*self.spd*dt
            if gravity.normal_gravity==False:
                if self.image==avatar_right_laser:
                    self.image=avatar_left_laser
            elif gravity.normal_gravity==True:
                if self.image==avatar_left_laser:
                    self.image=avatar_right_laser
            right_facing=False


        '''if not self.affected_by_gravity:
           

            if self.key_handler[key.UP]:
                dy=self.spd*dt
                

            if self.key_handler[key.DOWN]:
                dy=-1*self.spd*dt'''

                
        if self.affected_by_gravity:
            if not self.supported:
                self.vel_y-=self.acc*dt
                dy=self.vel_y*dt

        if self.supported:
            if self.key_handler[key.SPACE]:
                self.jump()
                

        super(Avatar,self).update(dx,dy,dt)


    def handle_collision_with(self,other):
        if self.death_timer<=0:
            if other.is_enemy:
                self.death_timer=1.5
                health.healthbar.decrease_healthbar()
                if health.healthbar.image==health.image0:
                    self.dead=True
                #self.dead=True
        #elif other.is_pwrup:
            #self.power_up()

    '''def power_up(self):
        self.image=avatar_pwrup_image
        self.speed=400
        pyglet.clock.schedule_once(self.revert,5)

    def revert(self,dt):
        self.image=avatar_image
        self.speed=200'''
        


    def jump(self):
        self.supported=False
        self.vel_y=self.jump_velocity

