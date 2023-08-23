

def get_prompt():
    with open('prompts/output_format.prompt', 'r') as f:
        output_format = f.read()

    total = """
    you are tasked to write an email marketing campaign that has a sequence of 5 emails.

    Below are the input parameters you need to consider:
    ----
    {inputs}
    ---

    Below is the email marketing campaign output format. Write the subject for each email as well:
    ---
    """ + output_format + """
    ---

    Generate the email sequence using the input parameters above and the output format given. Use placeholders wherever necessary.

    """
    return total

    