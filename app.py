import streamlit as st
from base64 import b64encode

def web_portfolio():
    # Page configuration
    st.set_page_config(page_title="Jambong Ralpher Portfolio", page_icon="🚀")

    # Introduction section with centered title and subtitle
    st.write(
        f"""
        <div class="title" style="text-align: center;">
            <span style="font-size: 32px;">Hello! I am Jambong Ralpher</span>
        </div>
        <div style="text-align: center;">
            <span style="font-size: 18px;">Software Engineering Student</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load and display image in a circle (use a generic avatar for anonymity)
    try:
        with open("image.jpg", "rb") as image_file:  
            encoded_image = b64encode(image_file.read()).decode()
    except FileNotFoundError:
        encoded_image = ""  # Fallback: no image if file missing
        st.warning("Profile image not found. Please add avatar.jpg.")

    st.markdown(
        f"""
        <style>
            .profile-image {{
                border-radius: 50%;
                border: 2px solid #ddd;
                width: 200px;
                height: 200px;
                margin: 0 auto;
                display: block;
            }}
            .social-icons {{
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }}
            .social-icon {{
                width: 25px;
                height: 25px;
                margin: 0 5px;
            }}
        </style>
        <div class="profile-image-container">
            <img class="profile-image" src="data:image/jpeg;base64,{encoded_image}" alt="TechCoder237">
        </div>
        <div class="social-icons">
        """,
        unsafe_allow_html=True
    )

    # Social icons (placeholders, update with your profiles)
    social_icons = {
        "LinkedIn": ["https://www.linkedin.com/in/JRalpher", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub": ["https://github.com/Staysafe020", "https://cdn-icons-png.flaticon.com/128/733/733553.png"],
        "X": ["https://x.com/Staysafe020", "https://cdn-icons-png.flaticon.com/128/5968/5968958.png"]
    }

    social_html = [
        f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{social_icons[platform][1]}' alt='{platform}'"
        f" style='width: 25px; height: 25px;'></a>"
        for platform in social_icons
    ]
    st.write(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_html)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("##")

    # About Me (Realistic, Simple, No Books)
    st.subheader("About Me")
    st.markdown("""
    - 🧑‍💻 I’m a final-year **Software Engineering student** at RHIBMS in Cameroon, learning to build cool tech projects.
    - 🚀 I’m working on:
      - **Python**: Practicing data structures and algorithms on LeetCode and HackerRank (solving problems like arrays and strings).
      - **Rust**: Learning basics like structs and ownership through online exercises.
      - **JavaScript**: Building simple web apps and learning how websites work.
      - **Go**: Exploring server-side coding and concurrency.
      - **Ethical Hacking**: Studying network security with online platforms like TryHackMe.
      - **AWS**: Training for the AWS Cloud Practitioner certification to learn cloud basics.
    - ❤️ I love coding, automation, and creating secure systems.
    - 🏠 I’m based in Cameroon.
    """)

    st.write("##")

    # Projects
    st.subheader("Projects")
    st.markdown("""
    - **Pyrustpipe** :
      -PyRustPipe is a library for processing semi-structured data (e.g., JSON, YAML, CSV) with validation and transformation pipelines. 
                It combines Python's ease of use for defining rules with Rust's speed for executing them.
    - **Portfolio Website**:
      - Built this website with Streamlit to share my coding journey.
    """)

    st.write("##")

    # Download CV
    try:
        with open("profile.pdf", "rb") as file:
            st.download_button("Download CV", file.read(), file_name="profile.pdf", key="download_cv")
    except FileNotFoundError:
        st.warning("CV file not found. Please create profile.pdf.")

    st.markdown(
        """
        <div style="margin-top: 20px; text-align: right; color: #00CED1;">
            Excited to build the future! ⭐
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    web_portfolio()