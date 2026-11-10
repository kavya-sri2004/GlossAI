
import streamlit as st
import pandas as pd
from mapping_engine import suggest_mappings

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="GlossAI",
    page_icon="🔗",
    layout="wide"
)

# -------------------------------
# Application Header
# -------------------------------
st.title("🔗 GlossAI")
st.subheader("AI-Powered Business Glossary Mapper")

st.write(
    "Upload a dataset to explore its structure and "
    "automatically suggest business glossary mappings."
)

st.divider()

# -------------------------------
# CSV Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        # -------------------------------
        # Dataset Overview
        # -------------------------------
        st.subheader("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Rows", df.shape[0])

        with col2:
            st.metric("Total Columns", df.shape[1])

        with col3:
            st.metric(
                "Total Missing Values",
                int(df.isnull().sum().sum())
            )

        # -------------------------------
        # Dataset Preview
        # -------------------------------
        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        # -------------------------------
        # Column Profiling
        # -------------------------------
        st.subheader("Column Profiling")

        profile = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            profile,
            use_container_width=True
        )

        # -------------------------------
        # Statistical Summary
        # -------------------------------
        st.subheader("Statistical Summary")

        st.dataframe(
            df.describe(include="all").transpose(),
            use_container_width=True
        )

        st.divider()

        # -------------------------------
        # Business Glossary Mapping
        # -------------------------------
                # -------------------------------
        # Business Glossary Mapping
        # -------------------------------
        st.subheader("Business Glossary Mapping")

        # Load the existing glossary from the project folder
        glossary_df = pd.read_csv("glossary.csv")

        required_columns = {
            "term",
            "description",
            "category"
        }

        if required_columns.issubset(glossary_df.columns):

            st.success("Business glossary loaded successfully!")

            if st.button("Generate Mapping Suggestions"):

                with st.spinner(
                    "Analyzing columns and matching glossary terms..."
                ):

                    mapping_results = suggest_mappings(
                        df,
                        glossary_df
                    )

                st.success("Mapping suggestions generated!")

                st.subheader("Suggested Mappings")

                st.dataframe(
                    mapping_results,
                    use_container_width=True
                )

                # -------------------------------
                # Download Mapping Results
                # -------------------------------
                csv_data = mapping_results.to_csv(
                    index=False
                ).encode("utf-8")

                st.download_button(
                    label="Download Mapping Results",
                    data=csv_data,
                    file_name="glossai_mapping_results.csv",
                    mime="text/csv"
                )

        else:

            st.error(
                "Your glossary CSV must contain these columns: "
                "term, description, category"
            )

    except Exception as e:

        st.error(f"An error occurred: {e}")

else:

    st.info(
        "Please upload a CSV file to begin profiling "
        "and business glossary mapping."
    )
