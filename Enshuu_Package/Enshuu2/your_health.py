class Evaluate_Your_Health():
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def calc_BMI(self):
        return self.weight/(self.height*self.height)
    def print_evaluate(self):
        BMI=self.calc_BMI()
        if BMI<18.5:
            print("{}: Your are too smart!".format(self.name))
        elif BMI>=25.0:
            print("{}: Your are too fat!".format(self.name))
        else:
            print("{}: Your are standard".format(self.name))