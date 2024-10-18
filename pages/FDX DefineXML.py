import streamlit as st
import pandas as pd
from lxml import etree
import json
from io import StringIO, BytesIO

def main():
    st.title("Formedix Define-XML 2.0 reader")
    st.write(st.__version__)
    uploaded_file = st.file_uploader("Upload Files", type=['xml'], key=11)

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        content = uploaded_file.read()

        #st.write(content)
        
        parser = etree.XMLParser(ns_clean=True)

        tree = etree.fromstring(content, parser)

        #st.write(tree)

        json_str = xml_file_to_json(tree)
        json_content = json.loads(json_str)

        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="output.json",
            mime="application/json"
        )

        tab_main, tab1, tab2, tab3 = st.tabs(["Study", "Datasets", "Variables", "Codelists"])

        with tab_main:
            st.header("Global variables")
            data = {}
            data['FileOID'] = json_content[0]
            st.write(data)

            #df = pd.DataFrame.from_dict(data)

            #st.dataframe(df)

        with tab1:
            st.header("Datasets")

            df = pd.DataFrame.from_dict(data, orient='columns')

            st.dataframe(df)

        with tab2:
            st.header("Variables")
            st.write(json_content)

        with tab3:
            st.header("Codelists")
            st.write(json_content[0])


def xml_to_dict(element):
    # Initialize the dictionary with attributes
    result = {k: v for k, v in element.attrib.items()}
    
    # If the element has no children, just set its text
    if len(element) == 0:
        if element.text:
            result['#text'] = element.text
        return result
    
    # Otherwise, iterate over children and recursively convert them
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_result)
        else:
            result[child.tag] = child_result
    
    return result

def xml_file_to_json(tree):
    root = tree
    xml_dict = {root.tag: xml_to_dict(root)}
    json_str = json.dumps(xml_dict, ensure_ascii=False, indent=4)
    return json_str

if __name__ == "__main__":
    main()