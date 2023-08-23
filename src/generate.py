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

from dotenv import dotenv_values

from prompts.prompt import get_prompt

config = dotenv_values(".env")

OPENAI_API_KEY = config["OPENAI_API_KEY"]

def generate_emails(inputs: str):
    with open("prompts/total.prompt", "r") as f:
        template = f.read()

    prompt = PromptTemplate.from_template(template)

    print(prompt)

    llm = OpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=2000)
    chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, max_tokens=2000)

    formatted_input = prompt.format(inputs=test_input)
    print(formatted_input)

    answer = llm(formatted_input)
    return answer

test_input = """business_information:
    business_name: FitLife Wellness
    business_type: Health and Fitness
    campaign_goal: Re-engage Inactive Subscribers
    audience_demographics: Health-conscious individuals, age 25-50, interested in fitness
content_guidelines:
    content_type: Re-engagement
    key_message: Your Health Journey Continues with FitLife Wellness
email_structure:
    call_to_action: Get Back on Track
product_service_information:
    product_service_details: null
    features_and_benefits: null
tone_and_voice:
    communication_tone: Supportive and Encouraging
    brand_voice: Inspirational and Motivating
storyline_progression:
    email_sequence_narrative: Remind subscribers of the benefits of a healthy lifestyle, showcase success stories, and offer personalized incentives to reignite their commitment.
pain_points_and_solutions:
    pain_points_addressed: [Lack of motivation, Busy schedule]
    solutions_presented: [Inspiring success stories, Personalized wellness plan]
"""
