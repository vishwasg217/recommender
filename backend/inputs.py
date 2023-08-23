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


default_input = {
    "business_information": {
        "business_name": "Trendy Junction",
        "business_type": "Fashion and Accessories",
        "campaign_goal": "Drive Sales during Summer Clearance Sale",
        "audience_demographics": "Fashion enthusiasts, age 18-35, worldwide"
    },
    "content_guidelines": {
        "content_type": "Sale Promotion",
        "key_message": "Shop the Hottest Summer Styles at Unbeatable Prices"
    },
    "email_structure": {
        "call_to_action": "Shop Now"
    },
    "product_service_information": {
        "product_service_details": "Summer clothing and accessories collection",
        "features_and_benefits": "Wide variety, discounted prices, free shipping for orders over $50"
    },
    "tone_and_voice": {
        "communication_tone": "Exciting and Trendy",
        "brand_voice": "Chic and Modern"
    },
    "storyline_progression": {
        "email_sequence_narrative": "Create anticipation for the Summer Clearance Sale, showcasing the latest fashion trends and emphasizing the limited-time nature of the event."
    },
    "pain_points_and_solutions": {
        "pain_points_addressed": "Limited-time offers, expensive summer fashion, missing out on latest trends",
        "solutions_presented": "Highlight exclusive discounts, emphasize unbeatable prices, showcase new arrivals"
    }
}

def format_json_to_multiline_string(data):
    print("data", data)
    result = []
    
    def recursive_format(data, indent_level=0):
        if isinstance(data, dict):
            for key, value in data.items():
                result.append("    " * indent_level + f"{key}:")
                recursive_format(value, indent_level + 1)
        elif isinstance(data, list):
            for item in data:
                result.append("    " * indent_level + f"- {item}")
        else:
            result.append("    " * indent_level + f"{data}")
    
    recursive_format(data)
    return "\n".join(result)

# Assuming 'json_data' contains the received JSON object
# formatted_string = format_json_to_multiline_string(test_input)
# print(formatted_string)

