import streamlit as st

st.set_page_config(page_title="For Nabiha 💖", page_icon="💌")

st.title("Hey Nabiha, you're the only one I got! 💖")

st.markdown("""
This little app is just for you,  
to show how special you are to me.  
Happy Girlfriend's Day, August 1st!  
""")

# Embed the YouTube Shorts video via iframe for reliable playback
st.markdown("""
<iframe width="560" height="315" 
src="https://www.youtube.com/embed/plA3U18_y1w" 
frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Add some interactive love
if st.button("Press me ❤️"):
    st.balloons()
    st.success("You're amazing, Nabiha! 😘")

# Add a personal note
st.write("""
> "In you, I've found my best friend and my forever love."  
> — From me to you, always.
""")
