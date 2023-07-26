import os
import sys

import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[0]

#Load your documents
loader = TextLoader('/Users/maxwell/Documents/MyProjects/chatGPT/data.txt')

#Create your index
index = VectorstoreIndexCreator().from_loaders([loader])
print("11")

print(index.query(query))
