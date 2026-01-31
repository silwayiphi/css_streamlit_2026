import streamlit as st
import pandas as pd

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
st.sidebar.title("Mr Mthokozisi S. Mathonsi")
st.sidebar.write("🎓 Data Scientist")
st.sidebar.write("🏫 University of Zululand")

section = st.sidebar.radio(
    "Navigation",
    ["Overview", "Projects", "Publications", "Contact"]
)

# -----------------------------
# Overview
# -----------------------------
if section == "Overview":
    st.title("Researcher Profile")

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", "3")
    col2.metric("Research Area", "NLP")
    col3.metric("Focus Language", "isiZulu")

    st.markdown("""
    ### Research Interests
    - Natural Language Processing (NLP)
    - Emotion Detection from isiZulu Text
    - Multilingual Chatbots
    - Educational Technology
    - Low-resource African Languages
    """)

    st.markdown("""
    ### Academic Journey
    I completed my Honours research on **Emotion Detection from isiZulu Text using NLP**.
    I am looking forward to extending this research at **Masters level**, with a focus on
    advanced NLP techniques for low-resource languages.
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
        queries related to university life and transitioning into higher education.

        **Key Features:**
        - Responds in the student’s preferred language
        - Improves accessibility and inclusivity
        - Designed for new students entering university
        """)

    with st.expander("🪑 Digital Examination Seating Plan System"):
        st.markdown("""
        **Description:**  
        A digital examination seating plan system developed to improve the traditional
        manual seating arrangement used at the University of Zululand.

        **Improvements:**
        - Automated seat allocation
        - Reduced human error
        - Improved efficiency and organization
        """)

    with st.expander("😊 Emotion Detection from isiZulu Text (Honours Research)"):
        st.markdown("""
        **Description:**  
        An honours research project focused on detecting emotions from isiZulu text
        using Natural Language Processing.

        **Research Focus:**
        - Text preprocessing for isiZulu
        - Emotion classification
        - Low-resource language challenges
        """)

# -----------------------------
# Publications
# -----------------------------
elif section == "Publications":
    st.title("Publications")

    uploaded_file = st.file_uploader("Upload Publications CSV", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)

        keyword = st.text_input("Search publications by keyword")

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
            st.subheader("Publication Trend")
            year_counts = publications["Year"].value_counts().sort_index()
            st.line_chart(year_counts)
    else:
        st.info("Upload a CSV file to display publications.")

# -----------------------------
# Contact
# -----------------------------
elif section == "Contact":
    st.title("Contact Information")

    st.markdown("""
    **Name:** Mr Mthokozisi Silwayiphi Mathonsi  
    **Institution:** University of Zululand  
    **Field:** Data Science / NLP  

    **Email:** mthokozisi.mathonsi@example.com  
    **WhatsApp:** +27 XX XXX XXXX
    """)

    st.markdown("""
    You may contact me regarding academic collaboration, research discussions,
    or postgraduate studies.
    """)
