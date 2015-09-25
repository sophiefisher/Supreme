#laser_shoot.py
import collidable, math, util, mob, pyglet, avatar

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

beam_image=pyglet.resource.image('beam5.png')
util.center_image(beam_image)
laser_batch=pyglet.graphics.Batch()

boom_sound=pyglet.media.load('./sounds/boom.wav',streaming=False)

class Beam_Shoot(mob.Mob):

    def __init__(self,x,y,*args,**kwargs):

        super(Beam_Shoot,self).__init__(beam_image,x=x,y=y,*args,**kwargs)
        self.scale=1
        self.spd=400
        self.batch=laser_batch
        self.destruct_timer=2
        self.dead=False
        #self.is_beam_shoot=True
        self.vel_x=0
        self.left=self.x-(self.width//2)
        self.right=self.x+(self.width//2)
        self.top=self.y+(self.height//2)
        self.bottom=self.y-(self.height//2)
        self.anchor_x=0
        self.anchor_y=0
        #self.x=x
        #self.y=y
        self.is_beam=True
        #test to see if avatar is right or left facing
        if avatar.right_facing==False:
            self.vel_x=-1*self.spd
        elif avatar.right_facing==True:
            self.vel_x=self.spd
        
    def update(self,dt):
        if self.dead: pyglet.clock.unschedule(self.update)
        else:
            dx=self.vel_x*dt
            dy=0
            self.x+=(dx*dt)
            self.left=self.x-(self.width//2)
            self.right=self.x+(self.width//2)
            self.top=self.y+(self.height//2)
            self.bottom=self.y-(self.height//2)
            super(Beam_Shoot,self).update(dx,dy,dt)
            if self.left<=0 or self.right>=(1100):
                    self.dead=True

    def collides_with(self,other):
        pass
        '''#first assume square resources and check distances
        actual_dist=util.distance((self.x,self.y),(other.x,other.y))
        min_dist=((self.image.height/2)*math.sqrt(2))+((other.image.height/2)*math.sqrt(2))
        #if collision detected, check edges of each for overlap
        if actual_dist<min_dist:
                if self.bottom<=other.top and self.top>=other.bottom and self.left<=other.right and self.right>=other.left:
                        return True
                        self.dead=True
                else:
                        return False
        else:
            return False'''
     
    def handle_collision_with(self, other):
        pass
        #if other.is_power_up:
                #pass
        #if other.is_enemy:
                #other.dead=True
                #self.dead=True
                #boom_sound.play()
        #if other.is_tile:
                #self.dead=True
        #if other.is_avatar:
               #pass

            
            
