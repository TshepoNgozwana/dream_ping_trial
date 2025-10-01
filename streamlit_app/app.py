import streamlit as st
import requests
from settings import API_URL
from logging_utils import log_event

st.set_page_config(page_title="Dream Ping", layout="centered")
st.title("Dream Ping — quick idea prototype")

st.markdown("Enter a short build idea and press **Submit**. The app will call the FastAPI `/spec` endpoint and display a JSON stub.")

idea = st.text_input("Build Idea", value="", max_chars=200)

if st.button("Submit"):
    if not idea.strip():
        st.warning("Please enter an idea.")
    else:
        log_event("submit_idea", {"idea": idea})
        try:
            resp = requests.post(f"{API_URL}/spec", json={"idea": idea}, timeout=5)
            log_event("api_call", {"status_code": resp.status_code})
            if resp.ok:
                stub = resp.json()
                st.subheader("Your idea")
                st.write(idea)
                st.subheader("Spec (from API)")
                st.json(stub)
            else:
                st.error(f"API returned {resp.status_code}: {resp.text}")
        except Exception as e:
            log_event("api_call_failed", {"error": str(e)})
            st.error(f"Failed to call API: {e}")
