import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")

# 🌌 Futuristic Theme (same as Skills & Projects)
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #38bdf8 0%, transparent 25%),
                radial-gradient(circle at 80% 30%, #f472b6 0%, transparent 25%),
                linear-gradient(135deg, #020617, #020617, #020617);
    color: white;
}
            
/* Floating orbs */
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

.orb1 {
    width: 500px;
    height: 500px;
    background: #6dd5ff;
    top: -150px;
    left: -150px;
}

.orb2 {
    width: 400px;
    height: 400px;
    background: #ff9bd2;
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

/* Title */
.section-title {
    font-size: 2.5rem;
    font-weight: bold;
    background: linear-gradient(90deg, #6dd5ff, #ff9bd2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 2rem;
}

/* Contact Card */
.contact-card {
    background: rgba(10, 15, 30, 0.7);
    border: 1px solid rgba(109, 213, 255, 0.3);
    border-radius: 20px;
    padding: 25px;
    max-width: 600px;
    margin: auto;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 25px rgba(109, 213, 255, 0.15),
                0 0 35px rgba(255, 155, 210, 0.1);
}

/* Button glow */
.stButton > button {
    background: linear-gradient(90deg, #6dd5ff, #ff9bd2);
    color: black;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px #6dd5ff, 0 0 30px #ff9bd2;
}

/* Inputs */
input, textarea {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# 🌟 Orbs
st.markdown('<div class="bg-orb orb1"></div>', unsafe_allow_html=True)
st.markdown('<div class="bg-orb orb2"></div>', unsafe_allow_html=True)
st.markdown('<div class="bg-orb orb3"></div>', unsafe_allow_html=True)

# 📬 Title
st.markdown('<div class="section-title">📬 Contact Me</div>', unsafe_allow_html=True)

# 📩 Contact Form
st.markdown('<div class="contact-card">', unsafe_allow_html=True)

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("✅ Message sent successfully!")
    else:
        st.error("⚠️ Please fill all fields.")

st.markdown('</div>', unsafe_allow_html=True)

# 🔗 Social Links
st.markdown("### Social Links")
st.write("- Github:https://github.com/fajardobelen")
st.write("- Facebook:https://www.facebook.com/belen.fajardo.543")
