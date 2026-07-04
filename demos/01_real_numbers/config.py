"""
==========================================================
Project:
Algebraic vs Transcendental Space Mapping Visualization

Module:
config.py

Description:
Global configuration file.

All global parameters are managed here:
    - Space
    - Animation
    - Colors
    - Physics-inspired conceptual mapping
    - Rendering

"""

import numpy as np


FIG_SIZE = (14, 10)

BACKGROUND_COLOR = "black"

TITLE = (
    "Field Extension Space Mapping\n"
    "Rational → Algebraic Irrational → Transcendental"
)

TITLE_SIZE = 18


SPACE_SIZE = 15

REAL_RADIUS = 12

ALG_RADIUS = 5


ALG_RADIUS_1 = 5.0      # √2

ALG_RADIUS_2 = 4.2      # √3

ALG_RADIUS_3 = 5.8      # ∛2


NUM_FRAMES = 400

FPS = 30

INTERVAL = 40

TIME_END = 12 * np.pi

TIME_STEPS = np.linspace(
    0,
    TIME_END,
    NUM_FRAMES
)


TAIL_LENGTH = 45


ALG_GLOW = 65

TRANS_GLOW = 130

SMOKE_SIGMA = 0.28


Q_COLOR = "#FFD700"

REAL_COLOR = "#FFFFFF"

ALG_COLOR = "#00FFFF"

ALG_COLOR2 = "#66FFFF"

ALG_COLOR3 = "#00AAFF"

TRANS_COLOR = "#FF00FF"

TRANS_COLOR2 = "#FF66FF"

TRANS_HEAD = "#FFFFFF"

TRANS_HEAD2 = "#FF99FF"

INFO_COLOR = "#00FFCC"

GRID_ALPHA = 0.35



BASE_FIELD = "ℚ"

REAL_FIELD = "ℝ"

ALGEBRAIC_RELAXATION = 0.0

TRANSCENDENTAL_RELAXATION = np.inf

ALGEBRAIC_DIMENSION = "Finite"

TRANSCENDENTAL_DIMENSION = "Infinite"



RNG_SEED = 2026

rng = np.random.default_rng(RNG_SEED)


INIT_ELEV = 22

INIT_AZIM = 30

ROTATE_SPEED = 0.45

REAL_LABEL = "Real Field R"

ALG_LABEL = "Finite Algebraic Extension"

BASE_LABEL = "Q"

SQRT2_LABEL = "√2"

SQRT3_LABEL = "√3"

CBRT2_LABEL = "∛2"

PI_LABEL = "π"

E_LABEL = "e"

NUMBER_TREE = {

    "Rational": [

        "-2",
        "-1",
        "0",
        "1",
        "2",
        "1/2",
        "2/3",
        "7/5"

    ],

    "Algebraic Irrational": [

        "√2",
        "√3",
        "√5",
        "∛2",
        "(1+√5)/2"

    ],

    "Transcendental": [

        "π",
        "e",
        "Liouville",
        "Champernowne"

    ]

}

SAVE_ANIMATION = False

OUTPUT_MP4 = "Field_Extension_Space.mp4"

OUTPUT_GIF = "Field_Extension_Space.gif"

DPI = 180

FOOTER = (
    "Field Extension Visualization\n"
    "Ivan Lee"
)


INFO_TEMPLATE = """
FIELD EXTENSION SPACE

Time
----------------------------------------
t = {time:.2f}

Base Field
----------------------------------------
ℚ

Real Field
----------------------------------------
ℝ = ℚ ∪ Irrational

Irrational Numbers
----------------------------------------
Algebraic:
 √2
 √3
 ∛2

Transcendental:
 π
 e

Current State

Finite Algebraic Dimension

Rigid Constraint

Infinite Transcendental Expansion

Free Fluid Evolution

Frame

{frame}/{total}
"""


BANNER = r"""
============================================================
        FIELD EXTENSION SPACE MAPPING
============================================================

             ℚ
             │
             ▼
             ℝ
      ┌──────┴──────────┐
      │                 │
 Rational        Irrational
                      │
          ┌───────────┴────────────┐
          │                        │
     Algebraic              Transcendental
          │                        │
     √2 √3 ∛2 ...             π  e ...

============================================================
Physics-inspired Conceptual Mapping
============================================================
"""