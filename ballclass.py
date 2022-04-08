class Ball(object):
    def __init__(self,color,shape,velocity):
        self.color=color
        self.shape=shape
        self.velocity=velocity
    def bounce(self,velocity):
        return self.velocity
ball1=Ball("red","round",100)
#ball1.bounce(100)
        