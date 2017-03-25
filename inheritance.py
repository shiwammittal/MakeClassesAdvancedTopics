class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor in execution")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name " + self.last_name)
        print("Eye color " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor in execution")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

name = Parent("mittal","black")
name.show_info()
#print(name.last_name)
#name = Child("mittal", "black", 5)
#print(name.last_name)
#print(name.number_of_toys)
