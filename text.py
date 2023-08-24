import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

config = dotenv_values(".env")
OPENAI_API_KEY = config["OPENAI_API_KEY"]

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

# Example usage
website_url = "https://www.activeloop.ai/"
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

print(website_text)
print(response)
parser = CommaSeparatedListOutputParser()
tone_of_voice = parser.parse(response)
print(tone_of_voice)
print(type(tone_of_voice))



