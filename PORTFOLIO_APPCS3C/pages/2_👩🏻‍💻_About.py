import streamlit as st

# --- Custom CSS ---
st.markdown("""
<style>

/* Background like Home (black + glow effect) */
.stApp {
    background: radial-gradient(circle at 20% 20%, #38bdf8 0%, transparent 25%),
                radial-gradient(circle at 80% 30%, #f472b6 0%, transparent 25%),
                linear-gradient(135deg, #020617, #020617, #020617);
    color: white;
}

/* Text styling */
h1 {
    color: #66ccff;
}

h2, h3 {
    color: #ff99cc;
}

p {
    color: #eaeaea;
}

/* Optional glass container */
.block-container {
    background: rgba(0, 0, 0, 0.4);
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

st.title("👩🏻‍🎓 About")
st.write("""
I am a passionate developer who enjoys creating systems and applications that are user-friendly design.
I love creating something beautiful and modern designs.
""")
st.subheader(" Education")
st.write("- BS Computer Science")
st.subheader(" Goals")
st.write("- Become a Full Stack Developer")
st.write("- Build impactful designs")