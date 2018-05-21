class Parent():
    def __init__(self, first_name, last_name, eye_color):
        print("Parent Constructor called")
        self.first_name = first_name
        self.last_name = last_name
        self.eye_color = eye_color
    
class Child(Parent):
    def __init__(self, first_name, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, first_name, last_name, eye_color)
        self.first_name = first_name
        self.number_of_toys = number_of_toys


cyrus = Parent("Billy", "Cyrus", "blue")
print(cyrus.last_name)

miley_cyrus = Child("Miley", "Cyrus", "blue", 5)
print(miley_cyrus.first_name)
print(miley_cyrus.number_of_toys)