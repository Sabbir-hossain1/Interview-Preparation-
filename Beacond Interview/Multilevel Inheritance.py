class GrandFather:
    def __init__(self,gfName):
        self.grandFather = gfName

class Father(GrandFather):
    def __init__(self,fName,gfName):
        self.fatherName = fName
        GrandFather.__init__(self,gfName)

class Children(Father):
    def __init__(self,child,fname,gfname):
        self.children = child
        Father.__init__(self,fname,gfname)
        
    def ChildDetails(self):
        print("Child Name: ",self.children)
        print("Father Name: ",self.fatherName)
        print("Grand Father  Name: ",self.grandFather)
child1 = Children("Sabbir Hossain","Momin Mia","Jabbar Ali Bepari")
child1.ChildDetails()