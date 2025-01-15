from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate  
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Creating the prompt template
prompt = PromptTemplate(
    input_variables=["topic", "location", "date", "details"],
    template="""
    Write a news article about {topic}. The article should include the following details:
    - The article should be about an event that happened in {location} on {date}.
    - Include key facts and quotes related to the event.
    - Make the article informative, engaging, and neutral in tone.
    - The article should be appropriate for a general audience and follow standard journalistic conventions.

    Article:
    """
)

# Streamlit interface
st.title("Langchain News Article Demo with OpenAI API")
input_topic = st.text_input("Enter the news topic here")
input_location = st.text_input("Enter the location of the event")
input_date = st.text_input("Enter the date of the event")
input_details = st.text_area("Enter key details or quotes for the event")

# OpenAI LLM call
llm = ChatOpenAI(model="gpt-4o-mini") 
output_parser = StrOutputParser()

# Chain to process the prompt, model, and output parsing
chain = prompt | llm | output_parser

if input_topic and input_location and input_date and input_details:
    # Display the generated news article after invoking the chain with the inputs
    article = chain.invoke({
        'topic': input_topic,
        'location': input_location,
        'date': input_date,
        'details': input_details
    })
    st.write(article)
