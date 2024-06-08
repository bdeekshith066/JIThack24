import streamlit as st
import streamlit.components.v1 as components




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
        <div class="gradient-text">Welcome to Neurowell</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    st.write(":orange[Your neuro-rehabilitation platform. Recovering from a stroke, brain injury, or other neurological conditions, we offer personalized plans, virtual therapy, and support tools]")

    st.image('divider.png')

    st.write('Neurological disorders present immense challenges in rehabilitation due to the complexity of physical and mental hurdles, exacerbated by the lack of personalized and integrated solutions. Traditional approaches often fall short in addressing diverse patient needs, with limited accessibility and fragmented care hindering progress. Neurowell aims to revolutionize neuro-rehabilitation by offering personalized care plans, technology-driven accessibility, integration of rehabilitation efforts, and data-driven insights, ultimately transforming patient outcome')
    
    
    col4, col5,col7, col6 = st.columns([0.03,0.45,0.07,0.5])
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
            
            st.write("- Progressive neurological disorders often lead to :orange[worsening symptoms over time], impacting daily functioning and quality of life.")
            
            st.write('')
            


        with tab2:
            st.subheader("Preventions")
            st.write("- :orange[Regular exercise] and a healthy lifestyle, including a :orange[balanced diet and sufficient sleep], can help maintain overall brain health and reduce the risk of developing neurological disorders,  decline associated with aging ")
            st.write("- :orange[Avoiding head injuries] through the use of protective gear during sports or activities that carry a risk of head trauma can help prevent conditions like TBI.")
            
            st.write("- Engaging in activities that stimulate the brain, such as :orange[reading, puzzles, and social interactions], may help maintain cognitive function. ")
            
            st.write('')
            


    st.image('divider.png')
    st.write('')
    st.write('')
    col1,col2,col3 = st.columns([0.5,1,0.5])
    with col2:
        st.write('   Project by team - :orange[BYTEBUDDIES] - Deekshith B , Sanjana W G, KM Skanda ')
    
    
if __name__ == "__main__":
    app()
    
