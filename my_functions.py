from datetime import datetime

def estimate_max_hr(calculate_age : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * calculate_age
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  calculate_age
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : estimate_max_hr(age,sex)}
    return dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return dict


def calculate_age(age):
    # Parse the birthdate string into a datetime object
    from main import sub_age
    birth_date = sub_age
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference in years
    age = current_date.year - birth_date.year
    
    # Adjust age if the birthday hasn't occurred yet this year
    if current_date.month < birth_date.month or \
       (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    
    return int(age)