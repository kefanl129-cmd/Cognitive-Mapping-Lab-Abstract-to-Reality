"""

Project:
Algebraic vs Transcendental Space Mapping Visualization

Module:
scene.py

Description:
Create 3D scene.

Responsible for:
    - Figure
    - Axes
    - Rational Grid
    - Real Sphere
    - Algebraic Sphere
    - Labels
    - Legend
    - Dynamic Objects

"""

import numpy as np
import matplotlib.pyplot as plt

from config import *

plt.style.use("dark_background")


def create_scene():

    fig = plt.figure(
        figsize=FIG_SIZE,
        facecolor=BACKGROUND_COLOR
    )

    ax = fig.add_subplot(
        111,
        projection="3d",
        facecolor=BACKGROUND_COLOR
    )

    ax.set_xlim(-SPACE_SIZE, SPACE_SIZE)
    ax.set_ylim(-SPACE_SIZE, SPACE_SIZE)
    ax.set_zlim(-SPACE_SIZE, SPACE_SIZE)

    ax.axis("off")

    fig.suptitle(
        TITLE,
        fontsize=TITLE_SIZE,
        color="white",
        fontweight="bold"
    )

    info_text = ax.text2D(
        0.02,
        0.02,
        "",
        transform=ax.transAxes,
        fontsize=10,
        color=INFO_COLOR,
        family="monospace"
    )

    ax.scatter(
        [0],
        [0],
        [0],
        s=260,
        color=Q_COLOR,
        edgecolors="white",
        linewidth=2,
        label="Field Q"
    )


    qx = []
    qy = []
    qz = []

    for i in range(-5, 6):
        for j in range(-5, 6):
            qx.append(i)
            qy.append(j)
            qz.append(0)

    ax.scatter(
        qx,
        qy,
        qz,
        s=8,
        color=Q_COLOR,
        alpha=GRID_ALPHA,
        label="Rational Numbers"
    )

    u, v = np.mgrid[
        0:2*np.pi:45j,
        0:np.pi:25j
    ]

    real_x = REAL_RADIUS * np.cos(u) * np.sin(v)
    real_y = REAL_RADIUS * np.sin(u) * np.sin(v)
    real_z = REAL_RADIUS * np.cos(v)

    ax.plot_wireframe(
        real_x,
        real_y,
        real_z,
        color="white",
        linewidth=0.3,
        alpha=0.05
    )

    alg_x = ALG_RADIUS * np.cos(u) * np.sin(v)
    alg_y = ALG_RADIUS * np.sin(u) * np.sin(v)
    alg_z = ALG_RADIUS * np.cos(v)

    ax.plot_wireframe(
        alg_x,
        alg_y,
        alg_z,
        color=ALG_COLOR,
        linewidth=0.5,
        alpha=0.10
    )

    ax.text(
        0,
        0,
        13,
        REAL_LABEL,
        color="white",
        fontsize=12
    )

    ax.text(
        0,
        0,
        6,
        ALG_LABEL,
        color=ALG_COLOR,
        fontsize=11
    )

    ax.text(
        0,
        0,
        0.6,
        BASE_LABEL,
        color=Q_COLOR,
        fontsize=14
    )

    sqrt2_particle = ax.scatter([], [], [], s=60,
                                color=ALG_COLOR,
                                label="√2")

    sqrt3_particle = ax.scatter([], [], [], s=60,
                                color=ALG_COLOR2,
                                label="√3")

    cbrt2_particle = ax.scatter([], [], [], s=60,
                                color=ALG_COLOR3,
                                label="∛2")

    trans_line, = ax.plot([], [], [],
                          color=TRANS_COLOR,
                          linewidth=2.5,
                          label="π")

    trans_head = ax.scatter([], [], [],
                            s=120,
                            color="white",
                            edgecolors=TRANS_COLOR)

    trans_line2, = ax.plot([], [], [],
                           color=TRANS_COLOR2,
                           linewidth=2,
                           label="e")

    trans_head2 = ax.scatter([], [], [],
                             s=90,
                             color=TRANS_HEAD2)

    fluid_cluster = ax.scatter([], [], [],
                               s=15,
                               color=TRANS_COLOR,
                               alpha=0.25)

    tail_line, = ax.plot([], [], [],
                         color=TRANS_COLOR,
                         linewidth=1.8,
                         alpha=0.45)


    legend = ax.legend(
        loc="upper left",
        fontsize=10,
        facecolor="black",
        edgecolor="#444444"
    )

    for txt in legend.get_texts():
        txt.set_color("white")


    return {
        "fig": fig,
        "ax": ax,
        "info_text": info_text,
        "sqrt2_particle": sqrt2_particle,
        "sqrt3_particle": sqrt3_particle,
        "cbrt2_particle": cbrt2_particle,
        "trans_line": trans_line,
        "trans_head": trans_head,
        "trans_line2": trans_line2,
        "trans_head2": trans_head2,
        "fluid_cluster": fluid_cluster,
        "tail_line": tail_line
    }