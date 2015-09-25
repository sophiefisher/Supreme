#switch.py

import collidable, util, pyglet, aabb, gravity, sound_fx

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

up_switch=pyglet.resource.image('up_switch.png')
util.center_image(up_switch)

down_switch=pyglet.resource.image('down_switch.png')
util.center_image(down_switch)

class Switch(collidable.Collidable):
    
    def __init__(self,x,y,direction, *args, **kwargs):
        super(Switch,self).__init__(up_switch,x=x,y=y,*args,**kwargs)
        self.direction=direction
        if self.direction=='left':
            self.image=up_switch
        elif self.direction=='right':
            self.image=down_switch
            self.rotation=180
        self.scale=.75
        self.is_pwrup=True
        self.dead=False
        self.flipped=False

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
        
    def flip_switch(self):
        if self.image==down_switch:
            self.image=up_switch
        elif self.image==up_switch:
            self.image=down_switch
        self.flipped=True

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    
    def handle_collision_with(self,other):

        if other.is_avatar:
            if self.flipped==False:
                self.flip_switch()
                #sound_fx.switch_sound.play()
                gravity.toggle_gravity(other)
#make classes for the bubbles and possibly the gun
