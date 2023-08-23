import streamlit as st
import requests

app_url = "http://fastapi:8000"
endpoint = "/email-marketing"


st.title("FitLife Wellness Campaign Creation")

# Business Information
st.header("Business Information")
business_name = st.text_input("Business Name")
business_type = st.text_input("Business Type")
campaign_goal = st.text_input("Campaign Goal")
audience_demographics = st.text_area("Audience Demographics")

# Content Guidelines
st.header("Content Guidelines")
content_type = st.text_input("Content Type")
key_message = st.text_area("Key Message")

# Email Structure
st.header("Email Structure")
call_to_action = st.text_input("Call to Action")

# Tone and Voice
st.header("Tone and Voice")
communication_tone = st.text_input("Communication Tone")
brand_voice = st.text_input("Brand Voice")

# Storyline Progression
st.header("Storyline Progression")
email_sequence_narrative = st.text_area("Email Sequence Narrative")

# Pain Points and Solutions
st.header("Pain Points and Solutions")
pain_points_addressed = st.text_area("Pain Points Addressed")
solutions_presented = st.text_area("Solutions Presented")

email_inputs = {
        "business_information": {
            "business_name": business_name,
            "business_type": business_type,
            "campaign_goal": campaign_goal,
            "audience_demographics": audience_demographics
        },
        "content_guidelines": {
            "content_type": content_type,
            "key_message": key_message
        },
        "email_structure": {
            "call_to_action": call_to_action
        },
        "tone_and_voice": {
            "communication_tone": communication_tone,
            "brand_voice": brand_voice
        },
        "storyline_progression": {
            "email_sequence_narrative": email_sequence_narrative
        },
        "pain_points_and_solutions": {
            "pain_points_addressed": pain_points_addressed,
            "solutions_presented": solutions_presented
        }
    }

if st.button("Generate Emails"):
    st.write(email_inputs)
    with st.spinner("Generating emails..."):
        response = requests.post(app_url + endpoint, json=email_inputs)
        if response.ok:
            emails = response.json()
            st.write(emails)
        else:
            st.write("Error generating emails", response.status_code, response.text)
