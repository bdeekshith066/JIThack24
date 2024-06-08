import streamlit as st
import streamlit.components.v1 as components
from googletrans import Translator

st.set_page_config(layout="wide", page_title="Neuro Well", page_icon="🧠")

# CSS for styling
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)



# Initialize session state for the button click
if "community_clicked" not in st.session_state:
    st.session_state.community_clicked = False

# Define columns
col1, col2  = st.columns([0.4,1])

# Add gradient text
with col2:
    gradient_text_html = """
    <style>
    .gradient-text {
        font-weight: bold;
        background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
        background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3.0em;
    }
    </style>
    <div class="gradient-text">Welcome to NeuroWell</div>
    """
    st.markdown(gradient_text_html, unsafe_allow_html=True)

# Add image


# Display message based on button click
if st.session_state.community_clicked:
    st.write("hi")

# Additional information
st.write(":orange[Your compr]")




    

    
    
col4, col5,col7, col6,col8,col9,col10 = st.columns([0.03,0.45,0.07,0.5,0.03,0.5,0.03])
with col5:
    st.write('')
        
    components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 400px;
  max-height : 400px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.9s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://www.hiranandanihospital.org/public/uploads/blogs/1691067725.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvCUh1GDnQgqs_1DZ0PbiconH4UKIjl5EOiQ&s">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://risehealthgroup.com.au/wp-content/uploads/2022/03/nerve-pain.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">4 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Y5NNfX-nqjUAsSZS9__gutqQMxrGZDmTRw&s">
    
  </div>
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=300, width=400
)
    

with col6:
    tab0,tab1, tab2 = st.tabs(["Facts", "Symptoms", "Prevention"])

    with tab0:
            st.subheader('Facts')
            st.write("- Neurological disorders affect millions worldwide, with over a :orange[billion people] estimated to be living with some form of neurological condition.")
            st.write("- These disorders are the leading cause of disability globally, contributing to approximately :orange[6.8 %]  of global disability-adjusted life years (DALYs).")
            st.write("- The economic burden of neurological disorders is substantial, with healthcare costs, lost productivity, and caregiving :orange[expenses amounting to billions] annually in many countries.")
            st.write('')
            

    with tab1:
            st.subheader("Symptoms")
            st.write("- Neurological disorders can manifest through a range of symptoms, including but :orange[not limited to] headaches, seizures, weakness, numbness, and difficulty with movement or coordination. ")
            st.write("- Cognitive symptoms such as :orange[memory loss, confusion, and changes in mood] or behavior are common in many neurological conditions.")
            st.write("- Sensory disturbances like tingling sensations, altered perception of touch or pain, and visual or auditory disturbances may also occur.")
            st.write("- Progressive neurological disorders often lead to :orange[worsening symptoms over time], impacting daily functioning and quality of life.")
            
            st.write('')
            


    with tab2:
            st.subheader("Preventions")
            st.write("- :orange[Regular exercise] and a healthy lifestyle, including a :orange[balanced diet and sufficient sleep], can help maintain overall brain health and reduce the risk of developing neurological disorders ")
            st.write("- :orange[Avoiding head injuries] through the use of protective gear during sports or activities that carry a risk of head trauma can help prevent conditions like traumatic brain injury (TBI).")
            st.write("- Managing chronic conditions such as hypertension, diabetes, and high cholesterol through medication, lifestyle modifications, and regular medical check-ups can lower the risk of developing certain neurological disorders.")
            st.write("- Engaging in activities that stimulate the brain, such as :orange[reading, puzzles, and social interactions], may help maintain cognitive function and reduce the risk of cognitive decline associated with aging or neurodegenerative diseases ")
            
            st.write('')
            st.write('Follow the above steps  to promote overall heart health and well-being.  \n :orange[Nothing beats a healthy body] ')

with col9:
      st.title('Our features')
    
    

    
target_languages = {
        "English": "en",
        "Hindi": "hi",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Telugu": "te",
        "Tamil": "ta",
        "Punjabi": "pa",
        "French": "fr",
        "Spanish": "es",
        "German": "de"
    }
col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
        st.button('Stroke')
        st.write('')
        st.write('')
        st.write('')
        st.button('Aphasia')
        st.write('')
        st.write('')
        st.write('')
        st.button('Dysphagia:')
        st.write('')
        st.write('')
        st.write('')
        st.button('FAST')

with col2:
        st.button('Ischemic Stroke')
        st.write('')
        st.write('')
        st.write('')
        st.button('Rehabilation')
        st.write('')
        st.write('')
        st.write('')
        st.button('Secondary Stroke Prevention')
        st.write('')
        st.write('')
        st.write('')
        st.button('Atrial Fibrillation (AFib')

with col3:
        st.button('Hemorrhagic Stroke:')
        st.write('')
        st.write('')
        st.write('')
        st.button('Thrombolytic Therapy)')
        st.write('')
        st.write('')
        st.write('')
        st.button('Endovascular Thrombectomy')
        st.write('')
        st.write('')
        st.write('')
        st.button('Modified Rankin Scale (mRS')
    
    
with col4:
        st.button('Transient Ischemic Attack (TIA)')
        st.write('')
        st.write('')
        st.write('')
        st.button('NIH Stroke Scale (NIHSS)')
        st.write('')
        st.write('')
        st.write('')
        st.button('Modified Rankin Scale (mRS)')
        st.write('')
        st.write('')
        st.write('')
        target_language = st.selectbox("Select Language", list(target_languages.keys()))
        
    # Language selection
    

    

def get_pedia_info(user_input, target_language='en'):
    pedia_info = {
            "stroke": """ :orange[Stroke]  \n  \n :orange[Understanding Stroke]  \n  A stroke, often referred to as a "brain attack," occurs when the blood supply to part of the brain is interrupted or reduced, depriving brain tissue of oxygen and nutrients. This sudden disruption can lead to brain cell damage and potentially life-altering consequences. Strokes are a medical emergency and require immediate attention to minimize long-term complications and improve outcomes.  \n  \n  :orange[Treatment and Recovery]  \n  Treatment for stroke often involves clot-busting medications and sometimes surgery to remove clots or repair damaged blood vessels. Post-stroke rehabilitation, including physical, occupational, and speech therapy, helps survivors regain lost abilities. While recovery varies, many stroke survivors make significant progress with therapy and support.  \n  \n :orange[Prevention Strategies]  \n Preventing stroke involves managing risk factors like high blood pressure, diabetes, and smoking. Adopting a healthy lifestyle, including regular exercise and a balanced diet, can reduce the likelihood of stroke. Regular check-ups and medication adherence are essential for individuals at risk. By prioritizing prevention, individuals can lower their chances of experiencing a stroke and lead healthier lives.  \n  \n
            Enter the name of a term from the HeartPedia to know more about it  """,




            "rehabilation": """ Rehabilation  \n  \n Understanding Rehabilitation  \n  Stroke rehabilitation is a crucial aspect of recovery, aiming to help survivors regain independence and improve quality of life. It encompasses various therapies, including physical, occupational, and speech therapy, tailored to individual needs. Rehabilitation efforts focus on restoring lost functions, enhancing mobility, and promoting overall well-being.   \n  \n  Treatment Approaches  \n   Rehabilitation after stroke involves a multidisciplinary approach, combining therapeutic exercises, assistive devices, and adaptive strategies. Physical therapy aims to improve strength, coordination, and mobility, while occupational therapy focuses on relearning daily activities and enhancing fine motor skills. Speech therapy addresses communication difficulties and swallowing disorders, facilitating language and cognitive recovery.  \n  \n Support and Progress  \n  Stroke rehabilitation is a gradual process, and progress varies for each individual. Support from healthcare professionals, caregivers, and support groups is invaluable during this journey. Setting realistic goals and celebrating milestones can boost morale and motivation. With dedication and perseverance, many stroke survivors experience significant improvements in function and quality of life through rehabilitation  \n  \n
            Enter the name of a term from the HeartPedia to know more about it  """,

            "aphasia" : """ :orange[Aphasia]  \n  Understanding Aphasia  \n Aphasia is a complex neurological condition that affects a person's ability to communicate effectively. It often occurs as a result of brain damage, typically from a stroke, brain injury, or neurological disorder. Individuals with aphasia may struggle with speaking, understanding language, reading, and writing, which can significantly impact their daily lives and interpersonal relationships.  \n - Types and Symptoms  \n -  There are different types of aphasia, each with its unique symptoms and severity. Expressive aphasia, for example, impairs a person's ability to speak fluently and form coherent sentences, while receptive aphasia affects comprehension and understanding of spoken or written language. Additionally, individuals may experience difficulty finding the right words (anomia) or struggle with language repetition. These symptoms vary depending on the location and extent of brain damage.  \n - Treatment and Support  \n  While there is no cure for aphasia, various therapies and interventions can help individuals manage and improve their communication skills. Speech and language therapy, cognitive rehabilitation, and assistive communication devices are commonly used to address aphasia's challenges. Moreover, support groups and counseling provide emotional support and practical strategies for coping with the condition. With proper treatment and support, many individuals with aphasia can regain some level of language function and lead fulfilling lives.  \n - Prompt recognition of heart attack symptoms and calling emergency services (911) is crucial for timely treatment.  \n - Treatment options include medications (aspirin, nitroglycerin), angioplasty, or coronary artery bypass surgery.  \n - Rehabilitation and lifestyle changes (diet, exercise, smoking cessation) are vital for recovery and prevention of future events.  \n
            Enter the name of a term from the HeartPedia to know more about it.""",


            "nih stroke scale": """ :orange[NIH Stroke Scale[NISS]]  \n  \n :orange[Understanding NIH Stroke Scale]  \n  The NIH Stroke Scale (NIHSS) is a standardized tool used by healthcare professionals to assess the severity of stroke and guide treatment decisions. It evaluates various neurological functions, including consciousness, sensation, movement, speech, and visual fields. The NIHSS score helps determine the type of stroke, predict outcomes, and monitor response to treatment.  \n  \n  :orange[Scoring and Interpretation]  \n   The NIHSS consists of 11 items, each scored based on the patient's performance during the evaluation. Higher scores indicate greater stroke severity, with a maximum score of 42. Healthcare providers use the NIHSS score to classify strokes as mild, moderate, or severe and tailor treatment accordingly.  \n  \n :orange[Clinical Utility]  \n The NIH Stroke Scale provides valuable information for clinicians assessing stroke patients in various settings, including emergency departments, stroke units, and rehabilitation facilities. It facilitates communication among healthcare team members and ensures consistent evaluation and management practices. Additionally, the NIHSS score serves as a prognostic indicator, helping healthcare providers make informed decisions about patient care and rehabilitation  \n  \n
            Enter the name of a term from the HeartPedia to know more about it  """,


            "nihss": """ :orange[NIH Stroke Scale[NISS]]  \n  \n :orange[Understanding NIH Stroke Scale]  \n  The NIH Stroke Scale (NIHSS) is a standardized tool used by healthcare professionals to assess the severity of stroke and guide treatment decisions. It evaluates various neurological functions, including consciousness, sensation, movement, speech, and visual fields. The NIHSS score helps determine the type of stroke, predict outcomes, and monitor response to treatment.  \n  \n  :orange[Scoring and Interpretation]  \n   The NIHSS consists of 11 items, each scored based on the patient's performance during the evaluation. Higher scores indicate greater stroke severity, with a maximum score of 42. Healthcare providers use the NIHSS score to classify strokes as mild, moderate, or severe and tailor treatment accordingly.  \n  \n :orange[Clinical Utility]  \n The NIH Stroke Scale provides valuable information for clinicians assessing stroke patients in various settings, including emergency departments, stroke units, and rehabilitation facilities. It facilitates communication among healthcare team members and ensures consistent evaluation and management practices. Additionally, the NIHSS score serves as a prognostic indicator, helping healthcare providers make informed decisions about patient care and rehabilitation  \n  \n
            Enter the name of a term from the HeartPedia to know more about it  """,



            "cardiac arrest": """ :orange[Cardiac Arrest]  \n Cardiac arrest is a sudden loss of heart function, breathing, and consciousness, usually due to an electrical malfunction in the heart.  \n :orange[Importance]  \n -Cardiac arrest is different from a heart attack and requires immediate intervention with CPR and use of an automated external defibrillator (AED).  \n - Survival rates decrease by 7-10% for every minute without CPR or defibrillation.  \n -  Effective bystander CPR can significantly increase the chances of survival and reduce disability.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",



            "coronary artery disease": """:orange[Coronary Artery Disease (CAD)]  \n CAD is a condition where the coronary arteries become narrowed or blocked due to the buildup of plaque, reducing blood flow to the heart.  \n :orange[Risk Factors]  \n - High cholesterol, high blood pressure, smoking, diabetes, obesity, sedentary lifestyle, family history.  \n - Age, gender (men have a higher risk at younger ages; risk increases for women after menopause).  \n - Stress, poor diet (high in saturated fats and sugars), excessive alcohol consumption.  \n :orange[Importance]  \n -CAD is the leading cause of heart attacks and requires comprehensive management of risk factors.  \n - Treatment involves lifestyle modifications (diet, exercise), medications (statins, blood thinners), and interventions (angioplasty, stenting, bypass surgery).  \n - Preventive measures include regular check-ups, cholesterol screenings, and early detection and treatment of risk factors.  \n     
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "hypertension(high bp)" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "hypertension" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "high bp" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "hypertension" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "heart failure" : """:orange[Heart Failure (Congestive Heart Failure)]  \n Heart failure occurs when the heart is unable to pump blood efficiently to meet the body's needs.  \n :orange[Symptoms]  \n - Shortness of breath, especially during physical activity or when lying flat.  \n - Fatigue, weakness, and swelling in the legs, ankles, or abdomen.  \n -Sudden weight gain due to fluid retention.  \n :orange[Importance]  \n - Heart failure is a chronic condition that requires lifelong management with medications (diuretics, ACE inhibitors), dietary changes (low-sodium diet), and exercise.  \n - Monitoring symptoms and regular check-ups are essential to prevent complications and hospitalizations.  \n -  Advanced heart failure may require interventions like heart transplant or mechanical circulatory support (ventricular assist devices).  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "cholesterol" : """ :orange[Cholestrol]  \n : Cholesterol is a fatty substance essential for cell function, transported in the blood by lipoproteins.  :orange[Important]  \n - High levels of low-density lipoprotein (LDL) cholesterol contribute to atherosclerosis and heart disease.  \n - Monitoring cholesterol levels (LDL, HDL, triglycerides) and maintaining a healthy diet (low in saturated fats, trans fats) are crucial for heart health.  \n - Statin medications are commonly prescribed to lower LDL cholesterol and reduce cardiovascular risk.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            

            "peripheral artery disease" : """ :orange[Peripheral Artery Disease (PAD)]  \n PAD is a circulatory condition where narrowed arteries reduce blood flow to the limbs, typically the legs.  \n :orange[Symptoms]  \n - Leg pain (claudication) during walking or exercise, relieved by rest.  \n - Coldness or numbness in the legs or feet.  \n - Slow-healing wounds or ulcers on the feet or toes.  \n :orange[Importance]  \n - PAD is often associated with coronary artery disease and increases the risk of heart attack and stroke.  \n - Treatment includes lifestyle changes (exercise, smoking cessation), medications (antiplatelets, statins), and in severe cases, angioplasty or surgery.  \n - Regular foot care and monitoring are essential to prevent complications like infections or gangrene.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "systolic/diastolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",


            "systolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",

            "diastolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",


            "holter monitor":""":orange[Holter Monitor]  \n A Holter monitor is a portable device worn to continuously record the heart's electrical activity (ECG) over 24-48 hours.  /n :orange[importance]  \n -Holter monitors detect intermittent arrhythmias that may not be captured during a standard ECG.  \n - Used to diagnose palpitations, evaluate symptoms like dizziness or fainting, and monitor response to anti-arrhythmic medications.  \n -Provides valuable data for treatment decisions and arrhythmia management strategies.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",



            "pacemaker" : """:orange[Pacemaker]  \n A pacemaker is a small device implanted under the skin to regulate abnormal heart rhythms (arrhythmias) and maintain a steady heartbeat.  \n :orange[Importance]  \n - Pacemakers monitor heart rate and deliver electrical impulses to stimulate the heart when necessary.  \n - Used to treat bradycardia (slow heart rate) or certain arrhythmias that can cause symptoms like dizziness or fainting.  \n -  Pacemaker checks and programming adjustments are performed regularly by healthcare providers.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "angina pectoris" :""":orange[Angina Pectoris]  \n Angina is chest pain or discomfort caused by reduced blood flow to the heart muscle.  \n :orange[Symptoms]  \n - Pressure, tightness, or burning sensation in the chest, often triggered by physical exertion or stress.  \n - Pain may radiate to the neck, jaw, shoulders, or arms.  \n - Symptoms typically subside with rest or nitroglycerin.  \n  :orange[Importance]  \n - Stable angina indicates underlying coronary artery disease, while unstable angina may precede a heart attack.  \n - Treatment involves lifestyle changes (smoking cessation, stress management), medications (nitroglycerin, beta-blockers), and interventions (angioplasty, stenting).  \n - Prompt medical attention is needed for worsening or new-onset angina symptoms.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "atherosclerosis" : """Atherosclerosis is the buildup of fatty deposits (plaque) within the arteries, leading to narrowing and hardening of the arteries.  \n :orange[Importance]  \n - Atherosclerosis contributes to coronary artery disease, peripheral artery disease, and stroke.  \n -Risk factors include high cholesterol, high blood pressure, smoking, diabetes, and family history.  \n Prevention involves lifestyle changes (healthy diet, exercise), medications (statins, blood thinners), and management of underlying conditions.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "electrocardiogram (ecg)": """An electrocardiogram (ECG or EKG) is a test that records the electrical activity of the heart over a period, typically displayed as a graph of voltage versus time.  \n :orange[Importance]  \n - ECGs help diagnose heart rhythm abnormalities (arrhythmias), conduction disorders, and signs of heart attack or ischemia.  \n - Used routinely in medical settings for initial cardiac assessments and ongoing monitoring of heart health.  \n - Provides valuable information for treatment decisions and management of various heart conditions.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "ecg": """An electrocardiogram (ECG or EKG) is a test that records the electrical activity of the heart over a period, typically displayed as a graph of voltage versus time.  \n :orange[Importance]  \n - ECGs help diagnose heart rhythm abnormalities (arrhythmias), conduction disorders, and signs of heart attack or ischemia.  \n - Used routinely in medical settings for initial cardiac assessments and ongoing monitoring of heart health.  \n - Provides valuable information for treatment decisions and management of various heart conditions.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "stent" : """ :orange[Stent]  \n : A stent is a small mesh tube inserted into a blocked or narrowed artery to improve blood flow  \n :orange[Importance]  \n - Stents are commonly used in coronary artery disease to reopen blocked arteries during angioplasty.  \n -  Drug-eluting stents release medication to prevent re-narrowing (restenosis) of the artery. \n - Stents may also be used in peripheral artery disease and other vascular conditions to relieve symptoms and prevent complications.  \n 
            Enter the name of a term from the HeartPedia  to know more about it."""


            # Add more festivals and their information here
        }

    user_input_lower = user_input.lower()

    if user_input_lower in pedia_info:
            translator = Translator()
            translation = translator.translate(pedia_info[user_input_lower], dest=target_language)
            return translation.text
    else:
            return "I'm sorry, I'm not sure which term you're asking about. Can you please provide more details?"

if "fest_messages" not in st.session_state:
        st.session_state.fest_messages = [{"role": "assistant", "content": "Discover important stroke-related terms and their meanings with our chatbot!"}]

for message in st.session_state.fest_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Enter the Term name"):
    st.session_state.fest_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    language_code = target_languages[target_language]
    response = get_pedia_info(prompt, target_language=language_code)

    with st.spinner(text="Thinking..."):
            st.session_state.fest_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response, unsafe_allow_html=True)


