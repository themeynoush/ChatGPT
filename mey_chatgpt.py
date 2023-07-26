import os
import sys

import constants
from langchain.document_loaders import TextLoader
#from langchain.document_loaders import DirectoryLoader # To use a directory instead of a file
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[0]

#Load your documents
loader = TextLoader('/Users/maxwell/Documents/MyProjects/chatgpt/data.txt')
#loader = DirectoryLoader(".", glob="*.txt") # In case you're using line number 6

#Create your index
index = VectorstoreIndexCreator().from_loaders([loader])
#print("11")

print(index.query(query, llm=ChatOpenAI()))
