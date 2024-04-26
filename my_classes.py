import json
import my_functions
from datetime import datetime


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.__dict__, fp)

def calculate_age(age):
    birth_date = datetime.strptime(age, "%Y-%m-%d")
    
    current_date = datetime.now()
    
    age = int(current_date.year - birth_date.year)
    
    if current_date.month < birth_date.month:
        age = int(age - 1)
    
    elif current_date.month == birth_date.month and current_date.day < birth_date.day:
        age = int(age - 1)
    else:
        pass
    return age
class Subject(Person):
    
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__age= calculate_age(age)
        
        self.estimate_max_hr = my_functions.estimate_max_hr(calculate_age(age), sex) #die Funktion aufrufen, und self werden übergeben
    
    
    def save(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.__dict__, fp)

class Supervisor(Person):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
         
    def save(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.__dict__, fp)


class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
    
    def save(self, file_name):
        with open(file_name, 'w') as fp:
            json.dump(self.__dict__, fp)