import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))


import uvicorn
from fastapi import FastAPI
import json

from backend.inputs import EmailMarketingInputs
from src.generate import generate_emails

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.post("/generate")
def generate(inputs: EmailMarketingInputs):
    answer = generate_emails(inputs)
    return answer


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



    
