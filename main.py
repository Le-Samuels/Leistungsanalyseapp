import json
from datetime import datetime
import my_classes 

if __name__ == "__main__":
    
    'Input the information of the subject and supervisor of the experiment'
    
    sub_f_name= input("Enter your Firstname: ")
    sub_l_name= input("Enter your Lastname: ")
    sub_sex= input("Enter your sex: ")
    sub_age= input("Enter your Birthdate(yyyy-mm-dd): ")
    
    sup_f_name= input("Enter your Supervisor's Firstname: ")
    sup_l_name= input("Enter your Supervisor's Lastname: ")

    
    'Build a dictionary of information about a supervisor and a subject'
    subject = my_classes.Subject(sub_f_name, sub_l_name, sub_sex, sub_age)
    supervisor = my_classes.Supervisor(sup_f_name, sup_l_name)
    
    
    'Build a dictionary of information about an experiment'
    experiment = my_classes.Experiment("Experiment 1","2021-06-01",supervisor.__dict__,subject.__dict__)
    my_classes.Person.save(subject,"subject.json")
    my_classes.Person.save(supervisor,"supervisor.json")
    my_classes.Experiment.save(experiment,"experiment.json")
