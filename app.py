import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Researcher Profile | Mthokozisi Mathonsi",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "useMe.jpg",
    width=200
)

st.sidebar.title("Mr Mthokozisi S. Mathonsi")
st.sidebar.write("🎓 Data Scientist")
st.sidebar.write("🏫 University of Zululand")

section = st.sidebar.radio(
    "Navigation",
    ["Overview", "Projects", "Publications", "STEM Data", "Contact"]
)

# -----------------------------
# Overview
# -----------------------------
if section == "Overview":
    st.title("Researcher Profile")

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", "3")
    col2.metric("Research Focus", "NLP")
    col3.metric("Languages", "isiZulu + English")

    st.markdown("""
    ### Research Interests
    - Natural Language Processing (NLP)
    - Emotion Detection from isiZulu Text
    - Multilingual Chatbots
    - Educational Technology
    - Low-Resource Language AI
    """)

    st.markdown("""
    ### Masters Research Vision
    Building on my honours research in **Emotion Detection from isiZulu Text**, 
    I aim to extend this work at Masters level by exploring advanced NLP and deep learning
    techniques for African languages.
    """)

# -----------------------------
# Projects
# -----------------------------
elif section == "Projects":
    st.title("Research & Development Projects")

    with st.expander("🤖 Multilingual Student Support Chatbot"):
        st.markdown("""
        **Description:**  
        A chatbot developed to assist UNIZULU first-year students with queries related to
        university life and academic processes.

        **Key Features:**
        - Responds in the student’s preferred language
        - Improves accessibility and inclusivity
        - Designed for new students entering university

        **Technologies:**
        - Python
        - NLP
        - Chatbot frameworks
        """)

    with st.expander("🪑 Digital Examination Seating Plan System"):
        st.markdown("""
        **Description:**  
        A digital examination seating plan system designed to improve the traditional
        manual process used at the University of Zululand.

        **Benefits:**
        - Faster seat allocation
        - Reduced errors
        - Improved organization and fairness

        **Technologies:**
        - Python
        - Data handling
        - Logical allocation algorithms
        """)

    with st.expander("😊 Emotion Detection from isiZulu Text (Honours Research)"):
        st.markdown("""
        **Description:**  
        Honours-level research focused on detecting emotions from isiZulu text using
        Natural Language Processing.

        **Focus Areas:**
        - Low-resource African languages
        - Text preprocessing
        - Emotion classification

        **Future Work:**
        - Extend research at Masters level
        - Explore deep learning approaches
        """)

# -----------------------------
# Publications
# -----------------------------
elif section == "Publications":
    st.title("Publications")

    uploaded_file = st.file_uploader("Upload Publications CSV", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)

        keyword = st.text_input("Search publications")

        filtered = publications
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]

        st.dataframe(filtered, use_container_width=True)

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.line_chart(year_counts)
    else:
        st.info("Upload a CSV file to view publications.")

# -----------------------------
# STEM Data
# -----------------------------
elif section == "STEM Data":
    st.title("STEM Data Explorer")

    physics_data = pd.DataFrame({
        "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
        "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    })

    astronomy_data = pd.DataFrame({
        "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
        "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    })

    weather_data = pd.DataFrame({
        "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
        "Temperature (°C)": [25, 10, -3, 15, 30],
        "Humidity (%)": [65, 70, 55, 80, 50],
    })

    tab1, tab2, tab3 = st.tabs(["Physics", "Astronomy", "Weather"])

    with tab1:
        st.dataframe(physics_data)
        st.bar_chart(physics_data.set_index("Experiment"))

    with tab2:
        st.dataframe(astronomy_data)
        st.bar_chart(astronomy_data.set_index("Celestial Object"))

    with tab3:
        st.dataframe(weather_data)
        st.scatter_chart(
            weather_data,
            x="Temperature (°C)",
            y="Humidity (%)"
        )

# -----------------------------
# Contact
# -----------------------------
elif section == "Contact":
    st.title("Contact Information")

    st.write("📧 Email: mthokozisim@example.com")
    st.write("🏫 Institution: University of Zululand")

    with st.form("contact_form"):
        sender_name = st.text_input("Your Name")
        sender_email = st.text_input("Your Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("Thank you! Your message has been sent.")
