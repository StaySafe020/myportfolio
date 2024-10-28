import streamlit as st
from base64 import b64encode

def web_portfolio():

    # Page configuration
    st.set_page_config(page_title="Jambong Ralpher's Portfolio", page_icon="")

    # Introduction section with centered title and subtitle
    st.write(
        f"""
        <div class="title" style="text-align: center;">
            <span style="font-size: 32px;">Hello! My name is Jambong Ralpher </span>
        </div>
        <div style="text-align: center;">
            <span style="font-size: 18px;">Software Engineering Student</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load and display image in a circle with border and proper sizing
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

            .social-icon-container {{
                text-align: center;  /* Center icons horizontally */
                margin-top: 20px;  /* Add some space between image and icons */
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

        <div class="social-icon-container">
            """,
        unsafe_allow_html=True
    )

    # Social icons section with improved formatting and links under images (without text)
    social_icons = {
        "linkedin": ["https://www.linkedin.com/in/jambong-ralpher/", "https://cdn-icons-png.flaticon.com/512/174/275874.png"],
        "github": ["https://github.com/jambongRalpher", "https://cdn-icons-png.flaticon.com/128/3291/3291695.png"],
        "gmail": ["jambongralpher@gmail.com", "https://cdn-icons-png.flaticon.com/128/3178/3178158.png"]
    }

    for platform, (link, icon_url) in social_icons.items():
        st.write(
            f"""
            <a href="{link}" target="_blank">
                <img class="social-icon" src="{icon_url}" alt="{platform}">
            </a>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)  # Close the social-icon-container div

if __name__ == "__main__":
    web_portfolio()