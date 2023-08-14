import streamlit as st

def main():
    st.set_page_config(page_title="ChatCSV 📊")
    st.header("Talk to your CSV 💬")

    file = st.file_uploader("Upload your CSV file below", type="csv")

if __name__ == '__main__':
    main()