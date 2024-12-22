import streamlit as st
from base64 import b64encode

def web_portfolio():

    # Page configuration
    st.set_page_config(page_title="Jambong Ralpher's Portfolio", page_icon="")

    # Introduction section with centered title and subtitle
    st.write(
        f"""
        <div class="title" style="text-align: center;">
            <span style="font-size: 32px;">Hello! My name is Jambong Ralpher  </span>
        </div>
        <div style="text-align: center;">
            <span style="font-size: 18px;">Software Engineering Student</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load and display image in a circle with proper sizing
    with open("image.jpg", "rb") as image_file:
        encoded_image = b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
            .profile-image {{
                border-radius: 50%;
                border: 2px solid #ddd;
                width: 200px;  /* Adjust width as needed */
                height: 200px; /* Adjust height as needed */
                margin: 0 auto;  /* Center horizontally */
                display: block;
            }}

            .social-icons {{
                display: flex;
                justify-content: center;  /* Center icons horizontally */
                margin-top: 20px;  /* Add space between image and icons */
            }}

            .social-icon {{
                width: 25px;
                height: 25px;
                margin: 0 5px;  /* Adjust spacing between icons */
            }}
        </style>

        <div class="profile-image-container">
            <img class="profile-image" src="data:image/jpeg;base64,{encoded_image}" alt="Jambong Ralpher">
        </div>

        <div class="social-icons">
        """,
        unsafe_allow_html=True
    )

    # Social icons 
    social_icons = {
        "linkedin": ["https://www.linkedin.com/in/jambong-ralpher/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "github": ["https://github.com/Jambong-Ralpher", "https://cdn-icons-png.flaticon.com/128/733/733553.png"],
        "twitter(x)": ["https://x.com/JRalpher59117", "https://cdn-icons-png.flaticon.com/128/5968/5968958.png"]
    }

    social_icons = [
    f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons
]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

      # About Me 
    st.subheader("About Me")

    st.markdown("""
    - 🧑‍💻 I am a third year **Computer Science student** at RHIBMS Buea, [RHIBMS](https://www.rhibms.org)
    where I am currently studying  software engineerng.
    - 🚀 I am also currently studying cloud computing on [Azure and IBM].
    - ❤️ I am passionate about *cloud computing, distributed systems, python, Software Engineering, 
    Computer Vision, Data structure and algorithms, Automation*, and more!
    - 🏂 In my free time, I enjoy reading.
    - 🏠 Based in cameroon.
    """)

    st.write("##")



    ## Download CV section
    if st.button("Download CV"):
            with open("profile.pdf", "rb") as file:
                st.download_button("Download CV", file.read(), file_name="profile.pdf"),

    st.markdown(
    """
    <div style="margin-top: 20px; text-align: right; color: yellow;">
        Have a wonderful day ⭐
    </div>
    """,
    unsafe_allow_html=True
)
    

if __name__ == "__main__":
    web_portfolio()
