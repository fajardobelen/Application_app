import streamlit as st
st.title(" ✨Welcome to my Portfolio")

st.set_page_config(page_title="Home", page_icon="🚀", layout="wide")

st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #38bdf8 0%, transparent 25%),
                radial-gradient(circle at 80% 30%, #f472b6 0%, transparent 25%),
                linear-gradient(135deg, #020617, #020617, #020617);
    color: white;
}

/* Titles */
h1 {
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #38bdf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2, h3 {
    color: #e0f2fe;
}

/* Glow text */
.glow {
    color: #e0f2fe;
    text-shadow: 0 0 5px #38bdf8,
                 0 0 10px #38bdf8,
                 0 0 15px #f472b6;
}

/* Neon buttons */
.stButton>button {
    background: transparent;
    color: #38bdf8;
    border: 1px solid #38bdf8;
    border-radius: 10px;
    padding: 10px 20px;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #38bdf8;
    color: black;
    box-shadow: 0 0 15px #38bdf8, 0 0 25px #f472b6;
}

/* Glass cards */
.card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(56,189,248,0.3);
    box-shadow: 0 0 20px rgba(244,114,182,0.2);
    margin-bottom: 20px;
}

/* Image glow */
.img-glow img {
    border-radius: 50%;
    box-shadow: 0 0 25px #38bdf8, 0 0 50px #f472b6;
}

</style>
""", unsafe_allow_html=True)

# ===== HERO SECTION =====
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Hi, I'm Belen Fajardo")
    st.title("Aspiring Developer & Designer")
    st.markdown('<p class="glow">Developer | Designer</p>', unsafe_allow_html=True)
    st.info("Welcome to my portfolio! Explore my work and skills.")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("📁 View Projects"):
            st.switch_page("pages/4_📂_Projects.py")
    with c2:
        if st.button("🧠 View Skills"):
            st.switch_page("pages/3_🛠️_Skills.py")

with col2:
    st.markdown('<div class="img-glow">', unsafe_allow_html=True)
    st.image("", width=250)
    st.markdown('</div>', unsafe_allow_html=True)
