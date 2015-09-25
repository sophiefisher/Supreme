#portal.py

import collidable, util, pyglet, aabb, mob, sound_fx

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

portal_image=pyglet.resource.image('portal.png')
util.center_image(portal_image)


class Portal(collidable.Collidable):
    
    def __init__(self,x,y, *args, **kwargs):
        super(Portal,self).__init__(portal_image,x=x,y=y,*args,**kwargs)
        self.scale=.04
        
        #self.visible=True
        #self.found=False

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

        
        
    def update(self,dt):
        super(Portal,self).update(dt)
        #if self.found:self.visible=True
        

    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    
    def handle_collision_with(self,other):
        if other.is_avatar:
            sound_fx.ping.play()
            self.dead=True


    

    
    
