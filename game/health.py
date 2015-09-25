#health.py
import pyglet,util,collidable

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

image0=pyglet.resource.image('0.png')
util.center_image(image0)

image1=pyglet.resource.image('1.png')
util.center_image(image1)

image2=pyglet.resource.image('2.png')
util.center_image(image2)

image3=pyglet.resource.image('3.png')
util.center_image(image3)

image4=pyglet.resource.image('4.png')
util.center_image(image4)

image5=pyglet.resource.image('5.png')
util.center_image(image5)

image6=pyglet.resource.image('6.png')
util.center_image(image6)

image7=pyglet.resource.image('7.png')
util.center_image(image7)

image8=pyglet.resource.image('8.png')
util.center_image(image8)

image9=pyglet.resource.image('9.png')
util.center_image(image9)

image10=pyglet.resource.image('10.png')
util.center_image(image10)

image11=pyglet.resource.image('11.png')
util.center_image(image11)

#health_batch=pyglet.graphics.Batch()

class HealthBar(pyglet.sprite.Sprite):

    def __init__(self,x,y,*args,**kwargs):
        super(HealthBar,self).__init__(image11,x=x,y=y,*args,**kwargs)
        #self.batch=health_batch
        self.scale=.45

    def decrease_healthbar(self):
        if self.image==image11:
            self.image=image10
            
        elif self.image==image10:
            self.image=image9
            
        elif self.image==image9:
            self.image=image8
            
        elif self.image==image8:
            self.image=image7

        elif self.image==image7:
            self.image=image6

        elif self.image==image6:
            self.image=image5

        elif self.image==image5:
            self.image=image4

        elif self.image==image4:
            self.image=image3

        elif self.image==image3:
            self.image=image2

        elif self.image==image2:
            self.image=image1

        elif self.image==image1:
            self.image=image0
        
    def increase_healthbar(self):
        if self.image==image1:
            self.image=image2
            
        elif self.image==image2:
            self.image=image3
            
        elif self.image==image3:
            self.image=image4
            
        elif self.image==image4:
            self.image=image5

        elif self.image==image5:
            self.image=image6

        elif self.image==image6:
            self.image=image7

        elif self.image==image7:
            self.image=image8

        elif self.image==image8:
            self.image=image9

        elif self.image==image9:
            self.image=image10

        elif self.image==image10:
            self.image=image11

healthbar=HealthBar(600,625)
        
