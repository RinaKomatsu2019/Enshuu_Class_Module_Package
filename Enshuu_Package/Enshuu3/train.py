import numpy as np
from chainer import optimizers
from Enshuu3.model import Model

def train_myModel():
        x=np.array([[0,0],[0,1],[1,0],[1,1]],np.float32)
        t=np.array([[0],[1],[1],[0]],np.float32)
        model=Model()
        optimizer=optimizers.Adam()
        optimizer.setup(model)
        for i in range(0,500):
                model.cleargrads()
                loss=model(x,t)
                loss.backward()
                optimizer.update()

                print("Epoch:{} loss:{}".format(i+1,loss.data))
