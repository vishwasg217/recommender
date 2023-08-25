from src.output import Campaign
from src.utils import format_json_to_multiline_string
from backend.inputs import EmailMarketingInputs

from langchain.output_parsers import PydanticOutputParser

import json

parser = PydanticOutputParser(pydantic_object=Campaign)

op = parser.get_format_instructions()
print(op)






