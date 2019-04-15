class Student():
    student_list=[]
    def __init__(self,name):
        self.name=name
        print("Registered {} to student_list".format(self.name))

    def calc_student_num(self):
        return len(Student.student_list)

    def output_student_list(self):
        print("student_list consists of {} students".format(self.calc_student_num()))
        for name in Student.student_list:
            print(name)
            print('\\n')

s1=Student(name='Taro')
s2=Student(name='Jiro')
s2.output_student_list()
