#background.py

import pyglet, util
import random, viewport, aabb
background_batch=pyglet.graphics.Batch()

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

background_image=pyglet.resource.image('background.jpg')

class Background(pyglet.sprite.Sprite):
        def __init__(self,*args,**kwargs):
                super(Background,self).__init__(background_image,*args,**kwargs)
                      

                self.scale=.575
                
                self.batch=background_batch
                self.dead=False
