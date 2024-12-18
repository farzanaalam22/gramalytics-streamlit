import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #fffdd0;
        font-family: 'Arial';
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    "<h1 style='text-align: center;'>Gramalytics</h1>",
    unsafe_allow_html=True
)
logo_path =  "logo/logo.png"
col1, col2, col3 = st.columns([1000, 800, 1000])  # Adjust ratio as needed

# Place the logo in the middle column (col2)
with col2:
    st.image("logo/logo.png", width=600)  # Adjust width as needed
#st.image(logo_path, width=100)  # You can adjust the width based on your preference


st.header("Welcome to **Gramalytics**!")
st.write("""
Gramalytics is designed to help Instagram users enhance their visibility and engagement amidst the platforms overwhelming content. By analyzing trending topics and hashtags, Gramalytics provides personalized and actionable recommendations tailored to users' specific niches. 
""")

st.subheader("Meet the Team:")
st.write("""
Our team consists of highly motivated individuals committed to delivering quality work. Though each memeber took leadership of different area of implementation, the process was collaborative. The breakdown goes as follows:
- **Esther Bilenkin**: Backend Developer
- **Dhara Rameshbhai Chandpara**: Frontend Developer
- **Farzana Alam**: Database Implementation
""")

st.subheader("Semester One:")

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.markdown('<u>Semester 1 Final Report:</u> ', unsafe_allow_html=True)
with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1o3B5E4iSRupgqVjo3h-y2eKl7GZYR55e"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.subheader("Semester Two:")
st.markdown('<u>Progress Reports:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("09/18/2024 - 10/02/2024:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1S1JfyUHbasBhtDBnWx9xp_ufsGzuPzWh"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/02/2024 - 10/16/2024:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=19jQSqEIjoGnrsp0c18KY-wHDVdOdhYKt"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/16/2024 - 10/30/2024:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=19X9Uwva1Ig5g-VSEji9lWdhgHY-geTFk"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/30/2024 - 11/13/2024:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1YofQLgVsXiq3O6oF_He9DJ957au_Epnh"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("11/13/2024 - 12/04/2024:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1vEXZqtLQ9xkP7zrwtCARFWz_CSHyBoDR"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Semester Two Final Report:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("Final Report:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1u95NNa4xctuRhC2B7eNDvk8bP-406ORm"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Final Presentation:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("Presentation:")

with col2:
    # Link to the Google Drive PDF (converted to direct download link)
    pdf_url = "https://drive.google.com/uc?export=download&id=1IuIHAQ1NyTx5Mm4RCsDwkkX1SbogDoNu"
    st.markdown(f'[Download Presentation]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Demo Video:</u> ', unsafe_allow_html=True)
#st.video("demo/Senior Design Demo Video.mp4")
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust proportions here
with col2:
    st.video("demo/Senior Design Demo Video.mp4")  # Replace with your video path