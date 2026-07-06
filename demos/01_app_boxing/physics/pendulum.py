import numpy as np

class Bag:

    def __init__(self):

        self.theta=0

        self.omega=0

    def position(self,length):

        x=length*np.sin(self.theta)

        z=-length*np.cos(self.theta)

        return x,z