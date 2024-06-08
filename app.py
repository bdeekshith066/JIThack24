import streamlit as st
import auth_functions


st.markdown("""
        <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            margin-top: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)



# Set up the session state
if 'user_info' not in st.session_state:
    st.session_state.user_info = None

if 'user_type' not in st.session_state:
    st.session_state.user_type = None

# -------------------------------------------------------------------------------------------------
# Initial Page -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
if st.session_state.user_info is None:
    
    col1, col2, col3 = st.columns([1, 2, 1])

    # User type selection
    st.session_state.user_type = col2.selectbox(label='Are you a nurse or a patient?', options=('Doctor', 'Patient'))

    # Authentication form layout
    do_you_have_an_account = col2.selectbox(label='Do you have an account?', options=('Yes', 'No', 'I forgot my password'))
    auth_form = col2.form(key='Authentication form', clear_on_submit=False)
    email = auth_form.text_input(label='Email')
    password = auth_form.text_input(label='Password', type='password') if do_you_have_an_account in {'Yes', 'No'} else auth_form.empty()
    auth_notification = col2.empty()

    # Sign In
    if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In', use_container_width=True, type='primary'):
        with auth_notification, st.spinner('Signing in'):
            auth_functions.sign_in(email, password)

    # Create Account
    elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account', use_container_width=True, type='primary'):
        with auth_notification, st.spinner('Creating account'):
            auth_functions.create_account(email, password)

    # Password Reset
    elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email', use_container_width=True, type='primary'):
        with auth_notification, st.spinner('Sending password reset link'):
            auth_functions.reset_password(email)

    # Authentication success and warning messages
    if 'auth_success' in st.session_state:
        auth_notification.success(st.session_state.auth_success)
        del st.session_state.auth_success
    elif 'auth_warning' in st.session_state:
        auth_notification.warning(st.session_state.auth_warning)
        del st.session_state.auth_warning

# -------------------------------------------------------------------------------------------------
# Logged in ----------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
else:
    # Determine dashboard based on user type
    if st.session_state.user_type == 'Doctor':
        # Load doctor dashboard
        st.title('Doctor Dashboard')
        # Include the rest of the doctor's dashboard code here
        # Example: st.write("Welcome, Doctor!")
        
    elif st.session_state.user_type == 'Patient':
        # Load patient dashboard
        st.title('Patient Dashboard')
        

        from streamlit_option_menu import option_menu
        import home,  bot,  vision,  pedia, therapy

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
        

        # Reducing whitespace on the top of the page
        

        class MultiApp:
            def __init__(self):
                self.app = []

            def add_app(self, title, func):
                self.app.append({
                    "title": title,
                    "function": func
                })   

            def run(self):
                with st.sidebar:
                    st.markdown("""
                    <style>
                    .gradient-text {
                        margin-top: -20px;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    typing_animation = """
                    <h3 style="text-align: left;">
                    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&Left=true&vLeft=true&width=500&height=70&lines=physio+-+man" alt="Typing Animation" />
                    </h3>
                    """
                    st.markdown(typing_animation, unsafe_allow_html=True)

                    app = option_menu(
                        menu_title='Sections',
                        options=['Home', 'Bot','Theraphy', 'Vision', 'Pedia'],
                        default_index=0,
                    )

                    st.sidebar.write("")
                    linkedin_url = "https://www.linkedin.com/in/deekshith2912/"
                    linkedin_link = f"[ByteBuddies]({linkedin_url})"
                    st.sidebar.header(f"Developed by {linkedin_link}")

                if app == "Home":
                    home.app()
                elif app == "Bot":
                    bot.app()
                elif app == "Therapy":
                    therapy.app()
                elif app == "Vision":
                    vision.app()
                elif app == "Pedia":
                    pedia.app()

        # Create an instance of the MultiApp class and run the app
        MultiApp().run()
