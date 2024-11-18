import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import base64

# Page Configuration
st.set_page_config(
    page_title="Shashank Garimella - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        font-size: 3rem !important;
        font-weight: bold !important;
        color: #0066cc !important;
    }
    .stSubheader {
        font-size: 1.5rem !important;
        color: #666666 !important;
    }
    .project-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
    }
    .skill-tag {
        display: inline-block;
        padding: 0.3rem 0.6rem;
        margin: 0.2rem;
        border-radius: 0.3rem;
        background-color: #e9ecef;
        font-size: 0.9rem;
    }
    .social-links {
        margin-top: 1rem;
    }
    .social-links a {
        color: #0066cc;
        text-decoration: none;
        margin-right: 1rem;
    }
    .social-links a:hover {
        text-decoration: underline;
    }
    .project-links {
        margin-top: 0.5rem;
        padding: 0.5rem 0;
    }
    .project-links a {
        background-color: #0066cc;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 0.3rem;
        text-decoration: none;
        font-size: 0.9rem;
        margin-right: 0.5rem;
    }
    .project-links a:hover {
        background-color: #0052a3;
    }
    </style>
    """, unsafe_allow_html=True)

# Social Media Links
LINKEDIN_URL = "https://www.linkedin.com/in/shashank-garimella-27a4b6193/"  
GITHUB_URL = "https://github.com/shashank10081999"  

# Project Links
PROJECT_LINKS = {
    "pneumonia_detection": "https://github.com/shashank10081999/pneumonia-detection",  
    "sensor_fault": "https://github.com/shashank10081999/sensor-fault-detection",      
    "number_plate": "https://github.com/shashank10081999/number-plate-recognition",    
    "language_identification": "https://github.com/shashank10081999/language-identification", 
    "face_authenticator": "https://github.com/shashank10081999/Face-matching-and-Face-Recognition"    
}


def show_experience():
    st.title("Professional Experience")
    
    # Ezynest LLC
    with st.container():
        st.markdown("### Python Developer (Intern) - Ezynest LLC")
        st.markdown("*Aug 2024 - Present | Dallas, TX*")
        st.markdown("""
        - Developed Python scripts for Azure DevOps automation, reducing manual setup time by 30%
        - Improved cross-team collaboration efficiency by 25% through dynamic permission solutions
        """)
    
    # Tiger Analytics
    with st.container():
        st.markdown("### Machine Learning Engineer - Tiger Analytics")
        st.markdown("*May 2022 - Dec 2022 | Hyderabad, India*")
        st.markdown("""
        - Engineered CI/CD pipeline using Databricks and Azure DevOps
        - Reduced deployment time by 40% and increased model accuracy by 10%
        """)
    
    # TCS
    with st.container():
        st.markdown("### Assistant System Engineer - Tata Consultancy Services")
        st.markdown("*Oct 2020 - Apr 2022 | Hyderabad, India*")
        st.markdown("""
        - Managed ETL processes with 99.9% data accuracy for 15 million records monthly
        - Reduced data errors by 20% through cross-functional collaboration
        """)

def show_skills():
    st.title("Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming & Tools")
        skills_data = {
            "Python": 90,
            "TensorFlow/PyTorch": 85,
            "SQL": 80,
            "Azure": 75,
            "Docker": 70
        }
        
        for skill, level in skills_data.items():
            st.progress(level/100)
            st.write(f"{skill}: {level}%")
    
    with col2:
        st.markdown("### Areas of Expertise")
        expertise = [
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Data Analysis",
            "MLOps",
            "ETL Pipeline Development"
        ]
        for item in expertise:
            st.markdown(f"- {item}")


def show_education():
    st.title("Education")
    
    st.markdown("### University of North Texas")
    st.markdown("*Masters in Data Science | Jan 2023 - Dec 2024*")
    st.markdown("- CGPA: 3.8")
    
    st.markdown("### Gandhi Institute of Technology and Management")
    st.markdown("*Bachelor of Technology in Electronics and Communication Engineering | May 2016 - May 2020*")
    st.markdown("- CGPA: 3.61")
    
    st.markdown("### Certifications")
    st.markdown("""
    - Professional Certification on Data Science by IBM
    - Certification on Python by University of Michigan
    """)

# Previous imports and configurations remain the same...

def show_about():
    st.title("Shanmukha Sai Shashank Garimella")
    st.subheader("Data Scientist | Machine Learning Engineer | Python Developer")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        👋 Hello! I'm a passionate Data Scientist and Machine Learning Engineer with expertise in:
        
        - 🤖 Machine Learning & Deep Learning
        - 📊 Data Analysis & Visualization
        - 💻 Full-Stack Development
        - 🔧 MLOps & Model Deployment
        
        Currently pursuing my Masters in Data Science at University of North Texas, I bring hands-on experience from roles at Ezynest LLC, Tiger Analytics, and Tata Consultancy Services.
        """)
        
        # Social Links
        st.markdown("""
        <div class="social-links">
            <a href="{}" target="_blank">📱 LinkedIn</a>
            <a href="{}" target="_blank">💻 GitHub</a>
        </div>
        """.format(LINKEDIN_URL, GITHUB_URL), unsafe_allow_html=True)
    
    with col2:
        # Load and display the profile image
        with open("profile-pic.jpeg", "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode("utf-8")
        
        # Display the image using HTML with improved styles
        st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/jpeg;base64,{base64_image}" alt="Profile Picture" 
                 style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover; border: 2px solid #ddd;">
        </div>
        """, unsafe_allow_html=True)


def show_projects():
    st.title("Featured Projects")
    
    # Pneumonia Detection Project
    with st.container():
        st.markdown("### Pneumonia Detection and Explainability")
        st.markdown("""
        **Technologies:** Python, Vision Transformers, k-NN, LLM, PyTorch
        
        - Developed ViT model achieving 90% accuracy in pneumonia classification
        - Implemented k-NN for similar case retrieval
        - Integrated LLM for human-readable diagnosis explanations
        """)
        st.markdown(f"""
        <div class="project-links">
            <a href="{PROJECT_LINKS['pneumonia_detection']}" target="_blank">📂 View Project</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Severity Sensor Project
    with st.container():
        st.markdown("### Severity Sensor Fault Detection")
        st.markdown("""
        **Technologies:** Python, AWS, Flask, Git, Docker
        
        - Built binary classification model with 90% accuracy for sensor fault detection
        - Implemented Docker containerization reducing deployment time by 40%
        """)
        st.markdown(f"""
        <div class="project-links">
            <a href="{PROJECT_LINKS['sensor_fault']}" target="_blank">📂 View Project</a>
        </div>
        """, unsafe_allow_html=True)
    
    # ANPR Project
    with st.container():
        st.markdown("### Automatic Number Plate Recognition")
        st.markdown("""
        **Technologies:** Python, Deep Learning
        
        - Achieved 95% precision and 92% recall in license plate detection
        - Developed efficient data preprocessing pipeline using XML annotations
        """)
        st.markdown(f"""
        <div class="project-links">
            <a href="{PROJECT_LINKS['number_plate']}" target="_blank">📂 View Project</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Language Identification Project
    with st.container():
        st.markdown("### Language Identification")
        st.markdown("""
        **Technologies:** Python, Deep Learning, AWS
        
        - Developed language identification system with 95% accuracy
        - Utilized CNNs for pattern extraction from audio spectrograms
        """)
        st.markdown(f"""
        <div class="project-links">
            <a href="{PROJECT_LINKS['language_identification']}" target="_blank">📂 View Project</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Face Authenticator Project
    with st.container():
        st.markdown("### Face Authenticator")
        st.markdown("""
        **Technologies:** Python, MTCNN, FastAPI
        
        - Implemented two-stage authentication system
        - Enhanced facial detection accuracy by 30%
        """)
        st.markdown(f"""
        <div class="project-links">
            <a href="{PROJECT_LINKS['face_authenticator']}" target="_blank">📂 View Project</a>
        </div>
        """, unsafe_allow_html=True)

def show_contact():
    st.title("Contact Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        📍 Dallas, Texas  
        📧 shanmukhasaishashankgarimella@gmail.com  
        📱 +1 945-267-5622
        """)
    
    with col2:
        st.markdown("### Connect with me:")
        st.markdown(f"""
        <div class="social-links">
            <a href="{LINKEDIN_URL}" target="_blank">💼 LinkedIn Profile</a>
            <a href="{GITHUB_URL}" target="_blank">💻 GitHub Profile</a>
        </div>
        """, unsafe_allow_html=True)

# Include other functions (show_experience, show_skills, show_education) as they were in the previous version


def main():
    # Sidebar
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", ["About Me", "Experience", "Skills", "Projects", "Education", "Contact"])

    # Main Content
    if page == "About Me":
        show_about()
    elif page == "Experience":
        show_experience()
    elif page == "Skills":
        show_skills()
    elif page == "Projects":
        show_projects()
    elif page == "Education":
        show_education()
    elif page == "Contact":
        show_contact()

if __name__ == "__main__":
    main()