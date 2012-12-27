# -*- coding: utf-8 *-*

import pyglet
from . import util

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects
asteroid_images = {util.center_image(pyglet.resource.image(image)) for image in
        ("asteroid_blend.png", "asteroid_blue.png", "asteroid_brown.png")}

double_ship = pyglet.resource.image("double_ship.png")
ship_grid = pyglet.image.ImageGrid(image=double_ship, rows=1, columns=2)
ship_image, ship_thrust = [util.center_image(img) for img in ship_grid]

shot_image = util.center_image(pyglet.resource.image("shot2.png"))

explosion_image = pyglet.resource.image("explosion.hasgraphics.png")
_explosion_seq = [util.center_image(img) for img in pyglet.image.ImageGrid(explosion_image, 9, 9)]
# revert column wise the sequence
explosion_seq = [_explosion_seq[9*(j-1) + i] for j in range(9, 0, -1) for i in range(9)]
explosion_animation = pyglet.image.Animation.from_image_sequence(explosion_seq, 1 / 60.0)

background_image = pyglet.resource.image("nebula_blue.png")
debris_image = pyglet.resource.image("debris1_blue.png")
splashscreen = util.center_image(pyglet.resource.image("splash.png"))


bullet_sound = pyglet.resource.media("missile.wav", streaming=False)
explosion_sound = pyglet.resource.media("explosion.wav", streaming=False)


thrust_sound = pyglet.media.Player()
thrust_sound.queue(pyglet.resource.media("thrust.wav", streaming=False))
thrust_sound.eos_action = thrust_sound.EOS_LOOP

soundtrack = pyglet.media.Player()
soundtrack.queue(pyglet.resource.media("soundtrack.wav"))
soundtrack.eos_action = soundtrack.EOS_LOOP

