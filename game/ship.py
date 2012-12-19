# -*- coding: utf-8 *-*

from pyglet.window import key
from . import util, physicalobject
from . import resources

class Ship(physicalobject.PhysicalObject):
    """A class for the player"""
    def __init__(self, thrust_image=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set some easy-to-tweak constants
        # play values
        self.rotate_speed = 170.0
        self.bullet_speed = 500.0
        self.thrust_acc = 500
        self.friction = 0.95
        self.bullet_duration = 0.6

        self.thrust = False
        self.thrust_image = thrust_image
        self.normal_image = self.image

        self.bullets = set() # FIXME: bullet by OOT


    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.shoot()
        elif symbol == key.LEFT:
            self.turn(-1)
        elif symbol == key.RIGHT:
            self.turn(1)
        elif symbol == key.UP:
            self.set_thrust(True)


    def on_key_release(self, symbol, modifiers):
        if symbol in (key.LEFT, key.RIGHT):
            self.turn(0)
        elif symbol == key.UP:
            self.set_thrust(False)


    def update(self, dt):
        super().update(dt)
        if self.thrust and self.thrust_image:
            self.image = self.thrust_image
        else:
            self.image = self.normal_image

        # update velocity
        if self.thrust:
            acc = util.angle_to_vector(self.rotation)
            for i in (0,1):
                self.vel[i] += acc[i] * self.thrust_acc * dt

        # add friction
        for i in (0,1):
            self.vel[i] *= (1 - self.friction * dt)

        for bullet in set(self.bullets):
            if bullet.update(dt):
                self.bullets.remove(bullet)

        return False

    def set_thrust(self, on):
        self.thrust = on
        if on:
            resources.thrust_sound.seek(0)
            resources.thrust_sound.play()
        else:
            resources.thrust_sound.pause()

    def turn(self, clockwise):
        self.rotation_speed = clockwise * self.rotate_speed


    def shoot(self):
        resources.bullet_sound.play()

        forward = util.angle_to_vector(self.rotation)

        bullet_pos = [self.x + self.radius * forward[0], self.y + self.radius * forward[1]]
        bullet_vel = [self.vel[0] + self.bullet_speed * forward[0], self.vel[1] + self.bullet_speed * forward[1]]
        bullet = physicalobject.PhysicalObject(lifespan=self.bullet_duration, vel=bullet_vel, x=bullet_pos[0], y=bullet_pos[1],
            img=resources.shot_image, batch=self.batch, group=self.group, screensize=self.screensize)
        self.bullets.add(bullet)

    def destroy(self):
        explosion = super().destroy()
        self.rotation = -90
        self.x = self.screensize[0] / 2
        self.y = self.screensize[1] / 2
        self.vel = [0, 0]
        self.visible = True
        return explosion

