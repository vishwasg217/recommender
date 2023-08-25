import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

def scrape_website_text(website_url):
        try:
            response = requests.get(website_url)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract text content from paragraphs and headers
                text_content = ""
                for paragraph in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    text_content += paragraph.get_text() + " "
                
                return text_content
            else:
                print("Failed to fetch website content")
                return ""
        except Exception as e:
            print("An error occurred:", e)
            return ""

def get_brand_tone_and_voice(website_url, OPENAI_API_KEY):

    website_text = scrape_website_text(website_url)

    template = """
    I am building an email marketing campaign generation system. 
    Hence I have scraped data from the company's website:

    {company_info}

    You are tasked to produce a list of exactly 5 words that capture the company's brand tone and voice. 

    Please provide only a list of comma separated  emotions.
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["company_info"]
    )

    formatted_prompt = prompt.format(company_info=website_text)

    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    response = llm(formatted_prompt)

    return response

def format_json_to_multiline_string(data):
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

def gather_user_inputs():
    print("1. Business Information:")
    business_name = input("   - Business Name: ")
    business_type = input("   - Business Type/Niche: ")
    campaign_goal = input("   - Campaign Goal: ")
    audience_demographics = input("   - Audience Demographics: ")

    print("\n2. Content Guidelines:")
    content_type = input("   - Content Type: ")
    key_message = input("   - Key Message: ")

    print("\n3. Email Structure:")
    call_to_action = input("   - Call to Action (CTA): ")

    print("\n4. Product/Service Information (If Applicable):")
    product_details = input("   - Product/Service Details: ")
    features_benefits = input("   - Features and Benefits: ")

    print("\n5. Tone and Voice:")
    communication_tone = input("   - Communication Tone: ")
    brand_voice = input("   - Brand Voice: ")

    print("\n6. Storyline Progression:")
    email_sequence_narrative = input("   - Email Sequence Narrative: ")

    print("\n7. Pain Points and Solutions:")
    pain_points = input("   - Pain Points Addressed (comma-separated list): ").split(",")
    solutions_presented = input("   - Solutions Presented (comma-separated list): ").split(",")

    inputs = {
        "business_name": business_name,
        "business_type": business_type,
        "campaign_goal": campaign_goal,
        "audience_demographics": audience_demographics,
        "content_type": content_type,
        "key_message": key_message,
        "call_to_action": call_to_action,
        "product_details": product_details,
        "features_benefits": features_benefits,
        "communication_tone": communication_tone,
        "brand_voice": brand_voice,
        "email_sequence_narrative": email_sequence_narrative,
        "pain_points": pain_points,
        "solutions_presented": solutions_presented,
    }
    return inputs


