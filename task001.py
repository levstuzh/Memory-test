import pyglet
from pyglet import shapes
from pyglet.window import mouse
import random
window = pyglet.window.Window(width=800, height=600, caption="Hello!")
window.set_location(x=300, y=200)
batch = pyglet.graphics.Batch()
m = []
for key in m:
    ...
_x = 60
_y = 500
for i in range(4):
    for j in range(3):
        circle = shapes.Rectangle(x = _x, y = _y, width=40, height=40, batch=batch)
        m.append(circle)
        _x+=50
    _y-=60
    _x=60
@window.event
def on_draw():
    for j in m:
        j.draw()
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button & mouse.LEFT:
        for u in m:
            u.color=(255,0,0)
    if button & mouse.RIGHT:
        for c in m:
            c.color=(0,255,0)
def shuffle_keys(target_key, x_y):
    run = True
    while run:
        if target_key.x < x_y[0]:
            target_key.x+1
        if

pyglet.app.run()
