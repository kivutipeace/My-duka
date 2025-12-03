class BankAccount:
    # Constructor - initializes objects
    def __init__(self,account_number,balance,owner_name,date_opened,):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        
        # self - refrences the object
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:  
            return "Insufficient funds"
        
    def deposit(self,amount):
        self.balance+= amount
        

    def display_info(self):
        return f"==== Welcome {self.owner_name} account number {self.account_number}, balance is {self.balance}, account created at {self.date_opened} ==="
    
        
# Object creation and method calling
userinput = input('Enter owner name')
Account1 = BankAccount(1234,100000.00,"Peace","12-10-2004")
Account2 = BankAccount(2345,200000.00,"Letting","13-10-2003")
Account1.deposit(1000)
Account1.withdraw(500)
Account2.deposit(1000)
Account2.withdraw(500)
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
        
        # self - references the object
    def start(self):
        if self.fuel_level >= 100 and self.is_running == True:
            return 'You can start it'
        else:
            return 'Your car cant start' 
    
    def stop(self):
        if self.is_running == False:
            return 'The is stopped'
        else: 
            return 'The car not stopped'

    def refuel(self, fuel_capacity, fuel_level, refuel_amount):
        if fuel_level >= fuel_capacity:
          return "The car is already full"
    
        new_level = fuel_level + refuel_amount

        if new_level > fuel_capacity:
            new_level = fuel_capacity

        self.fuel_level = new_level
        return f"Refueled. New fuel level is : {self.fuel_level}"

    def drive(self,fuel_level):
        if self.is_running == True and self.fuel_level == 10 <= fuel_level <=100 :
            print('You are driving the car')
        else: 
            print('You are not driving the car')
               
    def display_info(self):
            return f"=== Your car {self.brand}, {self.model}, year {self.year}, fuel capacity {self.fuel_capacity}, current fuel level {self.fuel_level} is runnning {self.is_running} ==="   
            
# Creating the objects and calling the method
car1 = Car ('Subaru','Forester',2016,100,80,True)
car1.refuel(100,70,80)
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
        super().display_info()
        print(f"=== Student id: {self.student_id} and student course: {self.course} ===")
class Teacher(Person): # Child class
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
        
    def display_info(self):
        super.display_info()
        print(f"=== Teachers subject {self.subject} \n and teachers salary {self.salary} ===")
    
# Object construction 
student = Student("Peace",15,90,"Computer Science")
teacher = Teacher("Letting",25,"Computer Science",200000)
# Printing the persons info
student.display_info()
teacher.dispaly_info()