import my_functions
import json


class Person():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = int(age)

        self.estimate_max_hr = my_functions.estimate_max_hr(age, sex) #die Funktion aufrufen, und self werden übergeben

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