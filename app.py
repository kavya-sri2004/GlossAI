
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="GlossAI",
    page_icon="🔗",
    layout="wide"
)

# Application title
st.title("🔗 GlossAI")

st.subheader("AI-Powered Business Glossary Mapper")

st.markdown("""
Welcome to **GlossAI**!

GlossAI helps data teams map dataset columns
to standardized business glossary terms using AI.

### What you can do

- Upload a dataset
- Profile dataset columns
- Match columns with business glossary terms
- Review AI-generated mapping suggestions
- Export the final mappings
""")

st.info(
    "Your AI-powered data mapping workspace "
    "is being initialized."
)
