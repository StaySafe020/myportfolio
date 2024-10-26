import streamlit as st
from base64 import b64encode

#page configs


def web_portfolio():
    st.set_page_config(page_title = "Jambong Ralpher's portfolio", page_icon="🌟")
    #page title
   # import streamlit as st
st.write(
    f"""
    <div class="title" style="text-align: center;">
        <span style="font-size: 32px;">Hello! My name is Jambong Ralpher👋 </span>
    </div>
    """,
    unsafe_allow_html=True)
st.markdown('<style>div.block=container{padding-top:2rem;}</style>',unsafe_allow_html=True)

#get image
with open("image.jpg", "rb") as img_file:
      img = "data:image/jpeg;base64," + b64encode(img_file.read()).decode()
      
      #reading profile
with open("profile.pdf", "rb") as pdf_file:
  
  #set the profile
  
  st.write (f"""
            <div style ="display: flex; justify-content: center;">
            <div class="box">
            <img src="{img}" alt="jambong ralpher" width: 300px; height: 200px;>
             </div> 
              </div> 
              """,
              unsafe_allow_html=True)
  st.markdown("""
<div style="text-align: center;">
    <span style="font-size: 32px;">Hello! My name is Jambong Ralpher</span>
    <br>
    <span style="font-size: 18px;">software engineering student</span>
</div>
""", unsafe_allow_html=True)
 
  
  #social icons
  social_icons = {
       "linkedin": ["https://www.linkedin.com/in/jambong-ralpher/", "https://cdn-icons-png.flaticon.com/512/174/275874.png"],
       "github": ["https://github.com/jambongRalpher", "https://cdn-icons-png.flaticon.com/128/3291/3291695.png"],
       "gmail": ["jambongralpher@gmail.com","https://cdn-icons-png.flaticon.com/128/3178/3178158.png" ]
  }

social_icons_html = [
    f"<a href={social_icons[platform][0]}"target="_blank" style ="margin-right: 10px;">"
    f"<img class='social-icon' src ='{social_icons[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons
]

if __name__ ==  "__main__":
        web_portfolio()