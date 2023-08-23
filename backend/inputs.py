from typing import List, Optional
from pydantic import BaseModel

class BusinessInformation(BaseModel):
    business_name: str
    business_type: str
    campaign_goal: str
    audience_demographics: Optional[str] = None

class ContentGuidelines(BaseModel):
    content_type: str
    key_message: str

class EmailStructure(BaseModel):
    call_to_action: str

class ProductServiceInformation(BaseModel):
    product_service_details: Optional[str] = None
    features_and_benefits: Optional[str] = None

class ToneAndVoice(BaseModel):
    communication_tone: Optional[str] = None
    brand_voice: Optional[str] = None

class StorylineProgression(BaseModel):
    email_sequence_narrative: str

class PainPointsSolutions(BaseModel):
    pain_points_addressed: List[str]
    solutions_presented: List[str]

class EmailMarketingInputs(BaseModel):
    business_information: BusinessInformation
    content_guidelines: ContentGuidelines
    email_structure: EmailStructure
    product_service_information: ProductServiceInformation
    tone_and_voice: ToneAndVoice
    storyline_progression: StorylineProgression
    pain_points_and_solutions: PainPointsSolutions


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