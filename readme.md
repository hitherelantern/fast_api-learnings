# FastAPI Practice: Building an API for a Dummy ML Model

This project demonstrates the creation of a RESTful API using FastAPI to serve a dummy machine learning (ML) model. The project is designed as a learning exercise to understand API development and deployment for ML models.

---

## Features

* **Endpoints for CRUD Operations**:

  * `GET`: Retrieve data.
  * `POST`: Add new data or make predictions.
  * `PUT`: Update existing data.
  * `DELETE`: Remove data entries.

* **Integration with a Dummy ML Model**:

  * The dummy ML model is a placeholder that mimics prediction functionality.

* **Pydantic for Data Validation**:

  * Ensures structured input data with proper validation.

* **FastAPI for Rapid API Development**:

  * Leverages FastAPI for a clean and efficient API structure.

---

## Project Structure

```bash
.
├── .gitignore # Files to ignore in Git version control

├── ML_api/app.py # FastAPI backend implementation
├── ML_api/fastapi_ml_model.ipynb # Jupyter notebook for model experimentation
├── ML_api/frontend.py # Streamlit frontend for user interaction
├── ML_api/insurance.csv # Dataset for training/validation
├── ML_api/model.pkl # Serialized ML model

├── PatientManagement/main.py # Additional script (Patient management system dummy APIs using pydantic and fastapi)
├── PatientManagement/patients.json # Sample patient data in JSON format

├── pydantic_tutorial/ # Directory for Pydantic examples/tutorials

└── readme.md # Project documentation (this file)
```

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hitherelantern/fast_api-learnings.git
   cd fast_api-learnings
   ```


2. **Run the application**:

   ```bash
   uvicorn app:app --reload
   ```

4. **Access the API**:
   Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---


## Future Enhancements

* Replace the dummy ML model with a trained ML model.
* Add authentication and authorization mechanisms.
* Integrate with a database for persistent storage.
* Implement additional endpoints for data analytics.

---

