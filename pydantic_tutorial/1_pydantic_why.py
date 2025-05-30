from pydantic import BaseModel

# pydantic model/class
class Patient(BaseModel):
    """define the schema,type validation"""
    name : str
    age : int


patient_info = {'name':'Krish','age':23}

# Making an object of the patient class.
patient1 = Patient(**patient_info)

def insert_data(patient:Patient):
    # Attributes of the object
    print(f"Name of the patient is {patient.name} and his/her age is {patient.age}")


insert_data(patient1)
