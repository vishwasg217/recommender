import streamlit as st
from langchain.llms import OpenAI

from dotenv import dotenv_values

config = dotenv_values(".env")

OPENAI_API_KEY = config["OPENAI_API_KEY"]

prompt = """
you are tasked to write an email marketing campaign which has a sequence of 5 emails.

Below are the input parameters you need to consider:
----
{inputs}
---

Below is the email marketing campaign output format. Write the subject for each email as well:
---
{outputs}
---

Generate the email sequence using the input parameters above and the output format given. Use placeholders wherever necessary.

"""

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3, max_tokens=2000)

answer = llm(prompt)
print(answer)