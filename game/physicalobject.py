# -*- coding: utf-8 *-*

import pyglet
from . import util, resources

# update and collision helper functions
def process_sprite_group(group, dt):
    """
    calls update for the whole group and removes after who returns True
    """
    for item in set(group):
        if item.update(dt):
            item.visible=False
            group.remove(item)


def group_collide(group, other_object):
    """
    Check collision between a group and another object
    returns how many object collided
    removes the collided object in the group and calls
    method "destroy" in them
    """
    collided = set()
    for item in set(group):
        if item.collide(other_object):
            collided.add(item.destroy())
            group.remove(item)

    # remove collide objects from group
    return collided


def group_group_collide(group1, group2):
    """
    For each item in group1 calls group collide
    if a collision happened destroy the item
    """
    collided = set()
    for item in set(group1):
        c = group_collide(group2, item)
        if len(c) > 0:
            collided.update(c)
            group1.remove(item)
    return collided


class MovingSprite(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity, and angle velocity"""
    def __init__(self, rotation=0, vel=(0,0), rotation_speed=0, screensize=(800, 600), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.screensize = screensize
        # Velocity
        self.vel = list(vel)
        # Angle (pyglet uses negative degrees)
        self.rotation = rotation
        self.rotation_speed = rotation_speed


    def update(self, dt):
        # rotate object
        self.rotation += self.rotation_speed * dt

        # Update position according to velocity and time
        self.x = (self.x + self.vel[0] * dt) % (self.screensize[0] + self.width)
        self.y = (self.y + self.vel[1] * dt) % (self.screensize[1] + self.height)

        # update methods could be checked for expiring
        return False

class ScaledMovingSprite(MovingSprite):
    """A Fullscreen Moving sprite"""

    def __init__(self, radius=None, lifespan=float("inf"), *args, **kwargs):
        """
        Interesting super() params: rotation=0, vel=(0,0), rotation_speed=0, screensize=(800, 600)
        """
        super().__init__(*args, **kwargs)
        self.scale = self.screensize[0] / self.image.width


class PhysicalObject(MovingSprite):
    """A Moving sprite with collision and expiring"""

    def __init__(self, radius=None, lifespan="inf", *args, **kwargs):
        """
        Interesting super() params: rotation=0, vel=(0,0), rotation_speed=0, screensize=(800, 600)
        """
        super().__init__(*args, **kwargs)

        # collision radius
        if radius:
            self.radius = radius
        else:
            self.radius = (max(self.width, self.height) / 2) * self.scale

        # track how much it should last before disappearing
        self.lifespan = float(lifespan)
        self.age = float(0)

    def update(self, dt):
        super().update(dt)
        # age the object
        self.age += dt
        return (self.age > self.lifespan) # update could be checked for expiring


    def collide(self, other_object):
        """Determine if this object collides with another"""

        # Calculate distance between object centers that would be a collision,
        # assuming circular images
        collision_distance = self.radius * self.scale + other_object.radius * other_object.scale

        # Get distance using position tuples
        actual_distance = util.distance(self.position, other_object.position)

        # update methods could be checked for expiring
        return (actual_distance <= collision_distance)


    def destroy(self):
        self.visible = False

        pos = list(self.position)
        vel = (self.vel[0]/2, self.vel[1] / 2)

        explosion = PhysicalObject(img=resources.explosion_animation,
                vel=vel, screensize=self.screensize, x=pos[0], y=pos[1],
                batch=self.batch, group=self.group, lifespan=1)

        resources.explosion_sound.play()

        return explosion

