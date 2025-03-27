from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(tiktoken_model_name = "gpt-3.5-turbo", temperature=0.3)
messages = [SystemMessage(content="You are an expert data scientist"), HumanMessage(content="Write a Python Script that trains a neural network on simulated data")]
response = chat(messages)
print(response.content, end='\n')