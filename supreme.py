#topfile_template.py

import pyglet,random
pyglet.options['debug_lib'] = True 
import pyglet.graphics
from pyglet.window import key
from game import viewport,world,avatar,hud,spawn_enemies,spawn_tokens, background,switch,portal,boss
from game import token, hidden_token, util, instructions,gravity,laser_shoot,enemy,power_up,health,sound_fx

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

enemy_image1=pyglet.resource.image('enemy1.png')
util.center_image(enemy_image1)

enemy_image2=pyglet.resource.image('enemy2.png')
util.center_image(enemy_image2)

enemy_image3=pyglet.resource.image('enemy3.png')
util.center_image(enemy_image3)

enemy_image4=pyglet.resource.image('enemy4.png')
util.center_image(enemy_image4)

media_player=pyglet.media.Player()
media_player.queue(sound_fx.theme)
media_player.eos_action=media_player.EOS_LOOP

media_player2=pyglet.media.Player()
media_player2.queue(sound_fx.combat)
media_player2.eos_action=media_player2.EOS_LOOP

media_player3=pyglet.media.Player()
media_player3.queue(sound_fx.boss)
media_player3.eos_action=media_player3.EOS_LOOP

media_player4=pyglet.media.Player()
media_player4.queue(sound_fx.relax)
media_player4.eos_action=media_player4.EOS_LOOP

def init():

    global inst, event_stack_size, level, bg

    event_stack_size=0
    level=1
    inst=instructions.Instructions_display()
    inst.batch=inst_batch
    viewport.window.push_handlers(inst.key_handler)
    pyglet.clock.schedule_interval(inst.update,1/120.0)
    bg=background.Background()

def spawn_enemy(dt,x,y):

    enemy_image=random.choice([enemy_image1,enemy_image2,enemy_image3,enemy_image4])
    new_enemy=enemy.Enemy(enemy_image,x,y)
    new_enemy.batch=main_batch
    game_objects.append(new_enemy)

def spawn_boss(dt,x,y):

    new_boss=boss.Boss(x,y)
    new_boss.batch=main_batch
    game_objects.append(new_boss)

def spawn_bubble(dt,x,y):

    new_bubble=power_up.Bubble(x,y)
    new_bubble.batch=main_batch
    game_objects.append(new_bubble)

def spawn_laser(dt,x,y):

    new_laser=power_up.Laser(x,y,)
    new_laser.batch=main_batch
    game_objects.append(new_laser)

def check_instructions(dt):
    media_player.play()
    
    if inst.complete:
        pyglet.clock.unschedule(inst.update)
        pyglet.clock.unschedule(check_instructions)
        media_player.pause()
        media_player2.play()
        load_level_1(1)
    
    
def clear_level():

    global game_objects

    if game_objects:
        for obj in game_objects:
            obj.delete()
        game_objects=[]
            

def load_level_1(level):

    global game_objects, hidden, event_stack_size, player
    global tokens_collected, max_tokens, laser, switch1, portal1

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0
    
    game_objects=[]
    reload(world)
    world.generate_world(level)

    #hidden=hidden_token.Hidden_token(batch=main_batch)
    #hidden.x=250
    #hidden.y=500
    #hidden.update_bounding_box()
    #game_objects.append(hidden)

    health.healthbar.batch=main_batch
    #game_objects.append(health.healthbar)

    portal1=portal.Portal(3060,60)
    portal1.batch=main_batch
    game_objects.append(portal1)

    switch1=switch.Switch(1056,367,'left')
    switch1.batch=main_batch
    game_objects.append(switch1)

    pyglet.clock.schedule_once(spawn_laser,.01,535,75)

    #laser=power_up.Laser(1050,140)
    #laser.batch=main_batch
    #laser.x=200
    #laser.y=200
    #laser.update_bounding_box()
    #laser.batch=main_batch
    #game_objects.append(laser)

    pyglet.clock.schedule_once(spawn_bubble,.01,251,50)
    pyglet.clock.schedule_once(spawn_bubble,.01,45,325)

    pyglet.clock.schedule_once(spawn_enemy,.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,3.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,6.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,9.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,12.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,15.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,18.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,21.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,24.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,27.01,991,528)
    pyglet.clock.schedule_once(spawn_enemy,30.01,991,528)
    
    pyglet.clock.schedule_once(spawn_enemy,.01,510,25)
    pyglet.clock.schedule_once(spawn_enemy,.01,251,50)

    #collectibles=spawn_tokens.spawn_tokens(4,level)
    #for collectible in collectibles:
    #    collectible.batch=main_batch
    #game_objects+=collectibles

    #tokens_collected=0
    #max_tokens=4

    player=avatar.Avatar(batch=avatar_batch)
    game_objects.append(player)

    
    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)

def load_level_2(level):

    global game_objects, hidden, event_stack_size, player
    global tokens_collected, max_tokens, laser, switch1, portal1

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0
    
    game_objects=[]
    reload(world)
    world.generate_world(level)
    
    player=avatar.Avatar(batch=avatar_batch)
    game_objects.append(player)

    portal1=portal.Portal(3060,60)
    portal1.batch=main_batch
    game_objects.append(portal1)

    switch1=switch.Switch(996,365,'right')
    switch1.batch=main_batch
    game_objects.append(switch1)

    pyglet.clock.schedule_once(spawn_laser,.01,134,195)

    pyglet.clock.schedule_once(spawn_bubble,.01,205,197)
    #pyglet.clock.schedule_once(spawn_bubble,.01,755,521)
    pyglet.clock.schedule_once(spawn_bubble,.01,576,322)
    pyglet.clock.schedule_once(spawn_bubble,.01,624,322)
    #pyglet.clock.schedule_once(spawn_bubble,.01,45,325)

    pyglet.clock.schedule_once(spawn_enemy,.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,6.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,12.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,18.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,24.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,30.01,289,570)
    pyglet.clock.schedule_once(spawn_enemy,36.01,289,570)

    pyglet.clock.schedule_once(spawn_enemy,.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,11.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,20.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,30.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,40.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,50.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,55.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,60.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,65.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,70.01,900,570)
    pyglet.clock.schedule_once(spawn_enemy,75.01,900,570)
    #pyglet.clock.schedule_once(spawn_enemy,35.01,950,570)
    

    pyglet.clock.schedule_once(spawn_enemy,.01,45,45)

    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)

def load_level_3(level):

    global game_objects, hidden, event_stack_size, player
    global tokens_collected, max_tokens, laser, switch1, portal1

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0
    
    game_objects=[]
    reload(world)
    world.generate_world(level)
    
    player=avatar.Avatar(batch=avatar_batch)
    game_objects.append(player)

    portal1=portal.Portal(3060,60)
    portal1.batch=main_batch
    game_objects.append(portal1)

    pyglet.clock.schedule_once(spawn_bubble,.01,25,175)
    pyglet.clock.schedule_once(spawn_bubble,.01,200,175)
    pyglet.clock.schedule_once(spawn_bubble,.01,1077,223)
    pyglet.clock.schedule_once(spawn_bubble,.01,1049,553)

    pyglet.clock.schedule_once(spawn_enemy,.01,125,175)
    pyglet.clock.schedule_once(spawn_enemy,.01,125,175)

    pyglet.clock.schedule_once(spawn_enemy,1.5,260,570)
    pyglet.clock.schedule_once(spawn_enemy,1.5,560,570)
    pyglet.clock.schedule_once(spawn_enemy,1.5,410,570)

    pyglet.clock.schedule_once(spawn_enemy,9.5,260,570)
    pyglet.clock.schedule_once(spawn_enemy,9.5,560,570)
    pyglet.clock.schedule_once(spawn_enemy,9.5,410,570)

    pyglet.clock.schedule_once(spawn_enemy,17.5,260,570)
    pyglet.clock.schedule_once(spawn_enemy,17.5,560,570)
    pyglet.clock.schedule_once(spawn_enemy,17.5,410,570)

    pyglet.clock.schedule_once(spawn_enemy,25.5,260,570)
    pyglet.clock.schedule_once(spawn_enemy,25.5,560,570)
    pyglet.clock.schedule_once(spawn_enemy,25.5,410,570)

    switch1=switch.Switch(770,90,'right')
    switch1.batch=main_batch
    game_objects.append(switch1)

    pyglet.clock.schedule_once(spawn_laser,.01,395,75)

    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)

def load_level_4(level):

    global game_objects, hidden, event_stack_size, player, boss1
    global tokens_collected, max_tokens, laser, switch1, portal1

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0
    
    game_objects=[]
    reload(world)
    world.generate_world(level)

    switch1=switch.Switch(1057,540,'left')
    switch1.batch=main_batch
    game_objects.append(switch1)

    boss1=boss.Boss(140,200)
    boss1.batch=main_batch
    game_objects.append(boss1)
    #pyglet.clock.schedule_once(spawn_boss,1,140,200)

    player=avatar.Avatar(batch=avatar_batch)
    game_objects.append(player)

    #gate1=gate.Gate(487,275)
    #gate1.batch=main_batch
    #game_objects.append(gate1)

    pyglet.clock.schedule_once(spawn_laser,.01,555,75)

    portal1=portal.Portal(3060,60)
    portal1.batch=main_batch
    game_objects.append(portal1)

    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)

def update(dt):

    global tokens_collected, max_tokens, level

    player_dead=False
    victory=False
    if switch1.flipped==True and level<4:
        portal1.x=1060
        portal1.update_bounding_box()
        if level==3:
            portal1.y=85
    elif switch1.flipped==True and level==4 and (boss1 in game_objects):
        #gate1.dead=True
        boss1.visible=True
        media_player2.pause()
        media_player3.play()
        #boss1.y=200
        #pyglet.clock.schedule_once(spawn_boss,1,140,200)
    #if hidden in game_objects:
       #if util.distance((player.x,player.y),(hidden.x,hidden.y))<=150:
            #hidden.found=True

    for i in xrange(len(game_objects)):
        for j in xrange(i+1,len(game_objects)):

            obj_1=game_objects[i]
            obj_2=game_objects[j]

            #make sure objects are not dead

            if not obj_1.dead and not obj_2.dead:
                if obj_1.__class__ is not obj_2.__class__:
                    if obj_1.collides_with(obj_2) or obj_2.collides_with(obj_1):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

    for obj in game_objects:
        obj.update(dt)

    #get rid of dead objects

    for to_remove in [obj for obj in game_objects if obj.dead]:

        #remove the object from the batch and the game_objects list
        to_remove.delete()
        game_objects.remove(to_remove)


        if to_remove==player:
            player_dead=True
            
        if isinstance(to_remove,portal.Portal):
            if level<4:
                gravity.toggle_gravity(player)
                victory=True
            elif level==4:
                victory=True

        if isinstance(to_remove,boss.Boss):
            media_player3.pause()
            media_player4.play()
            portal1.x=1060
            portal1.update_bounding_box()
        
        #Adjust the score if the dead item was worth points
        #if isinstance(to_remove,power_up.Power_up):
            #player.has_laser=True
            #tokens_collected+=1
            #gravity.toggle_gravity(player)
            #sound_fx.pop_sound.play()
            #score+=10
            #hud.score_label.text='Score:'+str(score)
            #if tokens_collected==max_tokens:
                #victory=True
            #    sound_fx.level_clear_sound.play()
        

        '''
        
        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,pwr_up.PwrUp):
            score+=to_remove.pt_value
            hud.score_label.text='Score:'+str(score)
            sound_fx.power_up_sound.play()
            avatar.process_power_up()'''

        #Adjust the score if the dead item was worth points
        #if isinstance(to_remove,enemy.Enemy):
            #sound_fx.pop_sound.play()
            #score+=to_remove.pt_value
            #score_label.text='Score:'+str(score)
        
        
        
    #check for win/lose conditions

    if player_dead:
        #if len(player_lives)>0:
        if media_player2.playing==True:
                media_player2.pause()
        elif media_player3.playing==True:
                media_player3.pause()
        media_player4.play()
        pyglet.clock.unschedule(spawn_enemy)
        pyglet.clock.unschedule(update)
        
        hud.game_over_label.y=viewport.v_ctr
    elif victory:
        pyglet.clock.unschedule(spawn_enemy)
        level+=1
        #hud.level_label.text='Level:'+str(level)
        #score+=level_clear_pts

        pyglet.clock.unschedule(update)
        clear_level()
        if level==2:
            load_level_2(level)
        elif level==3:
            load_level_3(level)
        elif level==4:
            load_level_4(level)
        else:
            media_player4.pause()
            media_player.play()
            hud.congrats_label.y=viewport.v_ctr
    
@viewport.window.event
def on_key_press(symbol,modifiers):
    global game_objects
    if inst.complete:
        if player.has_laser==True:
            if symbol==key.D:
                if player.image==avatar.avatar_left_laser:
                    #x_coord=avatar.player.left
                    beam=laser_shoot.Beam_Shoot((player.x-(player.width//2)),player.y)
                    sound_fx.pew_sound.play()
                    pyglet.clock.schedule_interval(beam.update,1.0/60.0)
                    game_objects.append(beam)
                elif player.image==avatar.avatar_right_laser:
                    #x_coord=avatar.player.right
                    beam=laser_shoot.Beam_Shoot((player.x+(player.width//2)),player.y)
                    sound_fx.pew_sound.play()
                    pyglet.clock.schedule_interval(beam.update,1.0/60.0)
                    game_objects.append(beam)
                else:
                    pass
        
@viewport.window.event
def on_draw():
    global bg
    viewport.window.clear()
    #if instructions are not complete, draw instructions
    if not inst.complete:
        inst_batch.draw()
    #if instructions are complete, draw everything else
    else:
        bg.draw()
        world.tile_batch.draw()
        hud.hud_batch.draw()
        #avatar.avatar_batch.draw()
        laser_shoot.laser_batch.draw()
        main_batch.draw()
    avatar_batch.draw()

@viewport.window.event
def on_close():
    viewport.window.close()
    quit()


#what does this do?
if __name__=='__main__':

    pyglet.gl.glClearColor(0.24,0.42,0.65,1.0)
    inst_batch=pyglet.graphics.Batch()
    main_batch=pyglet.graphics.Batch()
    avatar_batch=pyglet.graphics.Batch()
    

    init()
    pyglet.clock.schedule_interval(check_instructions,1/120.0)
    
    pyglet.app.run()
