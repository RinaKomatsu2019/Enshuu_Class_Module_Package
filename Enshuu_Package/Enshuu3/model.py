from chainer import Chain,Variable
import chainer.functions as F
import chainer.links as L

class Model(Chain):
    def __init__(self):
        super(Model,self).__init__(
            ln1=L.Linear(2,3),
            ln2=L.Linear(3,1),
        )

    def __call__(self,input,target):
        x=Variable(input)
        t=Variable(target)
        h=F.sigmoid(self.ln1(x))
        h=self.ln2(h)

        loss=F.mean_squared_error(h,t)
        return loss
