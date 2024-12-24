import streamlit as st



st.markdown(
    "<h1 style='text-align: center;'>Gramalytics</h1>",
    unsafe_allow_html=True
)
logo_path =  "logo/logo.png"
col1, col2, col3 = st.columns([1000, 800, 1000]) 


with col2:
    st.image("logo/logo.png", width=600) 
#st.image(logo_path, width=100)  


st.header("Welcome to **Gramalytics**!")
st.write("""
Gramalytics is designed to help Instagram users enhance their visibility and engagement amidst the platforms overwhelming content. By analyzing trending topics and hashtags, Gramalytics provides personalized and actionable recommendations tailored to users' specific niches. 
""")


st.header("Meet the Team!")
st.write("""
Our team consists of highly motivated individuals committed to delivering quality work. Though each member took leadership of different areas of implementation, the process was collaborative. The breakdown goes as follows:
"""
)
team_bios = [
    {
        "name": "Esther Bilenkin",
        "role": "Backend Developer",
        "bio": "Esther Bilenkin is a recent computer science graduate from NYIT, with a concentration in big data management and analysis. Passionate about data science and neural networks, she combines curiosity and a hands-on approach to creating innovative solutions. Drawing from her experience with Gramalytics, a senior project integrating AI to enhance user engagement, Esther is now working on bringing Nexxeaves to market, applying lessons learned to support content creators. Her academic work includes projects like a parental monitoring app and a holiday shopping sentiment analysis tool, reflecting her drive to explore the intersection of technology and impactful problem-solving."
    },
    {
        "name": "Dhara Rameshbhai Chandpara",
        "role": "Frontend Developer",
        "bio": "Dhara Chandpara is a recent computer science graduate from NYIT, pursuing a master’s in data science alongside a bachelor’s degree. With experience in IT support, tutoring, and software development, she has contributed to projects like Gramalytics, integrating AI to enhance user engagement. An active member of ACM and SWE, she is passionate about applying her skills in data science and IT to drive impactful solutions."
    },
    {
        "name": "Farzana Alam",
        "role": "Database Implementation",
        "bio": "Farzana Alam is a recent computer science graduate from NYIT, pursuing a masters in Data Science. Farzana is passionate about uncovering insights through data. With a keen interest in data science, she focuses on transforming raw information into actionable analytics. Her goal is to use data to drive better decision-making and optimize processes. Many of her projects involve preprocessing and analyzing large datasets to make predicitons and summarize key information. She aims to become a data analyst and and further expand her knowledge on machine learning, data analytics, and predictive modeling to tackle real-world problems effectively. "
    }
]

for member in team_bios:
    st.subheader(member["name"])
    st.write(f"**Role**: {member['role']}")
    st.write(member["bio"])
    st.markdown("---")

st.subheader("Project Advisor:")
st.write("""
- **Dr. Wenjia Li**   
- Title: Associate Professor of Computer Science at NYIT
- Email: wli20@nyit.edu
""")

st.subheader("Semester One:")

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.markdown('<u>Semester 1 Final Report:</u> ', unsafe_allow_html=True)
with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1o3B5E4iSRupgqVjo3h-y2eKl7GZYR55e"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.subheader("Semester Two:")
st.markdown('<u>Progress Reports:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("09/18/2024 - 10/02/2024:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1S1JfyUHbasBhtDBnWx9xp_ufsGzuPzWh"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/02/2024 - 10/16/2024:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=19jQSqEIjoGnrsp0c18KY-wHDVdOdhYKt"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/16/2024 - 10/30/2024:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=19X9Uwva1Ig5g-VSEji9lWdhgHY-geTFk"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("10/30/2024 - 11/13/2024:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1YofQLgVsXiq3O6oF_He9DJ957au_Epnh"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("11/13/2024 - 12/04/2024:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1vEXZqtLQ9xkP7zrwtCARFWz_CSHyBoDR"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Semester Two Final Report:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("Final Report:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1u95NNa4xctuRhC2B7eNDvk8bP-406ORm"
    st.markdown(f'[Download Report]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Final Presentation:</u> ', unsafe_allow_html=True)
col1, col2 = st.columns([0.5, 0.5]) 

with col1:
    st.write("Presentation:")

with col2:
    pdf_url = "https://drive.google.com/uc?export=download&id=1IuIHAQ1NyTx5Mm4RCsDwkkX1SbogDoNu"
    st.markdown(f'[Download Presentation]({pdf_url})', unsafe_allow_html=True)

st.markdown('<u>Demo Video:</u> ', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust proportions here
with col2:
    st.video("demo/Senior Design Demo Video.mp4")  # Replace with your video path