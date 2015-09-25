#sound_fx.py

import pyglet

theme=pyglet.resource.media('sounds/dragonborn.mp3')
combat=pyglet.resource.media('sounds/combat.mp3')
boss=pyglet.resource.media('sounds/boss.mp3')
relax=pyglet.resource.media('sounds/relax.mp3')

pop_sound=pyglet.media.load('sounds/pop.wav',streaming=False)
pew_sound=pyglet.media.load('sounds/laser.wav',streaming=False)
switch_sound=pyglet.media.load('sounds/switch.wav',streaming=False)
ping=pyglet.media.load('sounds/ping.wav',streaming=False)

