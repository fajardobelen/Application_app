import streamlit as st

st.set_page_config(page_title="Skills", page_icon="🛠️", layout="wide")

# 🌌 Futuristic Background Styling (Black + Light Blue + Light Pink)
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #38bdf8 0%, transparent 25%),
                radial-gradient(circle at 80% 30%, #f472b6 0%, transparent 25%),
                linear-gradient(135deg, #020617, #020617, #020617);
    color: white;
}
/* Floating neon orbs */
.bg-orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.4;
    z-index: -1;
    animation: float 18s infinite ease-in-out;
}

@keyframes float {
    0% { transform: translate(0, 0); }
    50% { transform: translate(40px, -60px); }
    100% { transform: translate(0, 0); }
}

/* Orb colors */
.orb1 {
    width: 500px;
    height: 500px;
    background: #6dd5ff; /* light blue */
    top: -150px;
    left: -150px;
}

.orb2 {
    width: 400px;
    height: 400px;
    background: #ff9bd2; /* light pink */
    bottom: -120px;
    right: -120px;
}

.orb3 {
    width: 300px;
    height: 300px;
    background: #6dd5ff;
    top: 40%;
    right: -80px;
}

/* Section Title */
.section-title {
    font-size: 2.5rem;
    font-weight: bold;
    background: linear-gradient(90deg, #6dd5ff, #ff9bd2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 2rem;
}

/* Skill Cards */
.skill-card {
    background: rgba(10, 15, 30, 0.7);
    border: 1px solid rgba(109, 213, 255, 0.3);
    border-radius: 20px;
    padding: 20px;
    margin: 10px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 25px rgba(109, 213, 255, 0.15),
                0 0 35px rgba(255, 155, 210, 0.1);
    transition: 0.3s ease;
}

.skill-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 35px rgba(109, 213, 255, 0.3),
                0 0 50px rgba(255, 155, 210, 0.25);
}

/* Progress bar glow */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #6dd5ff, #ff9bd2);
}

</style>
""", unsafe_allow_html=True)

# 🌟 Add animated orbs
st.markdown('<div class="bg-orb orb1"></div>', unsafe_allow_html=True)
st.markdown('<div class="bg-orb orb2"></div>', unsafe_allow_html=True)
st.markdown('<div class="bg-orb orb3"></div>', unsafe_allow_html=True)

# 🛠️ Title
st.markdown('<div class="section-title">🛠️ My Skills</div>', unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns(3)

# 💻 Programming
with col1:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.subheader("💻 Programming")
    st.progress(80)
    st.write("Python")
    st.progress(80)
    st.markdown('</div>', unsafe_allow_html=True)

# 🎨 Design
with col2:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.subheader("🎨 Design")
    st.progress(85)
    st.write("Canva / UI Design")
    st.markdown('</div>', unsafe_allow_html=True)

# 🧰 Tools
with col3:
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.subheader("🧰 Tools")
    st.write("- GitHub")
    st.write("- VS Code")
    st.write("- Streamlit")
    st.markdown('</div>', unsafe_allow_html=True)
