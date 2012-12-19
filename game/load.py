# -*- coding: utf-8 *-*

import pyglet
from . import util
from . import resources
from . import physicalobject
from . import ship as ship_
import random


def asteroid(player_pos=(-1000,-1000), screensize=(800,600), score=0, *args, **kwargs):
    """spawns an asteroid at random position"""

    pos = util.random_pos(screensize)
    while util.distance(pos, player_pos) < 300:
        pos = util.random_pos(screensize)

    max_speed = 90 + score * 3

    vel = [random.randrange(-max_speed, max_speed) for i in (0,1)]
    #vel = [0,0]

    rotation_speed = random.randrange(-250, 250)
    img = random.sample(resources.asteroid_images, 1)[0]

    asteroid = physicalobject.PhysicalObject(vel=vel, rotation_speed=rotation_speed, x=pos[0], y=pos[1],
            img=img, screensize=screensize, *args, **kwargs)
    return asteroid


def ship(screensize=(800,600), *args, **kwargs):
    myship = ship_.Ship(img=resources.ship_image, rotation=-90, x=screensize[0]/2, y=screensize[1]/2,
        thrust_image=resources.ship_thrust, screensize=screensize, *args, **kwargs)
    return myship


def debris(screensize=(800,600), *args, **kwargs):
    """
    A bunch of rock fullscreen images that shift right underground
    """
    image = resources.debris_image
    image.anchor_x = image.width
    image.anchor_y = 0

    debris = []
    for i in (0, 1):
        x0 = -i * screensize[0]
        frame = physicalobject.ScaledMovingSprite(img=image, vel=(30, 0), x=x0, screensize=screensize, *args, **kwargs)
        debris.append(frame)

    return debris


class ClickableSprite(pyglet.sprite.Sprite):
    def __init__(self, hook_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hook_function = hook_function

    def on_mouse_press(self, x, y, button, modifiers):
        print("ciao")
        if not self.visible:
            return
        x0 = self.x - self.width / 2.0
        x1 = x0 + self.width
        y0 = self.y - self.height / 2.0
        y1 = y0 + self.height

        if (x0 <= x <= x1) and (y0 <= y <= y1):
            self.visible = False
            self.hook_function()

