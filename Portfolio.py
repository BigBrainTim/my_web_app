import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="W kh", page_icon="coding.png", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("style/style.css")

# ------ load assets ----
lottie_coding = load_lottie("https://assets7.lottiefiles.com/packages/lf20_bzgbs6lx.json")

with st.container():
    st.title("Hi, i'm Wassim khachab :wave:")
    st.write("a professional computer programmer")

#------ About me ------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write("""
        I'm named Wassim Khachab , i'm from morocco , last 3 years i've been focusing on programming and web development and that's been fun , laterly i tried to learn blockchain development , so i have created a digital coin "Glasses coin" (A DECENTRALIZED TOKEN FOCUSED ON REVOLUTIONIZING WEB 3.0) also i dived in the NFT field , and by my programming background , i can generate a full NFT collection , create a minting dapp and create also smart contracts, in my path i faced some hurdles or challenges , one of them is the bad wifi connection :) and also my young age because in many times i needed at least an Identification card , however i'm trying to use my cryptocurrency wallet always as a payment method 
        three Specifications that i always respect:
        - never give up
        - learn 
        - respect time
        """)
    with right_column:
        st_lottie(lottie_coding)

#------ Skills ---------

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("##")
    st.write("""
    - Programming 

    - Coding

    - Web development 

    - Game development

    - NFT 

    - Blockchain development


    """)

# ------ Contact form -------

with st.container():
    st.write("---")
    st.subheader("Contact me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/yo40706260@gmail.com" method="POST">
        <input type="text" name="name" placeholder="name" required>
        <input type="email" name="email" placeholder="e-mail" required>
        <textarea name="message" placeholder="enter your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.subheader("Support me")
    st.write("""
    ##
    My ethereum wallet :

            0x0CA53BfA8FF5016646daE8Ca34951cC35aC37dCE

    My bitcoin wallet :

            bc1qefu8kwwc8lxss69pzfp9tpqhg2srungx4hpdmh

    My BNB wallet:

            0x0CA53BfA8FF5016646daE8Ca34951cC35aC37dCE

    
    """)





