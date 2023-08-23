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
    formatted_inputs = format_json_to_multiline_string(inputs)
    answer = generate_emails(formatted_inputs)
    return answer

# test_input = {
#     "business_information": {
#         "business_name": "FitLife Wellness",
#         "business_type": "Health and Fitness",
#         "campaign_goal": "Re-engage Inactive Subscribers",
#         "audience_demographics": "Health-conscious individuals, age 25-50, interested in fitness"
#     },
#     "content_guidelines": {
#         "content_type": "Re-engagement",
#         "key_message": "Your Health Journey Continues with FitLife Wellness"
#     },
#     "email_structure": {
#         "call_to_action": "Get Back on Track"
#     },
#     "product_service_information": {
#         "product_service_details": None,
#         "features_and_benefits": None
#     },
#     "tone_and_voice": {
#         "communication_tone": "Supportive and Encouraging",
#         "brand_voice": "Inspirational and Motivating"
#     },
#     "storyline_progression": {
#         "email_sequence_narrative": "Remind subscribers of the benefits of a healthy lifestyle, showcase success stories, and offer personalized incentives to reignite their commitment."
#     },
#     "pain_points_and_solutions": {
#         "pain_points_addressed": ["Lack of motivation", "Busy schedule"],
#         "solutions_presented": ["Inspiring success stories", "Personalized wellness plan"]
#     }
# }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
