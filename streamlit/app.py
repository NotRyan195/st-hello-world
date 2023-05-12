from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url) 
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style.css")

# ----- Load Assets -----
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_u8jppxsl.json")
img_contact_form = Image.open("image1.png") 
img_lottie_animation = Image.open("image2.png")

# ----- HEADER SECTOIN ------
with st.container():
    st.subheader("Hi, I am Ryan Chang :wave:")
    st.title("Computer Programmer")
    st.write("I am passionate about finding ways to use my skills and knowledge to be more effective and grow into a leader")


# ----- WHAT I DO -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am 18 seeking to further expand my knowledge to create creative solutions to problems and to broaden the network of people that I can help to further my career at whichever company I serve at: 
            - I am learning the following coding languages;
                - C++ 
                - Python 
                - SEQUEL(SQL)
                - HTML
                - Javascript
            - Hard-working determined achiever learning Data Analysis & web development to make meaningful impact
            
            If this sounds like someone you want working for you then you can reach me at 864-768-5470 or rchang195@gmail.com 
            """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
#  ----- Projects ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Snake Game")
        st.write(
        """
        Created snake game as a test of my knowledge of Python to see where I was as a programmer. The game is complete and playable for anyone with the file. 
        """
    )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
 
 
 # Documention: https://formsubmit.co/ 
contact_form = """ 
 <form action="https://formsubmit.co/rchang195@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" requiured></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column: 
    st.empty()