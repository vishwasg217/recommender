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
    tone_and_voice_from_website: Optional[str] = None
    communication_tone: Optional[str] = None
    brand_voice: Optional[str] = None

class StorylineProgression(BaseModel):
    email_sequence_narrative: str

class PainPointsSolutions(BaseModel):
    pain_points_addressed: Optional[str] = None
    solutions_presented: Optional[str] = None

class EmailMarketingInputs(BaseModel):
    business_information: BusinessInformation
    content_guidelines: ContentGuidelines
    email_structure: EmailStructure
    product_service_information: ProductServiceInformation
    tone_and_voice: ToneAndVoice
    storyline_progression: StorylineProgression
    pain_points_and_solutions: PainPointsSolutions

class Inputs(BaseModel):
    email_inputs : EmailMarketingInputs
    api_key : str


# Assuming 'json_data' contains the received JSON object
# formatted_string = format_json_to_multiline_string(test_input)
# print(formatted_string)

