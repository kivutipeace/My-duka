class BankAccount:
    # Constructor - initializes objects
    def __init__(self,account_number,balance,owner_name,date_opened,):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        
        # self - refrences the object
        # Behaviour - withdraw money
    def withdraw(self,amount):
        # Checking if the amount to be withdrawed is accurate with the balance
        if amount <= self.balance:
            self.balance -= amount
        else: # else your withdraw request isn't valid coz you dont have the required amount 
            return "Insufficient funds"
        
        # Behaviour - deposit money
    def deposit(self,amount):
        # From the balance and the amount to be deposited
        self.balance+= amount
        
        # Display banks info
    def display_info(self):
        return f"==== Welcome {self.owner_name} account number {self.account_number}, balance is {self.balance}, account created at {self.date_opened} ==="
    
        
# Object creation and method calling
# Creating the first bank account - object
userinput = input('Enter owner name')
Account1 = BankAccount(1234,100000.00,"Peace","12-10-2004")
# Creating the second bank account - object
Account2 = BankAccount(2345,200000.00,"Letting","13-10-2003")
# Bank acc 1 method calling
Account1.deposit(1000)
Account1.withdraw(500)
# Bank acc 2 method calling
Account2.deposit(1000)
Account2.withdraw(500)
# Printing the banks info
print(Account1.display_info())
print(Account2.display_info())


# OOP tasks 2
class Car: # Class
    # Method - constructor
    def __init__(self,brand,model,year,fuel_capacity,fuel_level,is_running):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running
        
        # Behaviour
        # self - references the object
        # Behaviour to start the car
    def start(self):
        # Check if the car has a brand and a model - is it a car?
        if self.brand == self.brand and self.model == self.model:
            return 'You have a car you can start it'
        else: # else its not a car and it can't start
            return 'You do not have a car, you cant start it' 
    
    # Behaviour to stop the car if running
    def stop(self):
        # Check if the car is running in order to stop the car
        if self.is_running == True:
            return 'The car is running press the stop button'
        else: # else the car is already stopped
            return 'The car is already on stop'
            
            
    # Behaviour to refuel the car
    def refuel(self, fuel_capacity, fuel_level, refuel_amount):
    # Can't refuel if already full
     if fuel_level >= fuel_capacity:
        return "The car is already full"
    
    # add the refueled amout 
     new_level = fuel_level + refuel_amount

    # Cap it at fuel_capacity
     if new_level > fuel_capacity:
        new_level = fuel_capacity

    # Update fuel level and return the new fuel level
     self.fuel_level = new_level
     return f"Refueled. New fuel level is : {self.fuel_level}"

    # Behaviour to drive the car
    def drive(self,fuel_level):
        # Checking if the car is running and the fuel level is enough
        if self.is_running == True and self.fuel_level == 10 <= fuel_level <=100 :
            print('You are driving the car')
        else: # else the car is not in drive
            print('You are not driving the car')
               
        # display the car info
    def display_info(self):
            return f"=== Your car {self.brand}, {self.model}, year {self.year}, fuel capacity {self.fuel_capacity}, current fuel level {self.fuel_level} is runnning {self.is_running} ==="   
            
# Creating the objects and calling the method
car1 = Car ('Subaru','Forester',2016,100,80,True)
car1.refuel(100,70,80)
# Printing the cars info
print(car1.display_info())


# Inheritance
class Person: # Parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        return f"Welcome {self.name}, age {self.age}"
    
class Student(Person): # Child class
    def __init__(self,name,age,student_id,course):
        super().__init__(name,age)
        self.student_id = student_id
        self.course = course
        
    def display_info(self):
        return f"=== Student id: {self.student_id} and student course: {self.course} ==="
class Teacher(Person): # Child class
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
        
    def display_info(self):
        return f"=== Teachers subject {self.subject} and teachers salary {self.salary} ==="
    
# Object construction 
student = Student("Peace",15,90,"Computer Science")
teacher = Teacher("Letting",25,"Computer Science",200000)
# Printing the persons info
print(student.display_info())
print(teacher.display_info())




userInput = input("Enter your name: ")
if userInput == "Ken":
    print('Failure')
elif userInput == "Faridah":
    print('Failure')
elif userInput == "Peace":
    print(Account1.display_info())
else:
    print('NaN')