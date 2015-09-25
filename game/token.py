#token.py

import collidable, util, pyglet, aabb

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

class Token(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Token,self).__init__(*args,**kwargs)
        self.scale=5

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    
    def handle_collision_with(self,other):

        if other.is_avatar:
            self.dead=True
           
