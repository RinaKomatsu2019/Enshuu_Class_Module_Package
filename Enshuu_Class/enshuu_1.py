class People():
    visitor=0
    def __init__(self):
        People.visitor+=1
        self.name=''

    def echo_name(self):
        print("Hello I'm {}!".format(self.name))
        print("\t the number of visitors :{}".format(People.visitor))

student1=People()
student1.name='Taro'
student1.echo_name()

student2=People()
student2.name='Jiro'
student2.echo_name()
