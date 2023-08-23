import uvicorn
from fastapi import FastAPI

from inputs import EmailMarketingInputs

app = FastAPI()

# @app.post("/email-marketing")
def generate(inputs: EmailMarketingInputs):
    print(inputs)

test_input = {
    "business_information": {
        "business_name": "FitLife Wellness",
        "business_type": "Health and Fitness",
        "campaign_goal": "Re-engage Inactive Subscribers",
        "audience_demographics": "Health-conscious individuals, age 25-50, interested in fitness"
    },
    "content_guidelines": {
        "content_type": "Re-engagement",
        "key_message": "Your Health Journey Continues with FitLife Wellness"
    },
    "email_structure": {
        "call_to_action": "Get Back on Track"
    },
    "product_service_information": {
        "product_service_details": None,
        "features_and_benefits": None
    },
    "tone_and_voice": {
        "communication_tone": "Supportive and Encouraging",
        "brand_voice": "Inspirational and Motivating"
    },
    "storyline_progression": {
        "email_sequence_narrative": "Remind subscribers of the benefits of a healthy lifestyle, showcase success stories, and offer personalized incentives to reignite their commitment."
    },
    "pain_points_and_solutions": {
        "pain_points_addressed": ["Lack of motivation", "Busy schedule"],
        "solutions_presented": ["Inspiring success stories", "Personalized wellness plan"]
    }
}


if __name__ == "__main__":
    generate(test_input)
    
