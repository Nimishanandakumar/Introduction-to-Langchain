# Chains
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

template = """You are an expert data scientist with an expertise in building deep learning models. Explain the concept of {concept} in a couple of lines."""
prompt = PromptTemplate(input_variables=["concept"], template=template)


chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("autoencoder"))

# Second Chain
second_prompt = PromptTemplate(input_variables=["ML_Concept"], template="Turn the concept description of {ML_Concept} and explain it to me like I'm five",)
chain_two = LLMChain(llm=llm, prompt=second_prompt)
print(chain_two.run("autoencoder"))

# Text Splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_Size = 100, chunk_overlap = 0,)
texts = text_splitter.create_documents([explanation])
texts

texts[0].page_content


from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model_name="ada")

query_result = embeddings.embed_query(texts[0].page_content)
query_result