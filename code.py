import streamlit as st
from PIL import Image

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Blink AI",
    page_icon="🧪",
    layout="wide"
)

# -------------------------------
# Load logo safely (GitHub + Cloud)
# -------------------------------
logo = Image.open("blink_logo.png")

# -------------------------------
# Top navbar logo (Streamlit native)
# -------------------------------
st.logo(
    logo,
    icon_image=logo
)

# -------------------------------
# Sidebar branding
# -------------------------------
with st.sidebar:
    st.image(logo, use_container_width=True)
    st.markdown("### 🔬 Blink AI")
    st.caption("Science • AI • Innovation")

# -------------------------------
# Main content
# -------------------------------
st.title("🔍 Blink AI – Science Fair Project")
st.write(
    """
    **Blink AI** is an intelligent system designed for science education,
    experimentation, and AI-driven analysis.
    """
)

st.info("✅ Logo loaded successfully (GitHub & Streamlit Cloud safe).")

st.divider()

# -------------------------------
# Sample interaction
# -------------------------------
st.subheader("🚀 Demo Section")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}! 👋")
