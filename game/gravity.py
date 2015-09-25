#gravity.py

import avatar, mob

normal_gravity=False
def toggle_gravity(self):
    global normal_gravity
    normal_gravity = not normal_gravity
    #if trying to switch to antigravity, do this:
    if not normal_gravity:
        self.acc=-1*self.acc
        self.jump_velocity=-self.jump_velocity
        self.rotation=180
    #if trying to switch to gravity, do this:
    if normal_gravity:
        self.acc=-1*self.acc
        self.jump_velocity=-self.jump_velocity
        self.rotation=0
    
    '''things that have to be switched:
    -self.acc from mob.py switched to postitive
    -if self.y<=occ_tile.y-self.height//2: has to be changed to
    self.y>=occ_tile.y+self.height//2 in mob.py-taken care of in mob
    -jump velocity from avatar.py changed to 600
    -rotate the object
    '''
    
