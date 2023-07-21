# This file is for fastapi to create endpoints
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()
# correct dtypes class to check - inherit from BaseModel, this helps us to check the input/output are string type
class TextIn(BaseModel):
    text:str
class PredictionOut(BaseModel):
    language:str

# helth check
@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

