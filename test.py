import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate  

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)  

# Correct usage of PromptTemplate
prompt = PromptTemplate(
    input_variables=['city'],
    template="Create an IT company name based on {city}."
)

# Format the prompt with the city and run it through the model
formatted_prompt = prompt.format(city="Kathmandu")
print(llm(formatted_prompt))
