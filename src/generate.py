import sys
from pathlib import Path

# Get the current script's directory
script_dir = Path(__file__).resolve().parent

# Get the project's root directory by going up one level
project_root = script_dir.parent

# Add the project's root directory to sys.path
sys.path.append(str(project_root))


import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage

from dotenv import dotenv_values

from prompts.prompt import get_prompt
from src.output import Campaign

config = dotenv_values(".env")

OPENAI_API_KEY = config["OPENAI_API_KEY"]

def generate_emails(inputs: str):
    with open("prompts/p2.prompt", "r") as f:
        template = f.read()

    parser = PydanticOutputParser(pydantic_object=Campaign)

    prompt = PromptTemplate(
        template=template,
        input_variables=["inputs"],
        partial_variables={"output_format": parser.get_format_instructions()}
    )

    print(prompt)

    llm = OpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=3000)
    chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=3000)

    formatted_input = prompt.format(inputs=inputs)
    print(formatted_input)

    response = llm(formatted_input)
    return response

test_input = {
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

answer = generate_emails(test_input)
print(answer)
