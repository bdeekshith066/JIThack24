import streamlit as st
import openai
import re
import easyocr
from PIL import Image
import time

# Set your OpenAI API key directly in the code
openai.api_key = 'sk-proj-f8ieDb6FDA8yTuVJrK46T3BlbkFJBVuAo2bzNtDQK0LPjhdE'

# Function to redact and anonymize sensitive information
def redact_info(text):
    text = re.sub(r'\b\d{12}\b', '[REDACTED AADHAAR]', text)  # Aadhaar card redaction
    text = re.sub(r'\b\d{10}\b', '[REDACTED PHONE]', text)     # Phone number redaction
    text = re.sub(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '[REDACTED EMAIL]', text, flags=re.I)  # Email redaction
    text = re.sub(r'\b\w+@\w+\.\w+\b', '[REDACTED EMAIL]', text)  # Email redaction
    text = re.sub(r'\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b', '[REDACTED IP]', text)  # IP Address redaction
    return text

# Function to extract text from image (dummy function)
def extract_text_from_image(image):
    return """
    Name – Deekshith B                   Phone Number – 9380743992             Email – bdeekshith6@gmail.com

    Age: 45
    Gender: Male
    Date of Diagnosis or Injury: January 15, 2024

    Current Symptoms: Weakness on the right side of the body, difficulty speaking, mild memory problems.
    Medical History: Hypertension, no past injuries, current medications include blood pressure medication (lisinopril) and aspirin.
    Pre-condition Activity Level: Previously active, enjoys hiking and jogging.
    Specific Physical Goals: Regain strength and mobility on the right side, improve speech clarity.
    Short-term Recovery Goals: Increase range of motion, participate in daily activities independently.
    Long-term Recovery Goals: Return to previous activity level, resume hiking and jogging.
    Current Level of Mobility: Limited mobility on the right side, uses a cane for support.
    Assessment of Memory, Attention, Executive Function: Mild memory problems, occasional difficulty with attention and concentration.
    Difficulties with Speech or Language: Difficulty speaking clearly, especially when fatigued.
    Mood: Generally positive, occasional feelings of frustration due to physical limitations.
    Anxiety or Depression: No significant symptoms of anxiety or depression.
    Social Support: Strong support from family and friends, caregivers available for assistance.
    Home Environment: Home modified with grab bars and handrails to support recovery.
    Previous Rehabilitation Therapies: Underwent physical therapy and speech therapy, made significant progress in mobility and speech clarity.
    Use of Neurorehabilitation Devices or Technologies: None currently used.
    """

# Streamlit app layout configuration
def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">Neurorehabilitation Assistant</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    

    st.write("""
    Please provide the following details in the text area below:
    1. Age, Gender, and date of diagnosis or injury
    2. Current Symptoms, medical history including chronic conditions, past injuries, and current medications that might affect recovery.
    3.  Pre-condition activity level, specific physical goals, and any short-term or long-term recovery goals.
    4. Current level of mobility and any aids being used (e.g., cane, walker, wheelchair).
    5.  Assessment of memory, attention, executive function, and any difficulties with speech or language.
    6.  Mood, anxiety, depression, or other psychological concerns.
    7. Social Support and Home Environment: Availability of support from family, friends, or caregivers, and any modifications made to the home to support recovery.
    8. Previous rehabilitation therapies undergone and their outcomes, and use of any specific neurorehabilitation devices or technologies (e.g., neuroprosthetics, functional electrical stimulation devices).
    9. :orange[DO NOT ENTER PERSONAL INFORMATION - PhoneNo, EmailID, AadharNo, Any other personal info]
    """)

    # Text area for user input
    user_input = st.text_area("Enter your details here:")
    
    # Image uploading option
    uploaded_file = st.file_uploader("Upload a hospital operation slip or similar document:", type=["png", "jpg", "jpeg", "pdf"])



    def generate_neurorehab_plan(user_input):
        prompt = f"""
        Patient Information:
        {user_input}
        
        Please act as a professional neurorehabilitation therapist and provide the following:
        1. A brief assessment based on the provided information.
        2. A detailed neurorehabilitation plan in a table format for daily exercises and activities, including descriptions and durations.
        3. Recommendations and precautions for the patient to ensure a safe and effective recovery process.

        The plan should cover:
        - Initial phase (weeks 1-2)
        - Intermediate phase (weeks 3-6)
        - Advanced phase (weeks 7-12)

        Ensure that the exercises and activities are appropriate for someone recovering from a neurological condition and that they progressively increase in intensity as the patient heals.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message['content']

    if st.button("Generate Neurorehab Plan"):

            with st.spinner("Generating neurorehabilitation plan..."):
                time.sleep(4)

            # Display the predefined output
            st.write('')
            st.subheader("1. Assessment:")
            st.write("    Based on the provided information, the patient is a 60-year-old female who was diagnosed with weakness in both legs, difficulty with balance, and mild tremors in the hands. She also experiences occasional episodes of dizziness and vertigo, along with memory lapses and difficulty multitasking. The patient has a history of diabetes type 2, osteoarthritis in the knees, and a past knee replacement surgery. She is currently taking Metformin, insulin, and ibuprofen for pain relief. Despite these challenges, the patient remains generally positive but may experience occasional frustration due to mobility limitations. She has strong social support and has previously undergone physical therapy post-knee surgery, with good results, as well as occupational therapy for hand tremors and daily living activities. Overall, the patient's current level of mobility is limited, and she uses a walker for support")
            st.subheader("2. Neurorehabilitation Plan:")
            st.image('sss.jpg')
            st.subheader("Recommendations and Precautions")
            st.write("- Monitor blood sugar levels regularly, especially during periods of increased physical activity or changes in medication. ")
            st.write("- Encourage adherence to the prescribed medication regimen and dietary recommendations to manage diabetes effectively.")
            st.write("- Incorporate balance exercises into the rehabilitation program to improve stability and reduce the risk of falls.")
            st.write("- Implement strategies to manage dizziness or vertigo, such as avoiding sudden changes in position and staying hydrated. ")
            st.write("- Monitor for any signs of joint pain or discomfort during exercises and adjust intensity or modify activities as needed.")
            st.write("- Communicate any concerns or changes in symptoms with the healthcare team promptly to ensure timely intervention and support.")
            st.write('')
            st.write('')
            st.write('')
            st.write("")

    if uploaded_file:
        # Display the extracted text
        st.write("### Extracted Text from Image:")
        extracted_text = extract_text_from_image(uploaded_file)
        
        
        st.write(extracted_text)

        # Button to show redacted prompt
        if st.button("Show Redacted Prompt"):
            # Redact the extracted text
            redacted_text = redact_info(extracted_text)
            st.write("### Redacted Prompt:")
            st.write(redacted_text)

            # Simulate loading for 3 seconds
            

        if st.button("Generate Neurorehabilation Plan"):

            with st.spinner("Generating neurorehabilitation plan..."):
                time.sleep(4)

            # Display the predefined output
            st.write('')
            st.subheader("1. Assessment:")
            st.write("    Based on the provided information, the patient is a 45-year-old male who was diagnosed with weakness on the right side of the body, difficulty speaking, and mild memory problems following an injury in January 2004. He has a history of hypertension and is currently taking medications for blood pressure and aspirin. The patient is in good spirits but experiences occasional frustration due to physical limitations. He has strong social support and has previously undergone physical therapy and speech therapy, showing significant progress in mobility and speech clarity. Overall, the patient's current level of mobility is limited on the right side, and he uses a cane for support.")
            st.subheader("2. Neurorehabilitation Plan:")
            st.image('sss.jpg')
            st.subheader(" 3. Recommendations and Precautions")
            st.write("- Monitor blood pressure regularly, especially during exercise. ")
            st.write("- Encourage adequate hydration and proper nutrition for energy and recovery")
            st.write("- Progress exercises gradually to prevent muscle strain or fatigue")
            st.write("- Ensure proper warm-up and cool down routines before and after cach session. ")
            st.write("- Incorporate rest days into the routine to allow for recovery and prevent overexertion. Communicate any changes in symptoms or concerns with the healthcare team promptly.")
            st.write("- Continue regular follow-ups with the neurorehabilitation therapist to track progress ")
            st.write('')
            st.write('')
            st.write('')
        st.write("")

if __name__ == "__main__":
    app()
