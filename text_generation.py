from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


from langchain.llms import OpenAI
llm = OpenAI(model_name = "text-davinci-003")
llm("Explain large language models in one sentence")

from langchain.schema import(AIMessage, HumanMessage, SystemMessage)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature=0.3)
messages = [SystemMessage(content="You are an expert data scientist"), 
            HumanMessage(content="Write a python script that trains a neural network on simulated data")]

response = chat(messages)
print(response.content, end = '\n')