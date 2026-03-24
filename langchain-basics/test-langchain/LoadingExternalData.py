#from langchain_core.documents import Document
from langchain_community.document_loaders import CSVLoader


#document = Document("Hello, this is LangChain's document.")


FILE_PATH = "/home/sanjju/kact/langchain/langchain-basics/test-langchain/country.csv"
loader = CSVLoader(FILE_PATH)

docs = loader.load()
print(len(docs))
print(docs[1])