from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


#creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',"you are a helpful assistant.Please provide response to the user queries"),
        ('user',"Question:{question}")
    ]
)
#streamlit 

st.title("Langchain Demo with OpenAI api")
input_text = st.text_input("search your topic here")

#open AI LLM call
llm = ChatOpenAI(model = "gpt-4o-mini")
output_parser = StrOutputParser()

#chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))