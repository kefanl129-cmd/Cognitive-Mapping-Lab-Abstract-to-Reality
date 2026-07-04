"""
animation.py

Animation Engine

Responsible for:

1. Algebraic Irrational Motion
2. Transcendental Motion
"""

import numpy as np

from config import *

def update_algebraic(
    frame,
    algebraic,
    objects
):
    """
    Update algebraic irrational particles.

    Parameters
    ----------
    frame : int

    algebraic : dict

    objects : dict
    """

    sqrt2 = algebraic["sqrt2"]
    sqrt3 = algebraic["sqrt3"]
    cbrt2 = algebraic["cbrt2"]

    # √2
    objects["sqrt2_particle"].set_offsets(
        np.array([sqrt2[0][frame], sqrt2[1][frame]])
    )

    objects["sqrt2_particle"].set_3d_properties(
        [sqrt2[2][frame]],
        zdir="z"
    )

    # √3
    objects["sqrt3_particle"].set_offsets(
        np.array([sqrt3[0][frame], sqrt3[1][frame]])
    )

    objects["sqrt3_particle"].set_3d_properties(
        [sqrt3[2][frame]],
        zdir="z"
    )

    # ∛2
    objects["cbrt2_particle"].set_offsets(
        np.array([cbrt2[0][frame], cbrt2[1][frame]])
    )

    objects["cbrt2_particle"].set_3d_properties(
        [cbrt2[2][frame]],
        zdir="z"
    )

def update_transcendental(
    frame,
    transcendental,
    objects
):
    """
    Update transcendental trajectories.

    π
    e
    """

    pi_curve = transcendental["pi"]

    current_x = pi_curve[0][:frame + 1]
    current_y = pi_curve[1][:frame + 1]
    current_z = pi_curve[2][:frame + 1]

    objects["trans_line"].set_data(
        current_x,
        current_y
    )

    objects["trans_line"].set_3d_properties(
        current_z
    )

    objects["trans_head"].set_offsets(
        np.array([
            [
                pi_curve[0][frame],
                pi_curve[1][frame]
            ]
        ])
    )

    objects["trans_head"].set_3d_properties(
        [pi_curve[2][frame]],
        zdir="z"
    )


    e_curve = transcendental["e"]

    current_x2 = e_curve[0][:frame + 1]
    current_y2 = e_curve[1][:frame + 1]
    current_z2 = e_curve[2][:frame + 1]

    objects["trans_line2"].set_data(
        current_x2,
        current_y2
    )

    objects["trans_line2"].set_3d_properties(
        current_z2
    )

    objects["trans_head2"].set_offsets(
        np.array([
            [
                e_curve[0][frame],
                e_curve[1][frame]
            ]
        ])
    )

    objects["trans_head2"].set_3d_properties(
        [e_curve[2][frame]],
        zdir="z"
    )


def update_tail(
    frame,
    transcendental,
    objects
):
    """
    Update trajectory tail.
    """

    pi_curve = transcendental["pi"]

    tail = objects["tail_cache"]

    tail["x"].append(pi_curve[0][frame])
    tail["y"].append(pi_curve[1][frame])
    tail["z"].append(pi_curve[2][frame])

    if len(tail["x"]) > TAIL_LENGTH:

        tail["x"].pop(0)
        tail["y"].pop(0)
        tail["z"].pop(0)

    objects["tail_line"].set_data(

        tail["x"],
        tail["y"]

    )

    objects["tail_line"].set_3d_properties(

        tail["z"]

    )

def update_smoke(
    frame,
    transcendental,
    objects
):
    """
    Update transcendental fluid effect.
    """

    pi_curve = transcendental["pi"]

    current_x = pi_curve[0][:frame + 1]
    current_y = pi_curve[1][:frame + 1]
    current_z = pi_curve[2][:frame + 1]

    smoke_x = current_x + np.random.normal(
        0,
        SMOKE_SIGMA,
        len(current_x)
    )

    smoke_y = current_y + np.random.normal(
        0,
        SMOKE_SIGMA,
        len(current_y)
    )

    smoke_z = current_z + np.random.normal(
        0,
        SMOKE_SIGMA,
        len(current_z)
    )

    objects["fluid_cluster"].set_offsets(

        np.column_stack(

            (

                smoke_x,

                smoke_y

            )

        )

    )

    objects["fluid_cluster"].set_3d_properties(

        smoke_z,

        zdir="z"

    )


def update_info(
    frame,
    t,
    info_text
):
    """
    Refresh information panel.
    """

    info = f"""
FIELD EXTENSION SPACE

Time
----------------------------------------
t = {t:.2f}

Hierarchy
----------------------------------------
ℚ ⊂ ℝ

ℝ = Rational ∪ Irrational

Algebraic Irrational
----------------------------------------
√2
√3
∛2

Transcendental
----------------------------------------
π
e

Physics-inspired Conceptual Mapping
----------------------------------------
Rigid Algebraic Constraint

Finite-dimensional Extension

Free Transcendental Expansion

Infinite-dimensional Evolution

Frame
----------------------------------------
{frame + 1} / {NUM_FRAMES}
"""

    info_text.set_text(info)



def update_camera(
    ax,
    frame,
    t
):
    """
    Update camera motion.
    """

    elev = 20 + 6 * np.sin(t * 0.15)

    azim = frame * ROTATE_SPEED

    ax.view_init(
        elev=elev,
        azim=azim
    )


def update_glow(
    t,
    objects
):
    """
    Dynamic glow effect.
    """

    pulse = 1 + 0.25 * np.sin(4 * t)

    objects["sqrt2_particle"].set_sizes(
        [ALG_GLOW * pulse]
    )

    objects["sqrt3_particle"].set_sizes(
        [ALG_GLOW * pulse]
    )

    objects["cbrt2_particle"].set_sizes(
        [ALG_GLOW * pulse]
    )

    objects["trans_head"].set_sizes(
        [
            TRANS_GLOW *
            (
                1 +
                0.15 *
                np.cos(3 * t)
            )
        ]
    )

    objects["trans_head2"].set_sizes(
        [
            TRANS_GLOW *
            (
                1 +
                0.15 *
                np.sin(3 * t)
            )
        ]
    )


def update(
    frame,
    ax,
    info_text,
    algebraic,
    transcendental,
    objects
):
    """
    Master animation update function.
    """

    t = TIME_STEPS[frame]

    update_algebraic(
        frame,
        algebraic,
        objects
    )

    update_transcendental(
        frame,
        transcendental,
        objects
    )

    update_tail(
        frame,
        transcendental,
        objects
    )

    update_smoke(
        frame,
        transcendental,
        objects
    )


    update_info(
        frame,
        t,
        info_text
    )

 
  

    update_camera(
        ax,
        frame,
        t
    )


    update_glow(
        t,
        objects
    )



    return (

        objects["sqrt2_particle"],

        objects["sqrt3_particle"],

        objects["cbrt2_particle"],

        objects["trans_line"],

        objects["trans_line2"],

        objects["trans_head"],

        objects["trans_head2"],

        objects["fluid_cluster"],

        objects["tail_line"],

        info_text

    )