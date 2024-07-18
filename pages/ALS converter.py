import streamlit as st
import pandas as pd
import openpyxl

def main():
    st.title("ALS converter app")

    uploaded_file = st.file_uploader("Upload Files", type=['xlsx', 'xls'], key=11)
    if uploaded_file is not None:
        # Process the uploaded file here
        # (e.g., save it, analyze it, etc.)
        st.write("File uploaded successfully!")
        df1 = pd.read_excel(uploaded_file)
        st.write(df1)

if __name__ == "__main__":
    main()