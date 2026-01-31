import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Researcher Profile | Mthokozisi Mathonsi",
    layout="wide"
)

# -----------------------------
# Sidebar (Profile + Navigation)
# -----------------------------
try:
    st.sidebar.image("profile.jpg", width=200)
except:
    st.sidebar.image(
        "https://images.unsplash.com/photo-1531482615713-2afd69097998",
        width=200
    )

st.sidebar.title("Mr Mthokozisi S. Mathonsi")
st.sidebar.write("🎓 Data Scientist")
st.sidebar.write("🏫 University of Zululand")

section = st.sidebar.radio(
    "Navigation",
    ["About Me", "Skills & Tools", "Projects", "Contact"]
)

# -----------------------------
# About Me
# -----------------------------
if section == "About Me":
    st.title("About Me")

    col1, col2, col3 = st.columns(3)
    col1.metric("Academic Level", "Honours")
    col2.metric("Research Area", "NLP")
    col3.metric("Focus Language", "isiZulu")

    st.markdown("""
    I am a Data Science graduate from the **University of Zululand** with a strong interest
    in **Natural Language Processing (NLP)** and **low-resource African languages**.

    My academic and practical work focuses on applying data science and NLP techniques
    to solve real-world problems in education and language technology.

    At honours level, I conducted research on **Emotion Detection from isiZulu Text using NLP**,
    and I intend to further extend this research at **Masters level**.
    """)

    st.markdown("""
    ### Research Interests
    - Natural Language Processing (NLP)
    - Emotion Detection and Sentiment Analysis
    - Low-resource African Languages
    - Multilingual Systems
    - Educational Technology
    """)

# -----------------------------
# Skills & Tools
# -----------------------------
elif section == "Skills & Tools":
    st.title("Skills & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        st.markdown("""
        - Data Analysis
        - Natural Language Processing (NLP)
        - Machine Learning
        - Text Preprocessing
        - Chatbot Development
        - Research & Academic Writing
        """)

    with col2:
        st.subheader("Tools & Technologies")
        st.markdown("""
        - Python
        - Pandas & NumPy
        - Streamlit
        - Scikit-learn
        - Jupyter Notebook
        - Git & GitHub
        """)

# -----------------------------
# Projects
# -----------------------------
elif section == "Projects":
    st.title("Research & Development Projects")

    with st.expander("🤖 Multilingual Student Support Chatbot"):
        st.markdown("""
        **Description:**  
        A chatbot developed to assist first-year University of Zululand students with
        queries related to university life and adapting to higher education.

        **Key Features:**
        - Responds in the student’s preferred language
        - Improves accessibility and inclusivity
        - Designed specifically for first-year students
        """)

    with st.expander("🪑 Digital Examination Seating Plan System"):
        st.markdown("""
        **Description:**  
        A digital examination seating plan system designed to improve the traditional
        manual seating arrangement used at the University.

        **Impact:**
        - Automated seat allocation
        - Reduced administrative errors
        - Improved efficiency during examinations
        """)

    with st.expander("😊 Emotion Detection from isiZulu Text (Honours Research)"):
        st.markdown("""
        **Description:**  
        An honours research project focused on detecting emotions from isiZulu text using
        Natural Language Processing techniques.

        **Focus Areas:**
        - Text preprocessing for isiZulu
        - Emotion classification
        - Challenges in low-resource languages

        **Future Direction:**
        - Extension of this research at Masters level
        """)

# -----------------------------
# Contact
# -----------------------------
elif section == "Contact":
    st.title("Contact Information")

    st.markdown("""
    **Name:** Mr Mthokozisi Silwayiphi Mathonsi  
    **Institution:** University of Zululand  
    **Field:** Data Science / Natural Language Processing  

    **Email:** your.email@example.com  
    **Phone / WhatsApp:** +27 XX XXX XXXX
    """)

    st.markdown("""
    You may contact me for academic discussions, research collaboration,
    or postgraduate-related inquiries.
    """)
