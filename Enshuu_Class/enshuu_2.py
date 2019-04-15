class Person():
    def __init__(self):
        self.name=''
        self.age=None

    def judge_adult(self):
        if (self.age>=20):
            print("{} became an adult!".format(self.name))
        else:
            print("{} is not an adult".format(self.name))


person1=Person()
person1.name="Yuki"
person1.age=25
person1.judge_adult()

person2=Person()
person2.name="Masa"
person2.age=18
person2.judge_adult()

person3=Person()
person3.name="Nana"
person3.age=20
person3.judge_adult()

