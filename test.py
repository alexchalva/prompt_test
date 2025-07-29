import streamlit as st

st.set_page_config(page_title="Prompt Optimizer", layout="centered")
st.title("✨ Prompt Optimizer (UI only)")

# Persist the output between reruns
if "output_text" not in st.session_state:
    st.session_state.output_text = ""

# 1 – Prompt input
user_prompt = st.text_area("Enter your prompt:")

# 2 – Run button
if st.button("Optimize"):
    # UI‑only demo: simply echo the input prompt.
    # Replace the next line with your real optimization call.
    st.session_state.output_text = user_prompt

# 3 – Output box
st.text_area(
    "Optimized prompt:",
    value=st.session_state.output_text,
    height=200,
    key="output_box",
)
