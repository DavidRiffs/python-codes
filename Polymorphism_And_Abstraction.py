class student:
    def __init__(self,name,score):
        self.name = name 
        self.score = score
    def display_info(self):
        print(self.name,self.score)
    from abc import ABC, abstractmethod
    class student(ABC):
        def calculate_result(self):
            pass
class graduate(student):
    def __init__(self, name, score):
        super().__init__(name, score)
    def calculate_result(self):
        if self.score >= 60:
            print(f"{self.name}: PASS")
            return
        print(f"{self.name}: FAIL")
    def display_info(self):
        return super().display_info()
class undergraduate(student):
    def calculate_result(self):
        if self.score >= 50:
            print(f"{self.name}: PASS")
            return
        print(f"{self.name}: FAIL")
    def display_info(self):
        return super().display_info()

student1 = graduate("Alice",90)
#student1.calculate_result()
student2 = undergraduate("Diana",45)
#student2.calculate_result()

students = [student1,student2]
for student in students:
    student1.calculate_result()
    student2.display_info()