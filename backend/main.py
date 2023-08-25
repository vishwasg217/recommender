import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))


import uvicorn
from fastapi import FastAPI, Header
import json

from backend.inputs import Inputs
from src.generate import generate_emails

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.post("/generate")
def generate(inputs: Inputs):
    email_inputs = inputs.email_inputs
    OPENAI_API_KEY = inputs.api_key
    answer = generate_emails(email_inputs, OPENAI_API_KEY)
    return answer


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



    
