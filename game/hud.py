#hud.py

import pyglet,viewport

pyglet.font.add_file('font/rennie.ttf')
rennie = pyglet.font.load('Rennie Mackintosh ITC Bold')

#arial = font.load('Arial', 14, bold=True, italic=False)

hud_batch=pyglet.graphics.Batch()

'''
instantiate all of your labels and or graphic icons here

make sure to set all of their batch attributes to hud_batch

do not draw them in this module

in the topfile, add hud_batch.draw() to the on_draw handler
'''

'''score_label=pyglet.text.Label(text='Score: 0',
                              anchor_x='left',
                              anchor_y='top',
                              x=0,
                              y=viewport.window.height,
                              font_size=24,
                              font_name='Rennie Mackintosh ITC Bold',
                              batch=hud_batch)'''

health_label=pyglet.text.Label(text='Health:',
                              anchor_x='left',
                              anchor_y='top',
                              x=280,
                              y=640,
                              color=(255, 0, 255, 255),
                              font_name='Rennie Mackintosh ITC Bold',
                              font_size=24,
                              batch=hud_batch)


game_over_label=pyglet.text.Label(text='GAME OVER',
                                  anchor_x='center',
                                  anchor_y='center',
                                  x=viewport.h_ctr,
                                  y=-300,
                                  color=(255, 0, 255, 255),
                                  font_size=120,
                                  font_name='Rennie Mackintosh ITC Bold',
                                  batch=hud_batch)

congrats_label=pyglet.text.Label(text='''CONGRATULATIONS!!!!! Now all space hedgehogs can live in peace!''', 
                                  anchor_x='center',
                                  anchor_y='center',
                                  x=viewport.h_ctr,
                                  y=-300,
                                  color=(255, 0, 255, 255),
                                  font_size=50,
                                  multiline=True,
                                  width=900,
                                  font_name='Rennie Mackintosh ITC Bold',
                                  batch=hud_batch)
