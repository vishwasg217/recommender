import streamlit as st
import requests
import pyperclip
import json

app_url = "http://localhost:8000"
endpoint = "/generate"
model_url = f"{app_url}{endpoint}"

import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# Default Example Input
with open("test/test_inputs.json", "r") as f:
    default_input = json.load(f)

default_input = default_input["2"]

# Streamlit App
st.title("Email Marketing Campaign Generator")

col1, col2 = st.columns(2)

with col1:
    st.write("## Inputs")
    st.header("Business Information")
    business_name = st.text_input("Business Name", value=default_input["business_information"]["business_name"])
    business_type = st.text_input("Business Type", value=default_input["business_information"]["business_type"])
    campaign_goal = st.text_input("Campaign Goal", value=default_input["business_information"]["campaign_goal"])
    audience_demographics = st.text_area("Audience Demographics", value=default_input["business_information"]["audience_demographics"])

    # Content Guidelines
    st.header("Content Guidelines")
    content_type = st.text_input("Content Type", value=default_input["content_guidelines"]["content_type"])
    key_message = st.text_area("Key Message", value=default_input["content_guidelines"]["key_message"])

    # Email Structure
    st.header("Email Structure")
    call_to_action = st.text_input("Call to Action", value=default_input["email_structure"]["call_to_action"])

    # Product/Service Information

    st.header("Product/Service Information")
    product_service_details = st.text_area("Product/Service Details", value=default_input["product_service_information"]["product_service_details"])
    features_and_benefits = st.text_area("Features and Benefits", value=default_input["product_service_information"]["features_and_benefits"])

    # Tone and Voice
    st.header("Tone and Voice")
    website_url = st.text_input("Website URL", value=default_input["tone_and_voice"]["website_url"])
    communication_tone = st.text_input("Communication Tone", value=default_input["tone_and_voice"]["communication_tone"])
    brand_voice = st.text_input("Brand Voice", value=default_input["tone_and_voice"]["brand_voice"])

    # Storyline Progression
    st.header("Storyline Progression")
    email_sequence_narrative = st.text_area("Email Sequence Narrative", value=default_input["storyline_progression"]["email_sequence_narrative"])

    # Pain Points and Solutions
    st.header("Pain Points and Solutions")
    pain_points_addressed = st.text_area("Pain Points Addressed", value=default_input["pain_points_and_solutions"]["pain_points_addressed"])
    solutions_presented = st.text_area("Solutions Presented", value=default_input["pain_points_and_solutions"]["solutions_presented"])


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
        "product_service_information": {
            "product_service_details": product_service_details,
            "features_and_benefits": features_and_benefits
        },
        "tone_and_voice": {
            "website_url": website_url,
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

with col2:
    st.write("## Output")

if "output" not in st.session_state:
    st.session_state.output = None

if st.button("Generate Emails"):
    st.write(email_inputs)
    with col2:
        with st.spinner("Generating emails..."):
            response = requests.post(model_url, json=email_inputs)
            if response.ok:
                emails = response.json()
                st.session_state.output = emails
            else:
                with col2:
                    st.write("Error generating emails", response.status_code, response.text)

with col2:
    if st.session_state.output:
        if st.button("Copy Emails"):
                pyperclip.copy(st.session_state.output)

        headers = ["Email 1: Introduction and Pain Point",
            "Email 2: Building on Pain Point",
            "Email 3: Solution Presentation",
            "Email 4: Benefits and Social Proof",
            "Email 5: Call to Action and Conclusion"
        ]

        for index, (email_id, email_data) in enumerate(st.session_state.output.items()):
            st.subheader(headers[index])
            st.write("**Subject:**")
            st.write(email_data["subject"])
            st.write(email_data["greeting"])
            st.write(email_data["body"])
            st.write(email_data["signature"])
            st.divider()
        
