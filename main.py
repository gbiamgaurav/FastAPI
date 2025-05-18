
from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "Fully functional API to manage patients and their data."}

@app.get("/view")
def view():
    data = load_data()
    return data

# Path Parameters
@app.get("/search/{patient_id}") # Path Parameter
def search(patient_id: str = Path(..., title="Patient ID", description="The unique identifier of the patient.", example="PID001")):
    data = load_data()
    for patient in data:
        if patient["id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found.")

# Query Parameters
@app.get("/sort")
def sort_patients(sort_by: str = Query(...,description="sort the patients on height, weight or bmi"), order: str = Query('asc',description="order the patients ascending or descending")):
    valid_fields = ["height","weight","bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid fields selected from {valid_fields}") # Changed to 400
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f"Invalid order selected from asc/desc") # Changed to 400
    
    data = load_data() # Assumed to be a list of dictionaries

    sort_order = True if order == "desc" else False

    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sort_order) # Corrected line

    return sorted_data