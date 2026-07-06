import numpy as np

class Boxer:

    def __init__(self):

        self.shoulder=np.array([-1,0,1.4])

        self.elbow=np.array([-0.6,0,1.2])

        self.hand=np.array([-0.2,0,1.0])

    def update(self,t):

        punch=np.sin(2*np.pi*t)

        self.hand[0]=-0.2+0.5*np.maximum(0,punch)