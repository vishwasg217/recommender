import sys
from pathlib import Path

# Get the current script's directory
script_dir = Path(__file__).resolve().parent

# Get the project's root directory by going up one level
project_root = script_dir.parent

# Add the project's root directory to sys.path
sys.path.append(str(project_root))



import uvicorn
from fastapi import FastAPI

from backend.inputs import EmailMarketingInputs, format_json_to_multiline_string
from src.generate import generate_emails

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.post("/generate")
def generate(inputs: EmailMarketingInputs):
    print("hello")
    formatted_inputs = format_json_to_multiline_string(inputs)
    answer = generate_emails(formatted_inputs)
    return answer


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
