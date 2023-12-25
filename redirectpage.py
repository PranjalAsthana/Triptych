import streamlit as st
import webbrowser

# color1 = '#2193b0'
# color2 = '#6dd5ed'
# color3 = '#fa6984'
# color4 = '#fa6984'
# inverse_color3 = "#{:06x}".format(0xFFFFFF ^ int(color3[1:], 16))
st.title("Triptych:clapper::books::musical_note:")
# st.markdown(f"<h1 style='text-align: center; color: linear-gradient(to right,{color1} 46%, {color2} 54%); '>Cosmosia</h1>", unsafe_allow_html=True)


# st.write(
#     f"""
#     <div style="text-align: center; background-image: linear-gradient(to right, {color1}, {color2}); -webkit-background-clip: text; color: transparent;">
#         <h1>Cosmosia</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

#st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">WHat is the outpitu</p>', unsafe_allow_html=True)
# st.markdown("""
# <style>
# .big-font {
#     font-size:50px !important;
# }
# </style>
# """, unsafe_allow_html=True)
    
# st.markdown('<p class="big-font">Cosmosia</p>', unsafe_allow_html=True)


    
st.write('Tailored Suggestions, Crafted from Your Preferences')

st.write("#")
st.write("#")
left_co, cent_co,last_co = st.columns([0.33,0.33,0.33])
with left_co:
    

        if st.button("PickFlicks : Unveil Cinematic Choices On Demand"):
            webbrowser.open('https://pickflicks.streamlit.app/')

    ##st.write("#")
    #st.write("#")
with cent_co:
    if st.button("PlotPilot : Navigate Stories, Delve into Genres"):
        webbrowser.open('https://plotpilot.streamlit.app/')

    #st.write("#")
    #st.write("#")
with last_co:
    if st.button("RythMix : Find Songs, Explore Artists, Discover Your Groove"):
        webbrowser.open('https://rythmix.streamlit.app/')


st.sidebar.markdown(":orange[App made by] :gray[-] :orange[[Pranjal Asthana](https://github.com/PranjalAsthana)]")
st.sidebar.write("")
st.sidebar.write("***Triptych***, a dynamic and user-centric website, redefines the way you discover and engage with diverse recommendations. Serving as a personalized compass in the vast landscape of content, Triptych guides users through meticulously curated suggestions for movies, books, and songs. Seamlessly blending intuitive design with machine learning algorithms, Triptych navigates your preferences, offering tailored recommendations on your fingertips. With Triptych, the exploration of entertainment becomes a journey of discovery, unveiling a trinity of choices that perfectly align with your individual preferences.")