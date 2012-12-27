#!/usr/bin/env python

import pyglet

joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]
joystick.open()

class JoyController(object):
    def on_joyaxis_motion(self, joystick, axis, value):
        print('motion', axis, value)

    def on_joybutton_press(self, joystick, button):
        print('button press', button)

    def on_joybutton_release(self, joystick, button):
        print('button release', button)

    def on_joyhat_motion(joystick, hat_x, hat_y):
        print('joyhat', hat_x, hat_y)

joystick.push_handlers(JoyController())
pyglet.app.run()


