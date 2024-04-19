import my_functions
import json
import my_classes

if __name__ == "__main__":
    
    'Input the information of the subject'
    
    x=input("Enter your Firstname: ")
    y=input("Enter your Lastname: ")
    z=input("Enter your sex: ")
    a=int(input("Enter your age: "))
    
    
    'Build a dictionary of information about a supervisor and a subject'
    supervisor = my_classes.Person("John","Doe","male",50)
    subject = my_classes.Person(x,y,z,int(a))
    
    'Build a dictionary of information about an experiment'
    experiment = my_classes.Experiment("Experiment 1","2021-06-01",supervisor.__dict__,subject.__dict__)
    my_classes.Person.save(subject,"subject.json")
    my_classes.Person.save(supervisor,"supervisor.json")
    my_classes.Experiment.save(experiment,"experiment.json")
