from langchain.chat_models import ChatOpenAI

api_key = " "
chat_model = ChatOpenAI(openai_api_key=api_key)
result = chat_model.predict("What is the capital of France?")
print(result)