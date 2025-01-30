import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2']='true'

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful assistant and answer the users queries"),
        ('user',"Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine)
    parser=StrOutputParser()
    chain=prompt|llm|parser
    response=chain.invoke({"question":question})
    return response

st.title("Simple Q&A Chatbot using Ollama")

llm=st.sidebar.selectbox("Select Open Source model",["llama3.2","deepseek-r1:1.5b"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write("Chatbot:",response)
else:
    st.write("Please enter a question")