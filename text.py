from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Email(BaseModel):
    subject: str = Field(description="The subject line of the email.")
    greeting: str = Field(description="The greeting of the email.")
    body: str = Field(description="The body of the email.")
    signature: str = Field(description="The signature of the email.")

class Campaign(BaseModel):
    email_1: Email = Field(description="Email 1: Introduction and Pain Point")
    email_2: Email = Field(description="Email 2: Building on Pain Point")
    email_3: Email = Field(description="Email 3: Solution Presentation")
    email_4: Email = Field(description="Email 4: Benefits and Social Proof")
    email_5: Email = Field(description="Email 5: Call to Action and Conclusion")

# Define test input data
test_input = {
    "email_1": {
        "subject": "Subject 1",
        "greeting": "Hello",
        "body": "This is the body of email 1.",
        "signature": "Best regards"
    },
    "email_2": {
        "subject": "Subject 2",
        "greeting": "Hi there",
        "body": "This is the body of email 2.",
        "signature": "Sincerely"
    },
    "email_3": {
        "subject": "Subject 3",
        "greeting": "Dear recipient",
        "body": "This is the body of email 3.",
        "signature": "Yours truly"
    },
    "email_4": {
        "subject": "Subject 4",
        "greeting": "Hey",
        "body": "This is the body of email 4.",
        "signature": "Kind regards"
    },
    "email_5": {
        "subject": "Subject 5",
        "greeting": "Hi friend",
        "body": "This is the body of email 5.",
        "signature": "Warm wishes"
    }
}

# Create a Campaign instance
# campaign_instance = Campaign(**test_input)

# # Access the extracted data for each email
# for idx, email in enumerate([campaign_instance.email_1, campaign_instance.email_2, campaign_instance.email_3, campaign_instance.email_4, campaign_instance.email_5], start=1):
#     print(f"Email {idx} Subject:", email.subject)
#     print(f"Email {idx} Greeting:", email.greeting)
#     print(f"Email {idx} Body:", email.body)
#     print(f"Email {idx} Signature:", email.signature)
#     print("-" * 30)

parser = PydanticOutputParser(pydantic_object=Campaign)
print(parser.get_format_instructions())
