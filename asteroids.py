#!/usr/bin/env python3
# -*- coding: utf-8 *-*

import pyglet
from pyglet import window, app, graphics, clock, text
from game import load, resources, physicalobject

MAX_ROCKS = 12
LIVES = 3


class Game(window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # batch for efficient drawing
        self.batch = graphics.Batch()
        background = graphics.OrderedGroup(0)
        foreground = graphics.OrderedGroup(1)

        self.gamelayer = graphics.OrderedGroup(2)

        toplayer = graphics.OrderedGroup(3)

        # window size
        self.size = self.get_size()

        # start with empty asteroid set
        self.asteroids = set()

        # empty explosions set
        self.explosions = set()

        # background and moving foreground sprites
        self.background = physicalobject.ScaledMovingSprite(img=resources.background_image,
                screensize=self.size, batch=self.batch, group=background)
        self.debris = load.debris(screensize=self.size, batch=self.batch, group=foreground)
        self.splashscreen = load.ClickableSprite(hook_function=self.start,
                img=resources.splashscreen,
                x = self.size[0] / 2.0, y=self.size[1] / 2.0,
                batch=self.batch, group=toplayer)


        # player ship
        self.player = load.ship(screensize=self.size, batch=self.batch, group=self.gamelayer)

        self.score = 0
        self.lives = LIVES
        self.started = False

        self.fps_display = clock.ClockDisplay()

        # Lives and score labels
        self.lives_label = text.Label(font_size=20, text="Lives: %d" % self.lives, x=40, y=self.size[1]-40,
                    batch=self.batch, group=toplayer)
        self.score_label = text.Label(font_size=20, anchor_x='right', text="Score: %d" % self.score, x=self.size[0]-40,
                    y=self.size[1]-40, batch=self.batch, group=toplayer)

        self.push_handlers(self.player)
        self.push_handlers(self.splashscreen)

        # add event handlers to the ship and splashscreen
        joysticks = pyglet.input.get_joysticks()
        for joystick in joysticks:
            joystick.open()
            joystick.push_handlers(self.player)

        # spawn a new asteroid each second
        clock.schedule_interval(self.spawn_asteroid, 1)

        # update function
        # upstream bug: more than 60hz and joypad stops generating events!
        clock.schedule_interval(self.update, 1 / 60)


    def start(self):
        self.score = 0
        self.lives = LIVES
        self.started = True
        self.splashscreen.visible = False
        resources.soundtrack.seek(0)
        resources.soundtrack.play()


    def stop(self):
        self.asteroids = set()
        self.started = False
        self.splashscreen.visible = True
        self.player.opacity = 255


    def spawn_asteroid(self, dt=0):
        if not self.started:
            return

        if len(self.asteroids) < MAX_ROCKS:
            asteroid = load.asteroid(self.player.position, screensize=self.size, score=self.score,
                        batch=self.batch, group=self.gamelayer)
            self.asteroids.add(asteroid)


    def on_draw(self):
        self.batch.draw()
        self.fps_display.draw()


    def update(self, dt):
        """update positions for objects and check collisions"""
        for group in ([self.player], self.debris, self.asteroids, self.explosions):
            physicalobject.process_sprite_group(group, dt)

        bullet_explosions = physicalobject.group_group_collide(self.player.bullets, self.asteroids)
        self.explosions.update(bullet_explosions)
        self.score += len(bullet_explosions)

        if self.player.opacity == 255:
            # Look if ship collides with asteroids
            ship_explosions = physicalobject.group_collide(self.asteroids, self.player)
            self.explosions.update(ship_explosions)

            if len(ship_explosions):
                # ship destroyed!
                self.explosions.add(self.player.destroy())
                self.lives -= 1
                self.player.invulnerable(5)
                if self.lives == 0:
                    # game over
                    self.stop()

        self.score_label.text = "Score: %d" % self.score
        self.lives_label.text = "Lives: %d" % self.lives


if __name__ == '__main__':
    #game = Game(fullscreen=True)
    game = Game(800, 600)

    app.run()
