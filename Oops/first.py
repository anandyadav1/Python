class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def get_AVG(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("Hi", self.name,"your avg  is", sum/3)


s1 = Student("Anand yadav", [88, 94, 90])
s1.get_AVG()