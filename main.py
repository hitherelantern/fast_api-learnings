from fastapi import FastAPI,HTTPException,Path, Query
import json
from pydantic import BaseModel,Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse

app = FastAPI()


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patients.json','w') as f:
        data = json.dump(data,f,indent=2)
        json



@app.get("/")
def hello():
    return {'message':'patient management system api'}


@app.get("/about")
def about():
    return {'message':"A dummy api to manage patients' records."}


@app.get("/view")
def view():
    data = load_data()
    return data






"""path parameters - dynamic segments of a url path used to identify a specific/particular resource.
 retrieval,update,delete....path parameter usecases !
eg: localhost:8000/view/3....where 3(here) is the path parameter(dynamic)"""

"""Path() in fastapi to increase the readability wrt. path parameter,used to provide metadata,
validation rules and documentation hints for path parameters in your API endpoints"""

x = Path(...,
         description='ID of the patient in the DB.The value is alphanumeric.',
         example = 'P001'
         )

@app.get("/patient/{patient_id}")
def get_patient(patient_id:str = x):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found!")






x = Query(...,description='Sort on the basis of age,height, weight or BMI')
y = Query('asc',description='Sort in ascending or descending order')

@app.get("/sort")
def sort_patients(sort_by:str = x,order:str = y):
    valid_fields = ['height','weight','bmi','age']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field.Select from {valid_fields}")

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid field.Select b/w asc and desc")

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(),key=lambda x:x[sort_by],reverse=sort_order)

    return sorted_data
    
"""searching,filtering,pagination...where query parameters are useful!"""



class Patient(BaseModel):

    id : Annotated[str,Field(...,description='id of the patient',examples=['P001'])]
    name : Annotated[str,Field(...,description='Name of the patient')]
    city : Annotated[str,Field(...,description='City where the patient is living.')]
    age : Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender : Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height : Annotated[float,Field(...,gt=0,lt=2.5,description='height of the patient in meters')]
    weight : Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]
    
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        
        elif self.bmi < 25:
            return "Normal"
        
        elif self.bmi < 30:
            return "Overweight"
        
        else:
            return "Obese"
    



@app.post('/create')
def create_patient(patient:Patient):

    # load existing data
    data = load_data()

    # Check if the patient is already in the db.
    if patient.id in data:
        raise HTTPException(status_code= 400, detail=f"patient with the id {patient.id} is already there in the database!")
    
    # Else, Add new patient to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save the updated data in the database
    save_data(data)

    # Note: 201 status code for successful creation of the resource.
    return JSONResponse(status_code=201,content = {'message':'patient created successfully!'})



class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]



@app.put('/edit/{patient_id}')
def update_patient(patient_update:PatientUpdate,patient_id:str):

    # load the data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="No patient found with that id !")

    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key] = value

    """existing_patient_info -> pydantic object -> update bmi and verdict -> pydantic object -> dict -> save"""
    existing_patient_info['id'] = patient_id
    patient_info_pydantic = Patient(**existing_patient_info)
    patient_info_dict = patient_info_pydantic.model_dump(exclude=['id'])


    data[patient_id] = patient_info_dict

    save_data(data)

    return JSONResponse(status_code=200,content = {'message':'patient updated successfully !'})



@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="No patient found with that id !")

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=201,content = {'message':'patient deleted successfully!'})














