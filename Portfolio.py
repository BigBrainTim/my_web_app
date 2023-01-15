import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd

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
        - I have been working as a web developer for the past 3 years, with a focus on building responsive and user-friendly websites using HTML, CSS, and JavaScript. I also have experience with popular web development frameworks such as Angular and React, which I use to create dynamic and interactive web applications
        - I have experience working with a variety of programming languages, including Python, Java, ... I have developed software applications for a wide range of industries
        - I am always seeking to learn new technologies and stay up to date with the latest industry trends. I am confident in my ability to deliver high-quality and reliable software and web solutions for any project.
        """)
    with right_column:
        st_lottie(lottie_coding)

#------ Skills ---------

with st.container():
    st.write("---")
    st.header("Skills")
    st.write("##")
    data = {"language":["Html", "Css", "Javascript", "Python", "Java"], "rate":[5,4,3,5,3]}

    data=pd.DataFrame(data)

    data = data.set_index("language")

    st.bar_chart(data)

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





