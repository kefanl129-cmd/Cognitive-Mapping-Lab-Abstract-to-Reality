"""

Project:
Algebraic vs Transcendental Space Mapping Visualization

Module:
objects.py

Description:
Create all dynamic objects.

Responsible for:
    - Algebraic particles
    - Transcendental trajectories
    - Particle heads
    - Fluid particles
    - Tail

"""

from config import *

def create_objects(ax):

    sqrt2_particle = ax.scatter(
        [], [], [],
        s=60,
        color=ALG_COLOR,
        label="√2"
    )

    sqrt3_particle = ax.scatter(
        [], [], [],
        s=60,
        color=ALG_COLOR2,
        label="√3"
    )

    cbrt2_particle = ax.scatter(
        [], [], [],
        s=60,
        color=ALG_COLOR3,
        label="∛2"
    )

    trans_line, = ax.plot(
        [], [], [],
        color=TRANS_COLOR,
        linewidth=2.5,
        label="π"
    )

    trans_head = ax.scatter(
        [], [], [],
        s=120,
        color="white",
        edgecolors=TRANS_COLOR,
        linewidth=2
    )


    trans_line2, = ax.plot(
        [], [], [],
        color=TRANS_COLOR2,
        linewidth=2,
        alpha=0.7,
        label="e"
    )

    trans_head2 = ax.scatter(
        [], [], [],
        s=90,
        color=TRANS_HEAD2
    )



    fluid_cluster = ax.scatter(
        [], [], [],
        s=15,
        color=TRANS_COLOR,
        alpha=0.25
    )

    tail_line, = ax.plot(
        [], [], [],
        linewidth=1.8,
        color=TRANS_COLOR,
        alpha=0.45
    )

    tail_cache = {

        "x": [],

        "y": [],

        "z": []

    }


    return {

        "sqrt2_particle": sqrt2_particle,

        "sqrt3_particle": sqrt3_particle,

        "cbrt2_particle": cbrt2_particle,

        "trans_line": trans_line,

        "trans_head": trans_head,

        "trans_line2": trans_line2,

        "trans_head2": trans_head2,

        "fluid_cluster": fluid_cluster,

        "tail_line": tail_line,

        "tail_cache": tail_cache

    }