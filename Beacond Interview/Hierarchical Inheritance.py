class Parent:
    def parentFunc(self):
        print("This is form Parent Class")

class Child1(Parent):
    def child1Func(self):
        print("This is form child1 class")

class Child2(Parent):
    def child3func(self):
        print("This is from Child 3 function")
object1 = Child2()
object1.parentFunc()
