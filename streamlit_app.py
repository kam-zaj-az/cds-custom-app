import streamlit as st
import pandas as pd

def main():
    st.title("Clinical Data Standards Web Service")
    st.write("This is a main screen of app to get the info of tools:")
    x = st.slider('x')
    st.write(x, 'squared is', x * x)
    st.subheader("This is a subheader")
    st.text("This is a st.text function.")

    st.text_input("Your name", key="name")

    # You can access the value at any point with:
    if st.checkbox('Show entered name'):
        st.write(st.session_state.name)

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

    option = st.selectbox(
        'Which number do you like best?',
        df['first column'])

    'You selected: ', option
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )



if __name__ == "__main__":
    main()