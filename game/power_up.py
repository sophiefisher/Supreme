#power_up.py
'''here i will make classes for the laser which will enable the avatar
to shoot and change the avatar's image, and oxygen bubbles which will
increase the avatar's oxygen supply'''

import collidable, util, pyglet, aabb, mob, health, sound_fx

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

gun_image=pyglet.resource.image('lasergun.png')
util.center_image(gun_image)

bubble_image=pyglet.resource.image('bubble2.png')
util.center_image(bubble_image)

#bubble_batch=pyglet.graphics.Batch()

class Laser(collidable.Collidable):
    
    def __init__(self,x,y, *args, **kwargs):
        super(Laser,self).__init__(gun_image,x=x,y=y,*args,**kwargs)
        self.scale=.25
        self.is_pwrup=True
        self.dead=False
        self.rotation=352

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    
    def handle_collision_with(self,other):

        if other.is_avatar:
            other.has_laser=True
            self.dead=True

class Bubble(collidable.Collidable):
    
    def __init__(self,x,y, *args, **kwargs):
        super(Bubble,self).__init__(bubble_image,x=x,y=y,*args,**kwargs)
        self.scale=.14
        self.is_pwrup=True
        self.dead=False
        #self.batch=bubble_batch

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    
    def handle_collision_with(self,other):

        if other.is_avatar:
            health.healthbar.increase_healthbar()
            sound_fx.pop_sound.play()
            self.dead=True
#make classes for the bubbles and possibly the gun
