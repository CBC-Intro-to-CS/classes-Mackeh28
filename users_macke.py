class User :
    def __init__(first_name,  last_name):
     
        self.first_name = first_name
        self.last_name = last_name
        self.age = 14
        self.hight = "5'1"


    def first_name(self) :
        print(f"{self.first_name} is your frist name")

    def last_name(self):
       print(f"{self.last_name} is your last name!")


    def age(self):
        print(f"{self.first_name} you are {self.age} year old .")

    def age(self):
        print(f"{self.first_name} you hight is {self.hight}  .")
describe_user = Dog('Henry', 'Macke')

print("Hello user this is your frist a last name")
print(f"your frist name is {describe_user.frist_name}.")
print(f"your last name is {describe_user.last_name} ")
print(f"You are {describe_user.age} year old")
print(f"You hight is {describe_user.age}")

called describe_user.(describe_user.frist_name)
called describe_user.(describe_user.last_name)
called describe_user.(describe_user.age)
called describe_user.(describe_user.hight)


