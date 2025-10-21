import os
from dotenv import load_dotenv

try:
    import streamlit as st
except Exception:
    st = None

# Load local .env for development
load_dotenv()

def get_api_key():
    """Return the Google API key.

    Priority:
    1. Streamlit secrets (st.secrets["GOOGLE_API_KEY"]) when available
    2. Environment variable GOOGLE_API_KEY
    3. Raises RuntimeError if not found
    """
    # Try Streamlit secrets first (when running on Streamlit Cloud)
    if st is not None:
        try:
            key = st.secrets.get("GOOGLE_API_KEY") if isinstance(st.secrets, dict) or hasattr(st.secrets, 'get') else None
            if key:
                return key
        except Exception:
            # If st.secrets isn't available or errors, fall back
            pass

    # Fall back to environment variable
    key = os.getenv("GOOGLE_API_KEY")
    if key:
        return key.strip().strip('"').strip("'")

    raise RuntimeError("Google API key not found. Set GOOGLE_API_KEY in Streamlit secrets or as an environment variable.")
