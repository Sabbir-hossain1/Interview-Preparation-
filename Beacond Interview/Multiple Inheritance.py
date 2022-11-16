class Father:
    father_name = ''
    
class Mother:
    mother_name = ''

class Child(Father,Mother):
    def parents(self):
        print("Father name is : ",self.father_name)
        print("Mother name is : ",self.mother_name)

child1 = Child()
child1.father_name = "Sabbir"
child1.mother_name = "Janina"
child1.parents()