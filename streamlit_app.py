import streamlit as st
import pandas as pd
import openpyxl

def main():
    st.title("Clinical Data Standards Web Service")
    st.write("This is a main screen of app to run tools")
        # Create a tab selector

    if st.sidebar.button("Main"):
        tabs = ["None", "Upload", "Results"]
        st.write("Select the tool below:")
        selected_tab = st.selectbox("Select Tab", tabs, )

        # Display content based on the selected tab
        if selected_tab == tabs[1]:
            st.write('selected 1 tool')
            tab1()

        elif selected_tab == tabs[2]:
            st.write("This is tab 2 content")
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

    # Sidebar menu    
    if st.sidebar.button("Help", key=1):
        st.write("Help")
    if st.sidebar.button("Results", key=2):
        st.write("Results")


    

def tab1():
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