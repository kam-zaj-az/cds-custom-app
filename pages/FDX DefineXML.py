import streamlit as st
import pandas as pd
import openpyxl

def main():
    st.title("RDS correction app")

    uploaded_file = st.file_uploader("Upload Files", type=['xml'], key=11)

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        df1 = xml_to_dataframe(uploaded_file)
        st.write(df1)

        excel_file = 'output.xlsx'
        save_to_excel(df1, excel_file)

def xml_to_dataframe(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    all_records = []
    columns = [elem.tag for elem in root[0]]

    for child in root:
        record = []
        for elem in child:
            record.append(elem.text)
        all_records.append(record)

    df = pd.DataFrame(all_records, columns=columns)
    return df

def save_to_excel(df, excel_file):
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    main()