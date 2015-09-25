#gate.py

import collidable, util, pyglet, aabb, mob

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

portal_image=pyglet.resource.image('gate.png')
util.center_image(portal_image)


class Gate(collidable.Collidable):
    
    def __init__(self,x,y, *args, **kwargs):
        super(Gate,self).__init__(portal_image,x=x,y=y,*args,**kwargs)
        self.scale=1
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

        
        
    def update(self,dt):
        super(Gate,self).update(dt)
        #if self.found:self.visible=True
        

    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    
    def handle_collision_with(self,other):
        pass


    

    
    
