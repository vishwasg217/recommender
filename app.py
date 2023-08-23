import streamlit as st

def main():
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
    
if __name__ == "__main__":
    main()
