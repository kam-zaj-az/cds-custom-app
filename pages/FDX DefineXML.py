import streamlit as st
import pandas as pd
import xmltodict
import json
from io import BytesIO

def main():
    st.title("Formedix Define-XML 2.0 reader")
    st.write(st.__version__)
    uploaded_file = st.file_uploader("Upload Files", type=['xml'], key=11)

    json_bytes = xml_file_to_json_bytes(uploaded_file)

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        xml = uploaded_file.read()
        file1_data = json.loads(json.dumps(xmltodict.parse(xml)))
        st.write(file1_data)

        st.download_button(
            label="Download JSON",
            data=file1_data,
            file_name="output.json",
            mime="application/json"
        )

# def xml_file_to_json_bytes(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     xml_dict = {root.tag: xml_to_dict(root)}
#     json_str = json.dumps(xml_dict, ensure_ascii=False, indent=4)
#     return BytesIO(json_str.encode('utf-8'))

# def xml_to_dict(element):
#     # Initialize the dictionary with attributes
#     result = {k: v for k, v in element.attrib.items()}
    
#     # If the element has no children, just set its text
#     if len(element) == 0:
#         if element.text:
#             result['#text'] = element.text
#         return result
    
#     # Otherwise, iterate over children and recursively convert them
#     for child in element:
#         child_result = xml_to_dict(child)
#         if child.tag in result:
#             if not isinstance(result[child.tag], list):
#                 result[child.tag] = [result[child.tag]]
#             result[child.tag].append(child_result)
#         else:
#             result[child.tag] = child_result
    
#     return result

if __name__ == "__main__":
    main()