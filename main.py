import my_functions
import pickle

if __name__ == "__main__":
    
    'Input the information of the subject'
    
    x=input("Enter your Firstname: ")
    y=input("Enter your Lastname: ")
    z=input("Enter your sex: ")
    a=input("Enter your age: ")
    
    
    'Build a dictionary of information about a supervisor and a subject'
    supervisor = my_functions.build_person("Samuel","Dabisch","male",19)
    subject = my_functions.build_person(x,y,z,int(a))
    
    'Build a dictionary of information about an experiment'
    experiment = my_functions.build_experiment("Experiment 1","2021-06-01",supervisor,subject)
    
    'Save dict as a Pickle file'
    with open('expiremnt_data.pkl', 'wb') as fp:
        pickle.dump([experiment], fp)