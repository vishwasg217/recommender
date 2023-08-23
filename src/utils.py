# Function to gather user inputs
def gather_user_inputs():
    print("1. Business Information:")
    business_name = input("   - Business Name: ")
    business_type = input("   - Business Type/Niche: ")
    campaign_goal = input("   - Campaign Goal: ")
    audience_demographics = input("   - Audience Demographics: ")

    print("\n2. Content Guidelines:")
    content_type = input("   - Content Type: ")
    key_message = input("   - Key Message: ")

    print("\n3. Email Structure:")
    call_to_action = input("   - Call to Action (CTA): ")

    print("\n4. Product/Service Information (If Applicable):")
    product_details = input("   - Product/Service Details: ")
    features_benefits = input("   - Features and Benefits: ")

    print("\n5. Tone and Voice:")
    communication_tone = input("   - Communication Tone: ")
    brand_voice = input("   - Brand Voice: ")

    print("\n6. Storyline Progression:")
    email_sequence_narrative = input("   - Email Sequence Narrative: ")

    print("\n7. Pain Points and Solutions:")
    pain_points = input("   - Pain Points Addressed (comma-separated list): ").split(",")
    solutions_presented = input("   - Solutions Presented (comma-separated list): ").split(",")

    inputs = {
        "business_name": business_name,
        "business_type": business_type,
        "campaign_goal": campaign_goal,
        "audience_demographics": audience_demographics,
        "content_type": content_type,
        "key_message": key_message,
        "call_to_action": call_to_action,
        "product_details": product_details,
        "features_benefits": features_benefits,
        "communication_tone": communication_tone,
        "brand_voice": brand_voice,
        "email_sequence_narrative": email_sequence_narrative,
        "pain_points": pain_points,
        "solutions_presented": solutions_presented,
    }
    return inputs

# Gather user inputs
user_inputs = gather_user_inputs()

# Print gathered inputs
print("\nGathered Inputs:")
for section, values in user_inputs.items():
    print(f"{section.replace('_', ' ')}:")
    if isinstance(values, list):
        print("\n".join(f"   - {value}" for value in values))
    else:
        print(f"   - {values}")
    print("=" * 50)
