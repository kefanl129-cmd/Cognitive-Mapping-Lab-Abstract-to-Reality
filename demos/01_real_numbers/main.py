"""
main.py

Program Entry

Responsibilities:

1. Create Scene
2. Create Objects
3. Generate Mathematical Models
4. Start Animation
5. Show Visualization
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from config import *

from scene import create_scene

from objects import create_objects

from mathematics import (
    generate_algebraic_orbits,
    generate_transcendental_orbits,
    draw_algebraic_skeleton,
    draw_labels
)

from animation import update

scene = create_scene()

fig = scene["fig"]
ax = scene["ax"]
info_text = scene["info_text"]

objects = create_objects(ax)

algebraic = generate_algebraic_orbits()

transcendental = generate_transcendental_orbits()

draw_algebraic_skeleton(ax, algebraic)

draw_labels(ax, algebraic, transcendental)

ani = FuncAnimation(

    fig,

    lambda frame: update(

        frame,

        ax,

        info_text,

        algebraic,

        transcendental,

        objects

    ),

    frames=NUM_FRAMES,

    interval=INTERVAL,

    blit=False,

    repeat=True

)

plt.tight_layout()

plt.show()