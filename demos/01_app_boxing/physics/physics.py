import numpy as np

def step(theta,
         omega,
         force,
         dt,
         length,
         damping):

    g = 9.81

    alpha = -(g/length)*np.sin(theta)

    alpha -= damping*omega

    alpha += force

    omega += alpha*dt

    theta += omega*dt

    return theta,omega