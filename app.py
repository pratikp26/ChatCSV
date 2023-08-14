import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile

def main():
    load_dotenv()

    st.set_page_config(page_title="ChatCSV 📊")
    st.header("Talk to your CSV 💬")
    st.write("Just ask a question about your data in natural language. ChatCSV will do all the heavy-lifting for you. 🤖")

    file = st.file_uploader("Upload your CSV file below:", type="csv")

    if file:
        with NamedTemporaryFile() as f:
            f.write(file.getvalue())
            user_qn = st.text_input("Ask your question below:")

            #llm = HuggingFaceHub(repo_id="bigscience/bloom", model_kwargs={"temperature":0.5, "max_length":512})
            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, f.name, verbose=True)

            if user_qn and user_qn != "":
                response = agent.run(user_qn)
                st.write(response)


if __name__ == '__main__':
    main()