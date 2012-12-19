from . import physicalobject

new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
class Asteroid(physicalobject.PhysicalObject):
    def destroy(self):
        # spawn explosion
        explosion = Sprite(list(item.pos), (0,0), 0, 0, explosion_image, explosion_info, explosion_sound)
        explosion_group.add(explosion)
        if item.do_divide and item.scale > 0.25:
            rock0 = Sprite(list(item.pos), item.vel, item.angle, item.angle_vel, asteroid_image, asteroid_info, None, True, item.scale /2)
            rock1 = Sprite(list(item.pos), (- item.vel[0], -item.vel[1]), -item.angle, -item.angle_vel, asteroid_image, asteroid_info, None, True, item.scale /2)
            rock_group.update((rock0, rock1))

