import streamlit as st
import pandas as pd
import openpyxl

def main():
    st.title("Clinical Data Standards Web Service")
    st.write("This is a main screen of app to run tools")
        # Create a tab selector


    uploaded_file = st.file_uploader("Upload Files", type=['xlsx', 'xls'], key=12)
    if uploaded_file is not None:
        # Load the workbook
        workbook = openpyxl.load_workbook(uploaded_file)

        # Select the active worksheet
        sheet = workbook.active

        # Access a specific cell
        cell = sheet['A1']

        # Get the color of the cell
        cell_color = cell.fill.start_color.index

        st.write(cell_color)  # This will print the color code




    

    st.title("Excel File Uploader and Viewer")

    uploaded_file = st.file_uploader("Upload Files", type=['xlsx', 'xls'], key=11)
    if uploaded_file is not None:
        # Process the uploaded file here
        # (e.g., save it, analyze it, etc.)
        st.write("File uploaded successfully!")
        df1 = pd.read_excel(uploaded_file)
        st.write(df1)

if __name__ == "__main__":
    main()