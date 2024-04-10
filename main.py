import my_functions
import pickle

if __name__ == "__main__":
    x=input("Enter your Firstname: ")
    y=input("Enter your Lastname: ")
    z=input("Enter your sex: ")
    a=input("Enter your age: ")
    supervisor = my_functions.build_person("Samuel","Dabisch","male",19)
    subject = my_functions.build_person(x,y,z,int(a))
    with open('subject_data.pkl', 'wb') as fp:
        pickle.dump([supervisor,subject], fp)