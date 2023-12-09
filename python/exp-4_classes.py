class Employee():

    emp_list = {}
    manager = {}

    def __init__(self, fname, lname, eid, type):
        self.emp_list[eid] = self
    def info(self, obj):
        return (obj.fname, obj.lname, obj.eid, obj.type)

class Manager(Employee):
    def __init__(self, fname, lname, eid):
        Employee.__init__(self, fname, lname, eid, 'Manager')
        super().manager[eid] = self
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.type = 'Manager'
    test = {}
    dev = {}
    man_emp = {}

    def add(self, obj):
        super().emp_list[obj.eid] = obj
        if (obj.type == 'Developer'):
            self.dev[obj.eid] = obj
        else:
            self.test[obj.eid] = obj
            self.man_emp[obj.eid] = obj

    def remove(self, eid, type):
        del super().emp_list[eid]
        if (type == 'Developer'):
            del self.dev[eid]
        else:
            del self.test[eid]
            del self.man_emp[eid]

    def display(self):
        for i in self.man_emp:
            print(i, ":", str(super().info(self.man_emp[i])))

    def manager_list(self):
        return super().manager

class Developer(Employee):
    def __init__(self, fname, lname, eid):
        Employee.__init__(self, fname, lname, eid, 'Developer')
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.type = 'Developer'

class Tester(Employee):

    def __init__(self, fname, lname, eid):
        Employee.__init__(self, fname, lname, eid, 'Tester')
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.type = 'Tester'

manager1 = Manager('Vijay', 'Harkare', 1)

print("Data corresponding to the manager:", manager1.manager[manager1.eid].fname, manager1.manager[manager1.eid].lname)

print()

print("List entry structure for employees is:")

print("<ID>: (<First Name>, <Last Name>, <ID>, ,<Type>)")

print()

print('List of employees before adding developer:')

manager1.display()

print()

print("List of employees after adding developer:")

manager1.add(Developer('Anaida', 'Lewis', 2))

manager1.display()

print()

manager1.add(Tester('Vidhi', 'Kansara', 3))

print('List of employees after adding tester:')

manager1.display()

print()

print('List of employees after removing tester:')

manager1.remove(3, 'Tester')

manager1.display()