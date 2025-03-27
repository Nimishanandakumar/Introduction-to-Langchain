from langchain import PromptTemplate

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

template = """ You are an expert data scientist with an expertise in building deep learning models. Explain the concept of {concept} in a couple of lines."""

prompt = PromptTemplate(input_variables=["concept"], template=template,)
prompt

llm(prompt.format(concept= "autoencoders"))