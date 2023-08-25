from pydantic import BaseModel, Field

class Email(BaseModel):
    subject: str = Field(description="The subject line of the email.")
    greeting: str = Field(description="Use placeholder for name.")
    body: str = Field(description="The body of the email. Atleast 2 paragraphs. Use placeholders if needed.")
    signature: str = Field(description="The signature of the email.")

class Campaign(BaseModel):
    email_1: Email = Field(description="Email 1: Introduction and Pain Point")
    email_2: Email = Field(description="Email 2: Building on Pain Point")
    email_3: Email = Field(description="Email 3: Solution Presentation")
    email_4: Email = Field(description="Email 4: Benefits and Social Proof")
    email_5: Email = Field(description="Email 5: Call to Action and Conclusion")