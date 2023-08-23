import sys
print(sys.path)

from prompts.prompt import get_prompt


prompt = get_prompt()

print
print(prompt)