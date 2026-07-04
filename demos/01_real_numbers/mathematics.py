"""

Project:
Algebraic vs Transcendental Space Mapping Visualization

Module:
mathematics.py

Description:
Generate mathematical trajectories.

Responsible for:
    - Time sequence
    - Algebraic irrational trajectories
    - Transcendental trajectories
    - Mathematical classifications

"""

import numpy as np

from config import *

time_steps = TIME_STEPS

def generate_algebraic_orbits():

    sqrt2_x = ALG_RADIUS_1 * np.cos(2 * time_steps)
    sqrt2_y = ALG_RADIUS_1 * np.sin(2 * time_steps)
    sqrt2_z = np.zeros(NUM_FRAMES)

    sqrt3_x = ALG_RADIUS_2 * np.cos(3 * time_steps)
    sqrt3_y = ALG_RADIUS_2 * np.sin(3 * time_steps)
    sqrt3_z = 0.8 * np.sin(time_steps)

    cbrt2_x = ALG_RADIUS_3 * np.cos(1.5 * time_steps)
    cbrt2_y = ALG_RADIUS_3 * np.sin(1.5 * time_steps)
    cbrt2_z = 1.2 * np.cos(2 * time_steps)

    return {

        "sqrt2": (sqrt2_x, sqrt2_y, sqrt2_z),

        "sqrt3": (sqrt3_x, sqrt3_y, sqrt3_z),

        "cbrt2": (cbrt2_x, cbrt2_y, cbrt2_z)

    }

def generate_transcendental_orbits():

    spiral_radius = 0.42 * time_steps

    trans_x = spiral_radius * np.cos(
        1.5 * time_steps
    )

    trans_y = spiral_radius * np.sin(
        1.5 * time_steps
    )

    trans_z = 0.42 * time_steps

    trans2_x = spiral_radius * np.cos(
        1.5 * time_steps + np.pi
    )

    trans2_y = spiral_radius * np.sin(
        1.5 * time_steps + np.pi
    )

    trans2_z = trans_z.copy()

    return {

        "pi": (trans_x, trans_y, trans_z),

        "e": (trans2_x, trans2_y, trans2_z)

    }

def draw_algebraic_skeleton(ax, algebraic):

    sqrt2 = algebraic["sqrt2"]
    sqrt3 = algebraic["sqrt3"]
    cbrt2 = algebraic["cbrt2"]

    ax.plot(

        sqrt2[0],
        sqrt2[1],
        sqrt2[2],

        color=ALG_COLOR,

        linewidth=0.7,

        alpha=0.18

    )

    ax.plot(

        sqrt3[0],
        sqrt3[1],
        sqrt3[2],

        color=ALG_COLOR2,

        linewidth=0.7,

        alpha=0.18

    )

    ax.plot(

        cbrt2[0],
        cbrt2[1],
        cbrt2[2],

        color=ALG_COLOR3,

        linewidth=0.7,

        alpha=0.18

    )


def draw_labels(ax, algebraic, transcendental):

    sqrt2 = algebraic["sqrt2"]
    sqrt3 = algebraic["sqrt3"]
    cbrt2 = algebraic["cbrt2"]

    pi_curve = transcendental["pi"]
    e_curve = transcendental["e"]

    ax.text(

        sqrt2[0][0],
        sqrt2[1][0],
        0.6,

        SQRT2_LABEL,

        color=ALG_COLOR

    )

    ax.text(

        sqrt3[0][0],
        sqrt3[1][0],
        0.8,

        SQRT3_LABEL,

        color=ALG_COLOR2

    )

    ax.text(

        cbrt2[0][0],
        cbrt2[1][0],
        1.2,

        CBRT2_LABEL,

        color=ALG_COLOR3

    )

    ax.text(

        pi_curve[0][10],
        pi_curve[1][10],
        pi_curve[2][10],

        PI_LABEL,

        color=TRANS_COLOR

    )

    ax.text(

        e_curve[0][10],
        e_curve[1][10],
        e_curve[2][10],

        E_LABEL,

        color=TRANS_COLOR2

    )

def get_number_tree():

    return NUMBER_TREE

def generate_smoke(x, y, z):

    smoke_x = x + rng.normal(

        0,

        SMOKE_SIGMA,

        len(x)

    )

    smoke_y = y + rng.normal(

        0,

        SMOKE_SIGMA,

        len(y)

    )

    smoke_z = z + rng.normal(

        0,

        SMOKE_SIGMA,

        len(z)

    )

    return smoke_x, smoke_y, smoke_z

def get_physics_mapping():

    return {

        "Base Field": BASE_FIELD,

        "Real Field": REAL_FIELD,

        "Algebraic Dimension": ALGEBRAIC_DIMENSION,

        "Transcendental Dimension": TRANSCENDENTAL_DIMENSION,

        "Algebraic Relaxation": ALGEBRAIC_RELAXATION,

        "Transcendental Relaxation": TRANSCENDENTAL_RELAXATION

    }

print("=" * 60)
print("Mathematical trajectories initialized.")
print("=" * 60)