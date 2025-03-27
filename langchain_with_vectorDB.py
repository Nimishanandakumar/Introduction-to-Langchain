import os
import pinecone
from langchain.vectorstores import Pinecone
pinecone.init(api_key = os.getenv("PINECONE_API_KEY"),
              environment = os.getenv("PINECONE_ENV"))

index_name = "langchain_quickstart"
search = Pinecone.from_documents(texts, embeddings, index_name= index_name)
query = " WHat is magical about an autoencoders"
result = search.similarity_search(query)
result