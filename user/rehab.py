import streamlit as st
import time
import os
import time as tm
import random
import base64
import json
from PIL import Image
from streamlit_autorefresh import st_autorefresh
import speech_recognition as sr
import openai
import random


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
            font-size: 3.2em;
        }
        </style>
        <div class="gradient-text">Rehab</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    st.write('Caring for you always!! ')
    

    with st.form("speech"):

        st.subheader("1. Speech Therapy Session")

        st.write("Welcome to the Speech Therapy Session!")
        st.write(":orange[Please click the button below and speak the paragraph after the prompt.Repeat the given paragraph as accurately as possible.Automatic pause if u stop speaking]")
        
        

    
        predefined_responses = [
        "Your pronunciation is clear and understandable. Your efforts are commendable, and with consistent practice, you'll continue to refine your speech. Keep up the good work, Everyday practice this twice.!",
        "While you're making progress, it might be beneficial to slow down your speech slightly and enunciate each word clearly. With a bit of patience and practice, you'll notice significant improvements.",
        "It seems like you're facing some challenges with pronunciation. Remember to focus on articulating each word distinctly, and don't hesitate to ask for assistance or clarification when needed. Your dedication to improvement is admirable."
        ]

        def generate_paragraph():
        # Generate a random paragraph for speech therapy
        # This function can be replaced with the actual paragraph generation logic
            paragraphs = [
            "The sun gently kissed the horizon as it dipped below the vast expanse of the ocean, painting the sky in hues of orange and pink. Seagulls soared gracefully overhead, their calls echoing against the sound of crashing waves. A gentle breeze carried the scent of salt in the air, mingling with the laughter of children playing on the sandy shore.",
            "Nestled amidst rolling hills and lush greenery, the quaint village exuded an aura of tranquility and charm. Stone cottages with thatched roofs lined narrow cobblestone streets, adorned with colorful flower boxes. The village square bustled with activity, as locals gathered to chat over steaming cups of tea and freshly baked pastries..",
            "The old bookstore stood as a testament to time, its weathered façade inviting passersby to step into a world of literary wonders. Rows upon rows of books filled the shelves, each one whispering tales of adventure, romance, and mystery. The scent of aging paper lingered in the air, evoking nostalgia in those who wandered its aisles."
            ]
            return random.choice(paragraphs)

        def analyze_response(user_response):
        # Dummy analysis: randomly select one of the predefined responses
            return random.choice(predefined_responses)


        

        # Button to start listening for audio input
        if st.form_submit_button("Click here to start"):
            st.write("Here's a new paragraph for your next session:")
            st.write(generate_paragraph())
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.write("Listening...")
                audio = recognizer.listen(source)

            try:
                st.write("Recognizing...")
                user_response = recognizer.recognize_google(audio)
                st.write("You said:", user_response)
                analysis = analyze_response(user_response)
                st.write("Analysis:", analysis)
            except sr.UnknownValueError:
                st.write("Sorry, I couldn't understand your speech.")
            except sr.RequestError as e:
                st.write(f"Could not request results from Google Speech Recognition service; {e}")

    st.write('---')

   
    
    
    with st.form("game"):
        vDrive = os.path.splitdrive(os.getcwd())[0]
        if vDrive == "C:": vpth = "C:/Users/Shawn/dev/utils/pixmatch/"   # local developer's disc
        else: vpth = "./"

        sbe = """<span style='font-size: 140px;
                            border-radius: 7px;
                            text-align: center;
                            display:inline;
                            padding-top: 3px;
                            padding-bottom: 3px;
                            padding-left: 0.4em;
                            padding-right: 0.4em;
                            '>
                            |fill_variable|
                            </span>"""

        pressed_emoji = """<span style='font-size: 24px;
                                        border-radius: 7px;
                                        text-align: center;
                                        display:inline;
                                        padding-top: 3px;
                                        padding-bottom: 3px;
                                        padding-left: 0.2em;
                                        padding-right: 0.2em;
                                        '>
                                        |fill_variable|
                                        </span>"""

        horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line
        purple_btn_colour = """
                                <style>
                                    div.stButton > button:first-child {background-color: #4b0082; color:#ffffff;}
                                    div.stButton > button:hover {background-color: RGB(0,112,192); color:#ffffff;}
                                    div.stButton > button:focus {background-color: RGB(47,117,181); color:#ffffff;}
                                </style>
                            """

        mystate = st.session_state
        if "expired_cells" not in mystate: mystate.expired_cells = []
        if "myscore" not in mystate: mystate.myscore = 0
        if "plyrbtns" not in mystate: mystate.plyrbtns = {}
        if "sidebar_emoji" not in mystate: mystate.sidebar_emoji = ''
        if "emoji_bank" not in mystate: mystate.emoji_bank = []
        if "GameDetails" not in mystate: mystate.GameDetails = ['Medium', 6, 7, '']  # difficulty level, sec interval for autogen, total_cells_per_row_or_col, player name

        # common functions
        def ReduceGapFromPageTop(wch_section = 'main page'):
            if wch_section == 'main page': st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", True) # main area
            elif wch_section == 'sidebar': st.markdown(" <style> div[class^='st-emotion-cache-10oheav'] { padding-top: 0rem; } </style> ", True) # sidebar
            elif wch_section == 'all': 
                st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", True) # main area
                st.markdown(" <style> div[class^='st-emotion-cache-10oheav'] { padding-top: 0rem; } </style> ", True) # sidebar
            
        

            

        
            
            

                

            

            

        def ReadPictureFile(wch_fl):
            try:
                pxfl = f"{vpth}{wch_fl}"
                return base64.b64encode(open(pxfl, 'rb').read()).decode()

            except: return ""

        def PressedCheck(vcell):
            if mystate.plyrbtns[vcell]['isPressed'] == False:
                mystate.plyrbtns[vcell]['isPressed'] = True
                mystate.expired_cells.append(vcell)

                if mystate.plyrbtns[vcell]['eMoji'] == mystate.sidebar_emoji:
                    mystate.plyrbtns[vcell]['isTrueFalse'] = True
                    mystate.myscore += 5

                    if mystate.GameDetails[0] == 'Easy': mystate.myscore += 5
                    elif mystate.GameDetails[0] == 'Medium': mystate.myscore += 3
                    elif mystate.GameDetails[0] == 'Hard': mystate.myscore += 1
                
                else:
                    mystate.plyrbtns[vcell]['isTrueFalse'] = False
                    mystate.myscore -= 1

        def ResetBoard():
            total_cells_per_row_or_col = mystate.GameDetails[2]

            sidebar_emoji_no = random.randint(1, len(mystate.emoji_bank))-1
            mystate.sidebar_emoji = mystate.emoji_bank[sidebar_emoji_no]

            sidebar_emoji_in_list = False
            for vcell in range(1, ((total_cells_per_row_or_col ** 2)+1)):
                rndm_no = random.randint(1, len(mystate.emoji_bank))-1
                if mystate.plyrbtns[vcell]['isPressed'] == False:
                    vemoji = mystate.emoji_bank[rndm_no]
                    mystate.plyrbtns[vcell]['eMoji'] = vemoji
                    if vemoji == mystate.sidebar_emoji: sidebar_emoji_in_list = True

            if sidebar_emoji_in_list == False:  # sidebar pix is not on any button; add pix randomly
                tlst = [x for x in range(1, ((total_cells_per_row_or_col ** 2)+1))]
                flst = [x for x in tlst if x not in mystate.expired_cells]
                if len(flst) > 0:
                    lptr = random.randint(0, (len(flst)-1))
                    lptr = flst[lptr]
                    mystate.plyrbtns[lptr]['eMoji'] = mystate.sidebar_emoji

        def PreNewGame():
            total_cells_per_row_or_col = mystate.GameDetails[2]
            mystate.expired_cells = []
            mystate.myscore = 0

            
        
            foods = ['🍏', '🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🥭', '🍍', '🥥', '🥝', '🍅', '🍆', '🥑', '🥦', '🥬', '🥒', '🌽', '🥕', '🧄', '🧅', '🥔', '🍠', '🥐', '🥯', '🍞', '🥖', '🥨', '🧀', '🥚', '🍳', '🧈', '🥞', '🧇', '🥓', '🥩', '🍗', '🍖', '🦴', '🌭', '🍔', '🍟', '🍕']
            clocks = ['🕓', '🕒', '🕑', '🕘', '🕛', '🕚', '🕖', '🕙', '🕔', '🕤', '🕠', '🕕', '🕣', '🕞', '🕟', '🕜', '🕢', '🕦']
            hands = ['🤚', '🖐', '✋', '🖖', '👌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '🤲', '🤝', '🤚🏻', '🖐🏻', '✋🏻', '🖖🏻', '👌🏻', '🤏🏻', '✌🏻', '🤞🏻', '🤟🏻', '🤘🏻', '🤙🏻', '👈🏻', '👉🏻', '👆🏻', '🖕🏻', '👇🏻', '☝🏻', '👍🏻', '👎🏻', '✊🏻', '👊🏻', '🤛🏻', '🤜🏻', '👏🏻', '🙌🏻', '🤚🏽', '🖐🏽', '✋🏽', '🖖🏽', '👌🏽', '🤏🏽', '✌🏽', '🤞🏽', '🤟🏽', '🤘🏽', '🤙🏽', '👈🏽', '👉🏽', '👆🏽', '🖕🏽', '👇🏽', '☝🏽', '👍🏽', '👎🏽', '✊🏽', '👊🏽', '🤛🏽', '🤜🏽', '👏🏽', '🙌🏽']
            animals = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐵', '🙈', '🙉', '🙊', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', '🦋', '🐌', '🐞', '🐜', '🦟', '🦗', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐓', '🦃', '🦚', '🦜', '🦢', '🦩', '🐇', '🦝', '🦨', '🦦', '🦥', '🐁', '🐀', '🦔']
            vehicles = ['🚗', '🚕', '🚙', '🚌', '🚎', '🚓', '🚑', '🚒', '🚐', '🚚', '🚛', '🚜', '🦯', '🦽', '🦼', '🛴', '🚲', '🛵', '🛺', '🚔', '🚍', '🚘', '🚖', '🚡', '🚠', '🚟', '🚃', '🚋', '🚞', '🚝', '🚄', '🚅', '🚈', '🚂', '🚆', '🚇', '🚊', '🚉', '✈️', '🛫', '🛬', '💺', '🚀', '🛸', '🚁', '🛶', '⛵️', '🚤', '🛳', '⛴', '🚢']
            
            moon = ['🌕', '🌔', '🌓', '🌗', '🌒', '🌖', '🌑', '🌜', '🌛', '🌙']

            random.seed()
            if mystate.GameDetails[0] == 'Easy':
                wch_bank = random.choice(['foods'])
                mystate.emoji_bank = locals()[wch_bank]

            
            mystate.plyrbtns = {}
            for vcell in range(1, ((total_cells_per_row_or_col ** 2)+1)): mystate.plyrbtns[vcell] = {'isPressed': False, 'isTrueFalse': False, 'eMoji': ''}

        def ScoreEmoji():
            if mystate.myscore == 0: return '😐'
            elif -5 <= mystate.myscore <= -1: return '😏'
            elif -10 <= mystate.myscore <= -6: return '☹️'
            elif mystate.myscore <= -11: return '😖'
            elif 1 <= mystate.myscore <= 5: return '🙂'
            elif 6 <= mystate.myscore <= 10: return '😊'
            elif mystate.myscore > 10: return '😁'

        def NewGame():
            ResetBoard()
            total_cells_per_row_or_col = mystate.GameDetails[2]

            ReduceGapFromPageTop('sidebar')
            
            

            st.markdown(sbe.replace('|fill_variable|', mystate.sidebar_emoji), True)

            aftimer = st_autorefresh(interval=(mystate.GameDetails[1] * 1000), key="aftmr")
            if aftimer > 0: mystate.myscore -= 1

            st.info(f"{ScoreEmoji()} Score: {mystate.myscore} | Pending: {(total_cells_per_row_or_col ** 2)-len(mystate.expired_cells)}")

            st.markdown(horizontal_bar, True)
            
            
            

            # Set Board Dafaults
            st.markdown("<style> div[class^='css-1vbkxwb'] > p { font-size: 1.5rem; } </style> ", unsafe_allow_html=True)  # make button face big

            for i in range(1, (total_cells_per_row_or_col+1)):
                tlst = ([1] * total_cells_per_row_or_col) + [2] # 2 = rt side padding
                globals()['cols' + str(i)] = st.columns(tlst)
            
            for vcell in range(1, (total_cells_per_row_or_col ** 2)+1):
                if 1 <= vcell <= (total_cells_per_row_or_col * 1):
                    arr_ref = '1'
                    mval = 0

                elif ((total_cells_per_row_or_col * 1)+1) <= vcell <= (total_cells_per_row_or_col * 2):
                    arr_ref = '2'
                    mval = (total_cells_per_row_or_col * 1)

                elif ((total_cells_per_row_or_col * 2)+1) <= vcell <= (total_cells_per_row_or_col * 3):
                    arr_ref = '3'
                    mval = (total_cells_per_row_or_col * 2)

                elif ((total_cells_per_row_or_col * 3)+1) <= vcell <= (total_cells_per_row_or_col * 4):
                    arr_ref = '4'
                    mval = (total_cells_per_row_or_col * 3)

                elif ((total_cells_per_row_or_col * 4)+1) <= vcell <= (total_cells_per_row_or_col * 5):
                    arr_ref = '5'
                    mval = (total_cells_per_row_or_col * 4)

                elif ((total_cells_per_row_or_col * 5)+1) <= vcell <= (total_cells_per_row_or_col * 6):
                    arr_ref = '6'
                    mval = (total_cells_per_row_or_col * 5)

                elif ((total_cells_per_row_or_col * 6)+1) <= vcell <= (total_cells_per_row_or_col * 7):
                    arr_ref = '7'
                    mval = (total_cells_per_row_or_col * 6)

                elif ((total_cells_per_row_or_col * 7)+1) <= vcell <= (total_cells_per_row_or_col * 8):
                    arr_ref = '8'
                    mval = (total_cells_per_row_or_col * 7)

                elif ((total_cells_per_row_or_col * 8)+1) <= vcell <= (total_cells_per_row_or_col * 9):
                    arr_ref = '9'
                    mval = (total_cells_per_row_or_col * 8)

                elif ((total_cells_per_row_or_col * 9)+1) <= vcell <= (total_cells_per_row_or_col * 10):
                    arr_ref = '10'
                    mval = (total_cells_per_row_or_col * 9)
                    
                globals()['cols' + arr_ref][vcell-mval] = globals()['cols' + arr_ref][vcell-mval].empty()
                if mystate.plyrbtns[vcell]['isPressed'] == True:
                    if mystate.plyrbtns[vcell]['isTrueFalse'] == True:
                        globals()['cols' + arr_ref][vcell-mval].markdown(pressed_emoji.replace('|fill_variable|', '✅️'), True)
                    
                    elif mystate.plyrbtns[vcell]['isTrueFalse'] == False:
                        globals()['cols' + arr_ref][vcell-mval].markdown(pressed_emoji.replace('|fill_variable|', '❌'), True)

                else:
                    vemoji = mystate.plyrbtns[vcell]['eMoji']
                    globals()['cols' + arr_ref][vcell-mval].button(vemoji, on_click=PressedCheck, args=(vcell, ), key=f"B{vcell}")

            st.caption('') # vertical filler
            st.markdown(horizontal_bar, True)

            if len(mystate.expired_cells) == (total_cells_per_row_or_col ** 2):
                

                if mystate.myscore > 0: st.balloons()
                elif mystate.myscore <= 0: st.snow()

                tm.sleep(5)
                mystate.runpage = Main
                st.rerun()

        def Main():
            st.markdown('<style>[data-testid="stSidebar"] > div:first-child {width: 310px;}</style>', unsafe_allow_html=True,)  # reduce sidebar width
            st.markdown(purple_btn_colour, unsafe_allow_html=True)

            
            
        mystate.GameDetails[0] = 'Easy'

        st.subheader('2. PICMATCH')
        st.write(':orange[PicMatch - Match emojis scattered across the grid to the ones displayed in the image]')

        _LOREM_IPSUM = """Engage in a dynamic blend of memory exercises, problem-solving tasks, and attention training in this immersive and challenging game."""
        def stream_data():
            for word in _LOREM_IPSUM.split(" "):
                    yield word + " "
                    time.sleep(0.08)
        if st.form_submit_button("Why play this game"):
                st.write_stream(stream_data)
        st.write('')
                

        if st.form_submit_button(f"🕹️ Start the  Game", use_container_width=True):

            if mystate.GameDetails[0] == 'Easy':
                mystate.GameDetails[1] = 15         # secs interval
                mystate.GameDetails[2] = 6         # total_cells_per_row_or_col
                    
                    
                    

                PreNewGame()
                mystate.runpage = NewGame
                st.rerun()

        st.markdown(horizontal_bar, True)


    if 'runpage' not in mystate: mystate.runpage = Main
    mystate.runpage()
